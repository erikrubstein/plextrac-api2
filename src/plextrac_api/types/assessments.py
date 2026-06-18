from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import cast

from plextrac_api.types.common import CustomField, JsonDict, clean
from plextrac_api.types.findings import FindingSeverity
from plextrac_api.types.users import UserName


class AssessmentSortOrder(str, Enum):
    ASCENDING = "ascend"
    DESCENDING = "descend"


class TenantAssessmentSort(str, Enum):
    ALL_DESCENDING = "ALL_DESCEND"


@dataclass(slots=True)
class AnswerOption:
    label: str
    value: str
    option_id: int | str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> AnswerOption:
        return cls(
            label=str(data.get("label") or ""),
            value=str(data.get("value") or ""),
            option_id=data.get("id"),
            raw=dict(data),
        )

    def to_api(self) -> JsonDict:
        return clean({"label": self.label, "value": self.value, "id": self.option_id})


@dataclass(slots=True)
class AssessmentAnswerField:
    key: str
    label: str | None = None
    value: str | list[str] | None = None
    required: bool | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> AssessmentAnswerField:
        return cls(
            key=str(data.get("key") or ""),
            label=data.get("label"),
            value=data.get("value"),
            required=data.get("required"),
            raw=dict(data),
        )

    def to_api(self) -> JsonDict:
        return clean(
            {
                "key": self.key,
                "label": self.label,
                "value": self.value,
                "required": self.required,
            }
        )


@dataclass(slots=True)
class QuestionAnswerType:
    key: str
    label: str | None = None
    value: str | None = None
    required: bool | None = None
    multi_choice_answers: list[AnswerOption] | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> QuestionAnswerType:
        answers = data.get("multi_choice_answers")
        return cls(
            key=str(data.get("key") or ""),
            label=data.get("label"),
            value=data.get("value"),
            required=data.get("required"),
            multi_choice_answers=[
                AnswerOption.from_api(item) for item in answers if isinstance(item, dict)
            ]
            if isinstance(answers, list)
            else None,
            raw=dict(data),
        )

    def to_api(self) -> JsonDict:
        return clean(
            {
                "key": self.key,
                "label": self.label,
                "value": self.value,
                "required": self.required,
                "multi_choice_answers": [
                    answer.to_api() for answer in self.multi_choice_answers
                ]
                if self.multi_choice_answers is not None
                else None,
            }
        )


@dataclass(slots=True)
class QuestionScore:
    calculation: str | None = None
    value: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict | None) -> QuestionScore | None:
        if not isinstance(data, dict):
            return None
        return cls(
            calculation=data.get("calculation"),
            value=data.get("value"),
            raw=dict(data),
        )

    def to_api(self) -> JsonDict:
        return clean({"calculation": self.calculation, "value": self.value})


@dataclass(slots=True)
class QuestionInput:
    title: str
    text: str
    answer_type: list[QuestionAnswerType]
    category: str | None = None
    recommendations: str | None = None
    references: str | None = None
    score: QuestionScore | None = None
    severity: FindingSeverity | None = None
    tags: list[str] | None = None
    order: int | None = None
    custom_fields: list[CustomField] | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "answer_type": [answer.to_api() for answer in self.answer_type],
                "category": self.category,
                "recommendations": self.recommendations,
                "references": self.references,
                "score": self.score.to_api() if self.score is not None else None,
                "severity": self.severity.value if self.severity is not None else None,
                "text": self.text,
                "title": self.title,
                "tags": self.tags,
                "order": self.order,
                "custom_fields": [
                    field.to_api() for field in self.custom_fields
                ]
                if self.custom_fields is not None
                else None,
            }
        )


@dataclass(slots=True)
class Question:
    question_id: int | str | None = None
    title: str | None = None
    text: str | None = None
    category: str | None = None
    order: int | None = None
    answer_type: list[QuestionAnswerType] | None = None
    severity: FindingSeverity | None = None
    recommendations: str | None = None
    references: str | None = None
    score: QuestionScore | None = None
    tags: list[str] | None = None
    custom_fields: list[CustomField] | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> Question:
        answer_type = data.get("answer_type")
        custom_fields = data.get("custom_fields")
        return cls(
            question_id=data.get("qid") or data.get("question_id") or data.get("id"),
            title=data.get("title"),
            text=data.get("text") or data.get("question"),
            category=data.get("category"),
            order=data.get("order"),
            answer_type=[
                QuestionAnswerType.from_api(item) for item in answer_type if isinstance(item, dict)
            ]
            if isinstance(answer_type, list)
            else None,
            severity=_finding_severity(data.get("severity")),
            recommendations=data.get("recommendations"),
            references=data.get("references"),
            score=QuestionScore.from_api(data.get("score")),
            tags=_string_list(data.get("tags")),
            custom_fields=_custom_fields(custom_fields),
            raw=dict(data),
        )


@dataclass(slots=True)
class AnswerTypeInput:
    label: str
    values: list[AnswerOption]
    visible: bool | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "label": self.label,
                "values": [value.to_api() for value in self.values],
                "visible": self.visible,
            }
        )


@dataclass(slots=True)
class AnswerType:
    answer_type_id: int | str | None = None
    name: str | None = None
    label: str | None = None
    values: list[AnswerOption] | None = None
    visible: bool | None = None
    core: bool | None = None
    order: int | None = None
    tenant_id: int | str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> AnswerType:
        values = data.get("values")
        return cls(
            answer_type_id=data.get("id"),
            name=data.get("name"),
            label=data.get("label"),
            values=[AnswerOption.from_api(item) for item in values if isinstance(item, dict)]
            if isinstance(values, list)
            else None,
            visible=data.get("visible"),
            core=data.get("core"),
            order=data.get("order"),
            tenant_id=data.get("tenantId") or data.get("tenant_id"),
            raw=dict(data),
        )


@dataclass(slots=True)
class Framework:
    framework_id: str | None = None
    label: str | None = None
    title: str | None = None
    version: str | None = None
    categories: list[str] | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict | str | None) -> Framework | None:
        if isinstance(data, str):
            return cls(framework_id=data, raw={"id": data})
        if not isinstance(data, dict):
            return None
        return cls(
            framework_id=data.get("id"),
            label=data.get("label"),
            title=data.get("title"),
            version=data.get("version"),
            categories=_string_list(data.get("categories")),
            raw=dict(data),
        )


@dataclass(slots=True)
class QuestionnaireInput:
    assessment_title: str
    framework_id: str

    def to_api(self) -> JsonDict:
        return {"assessment_title": self.assessment_title, "framework_id": self.framework_id}


@dataclass(slots=True)
class Questionnaire:
    questionnaire_id: int | str | None = None
    assessment_title: str | None = None
    framework: Framework | None = None
    questions_count: int | None = None
    tenant_id: int | str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> Questionnaire:
        source = _nested_object(data)
        return cls(
            questionnaire_id=source.get("questionnaire_id") or source.get("questionnaireId"),
            assessment_title=source.get("assessment_title") or source.get("title"),
            framework=Framework.from_api(source.get("framework")),
            questions_count=source.get("questions_count") or source.get("questionsCount"),
            tenant_id=source.get("tenant_id") or source.get("tenantId"),
            raw=dict(data),
        )


@dataclass(slots=True)
class QuestionnaireResult:
    status: str | None = None
    message: str | None = None
    questionnaire_id: int | str | None = None
    raw: JsonDict | None = None

    @property
    def ok(self) -> bool:
        return self.status == "success" or self.questionnaire_id is not None

    @classmethod
    def from_api(cls, data: JsonDict) -> QuestionnaireResult:
        return cls(
            status=data.get("status"),
            message=data.get("message"),
            questionnaire_id=data.get("questionnaire_id") or data.get("questionnaireId"),
            raw=dict(data),
        )


@dataclass(slots=True)
class QuestionnaireExport:
    title: str | None = None
    framework_id: str | None = None
    version: str | None = None
    questions: list[Question] | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> QuestionnaireExport:
        questions = data.get("questions")
        return cls(
            title=data.get("title"),
            framework_id=data.get("framework_id") or data.get("frameworkId"),
            version=data.get("version"),
            questions=[Question.from_api(item) for item in questions if isinstance(item, dict)]
            if isinstance(questions, list)
            else None,
            raw=dict(data),
        )


@dataclass(slots=True)
class AssessmentAnswer:
    question_id: int | str
    title: str | None = None
    question: str | None = None
    answer: list[AssessmentAnswerField] | None = None
    note: str | None = None
    status: str | None = None
    custom_fields: list[CustomField] | None = None
    input_fields: list[CustomField] | None = None
    order: int | None = None
    completion_required: bool | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> AssessmentAnswer:
        answer = data.get("answer")
        return cls(
            question_id=data.get("qid") or data.get("question_id") or data.get("id") or "",
            title=data.get("title"),
            question=data.get("question"),
            answer=[
                AssessmentAnswerField.from_api(item)
                for item in answer
                if isinstance(item, dict)
            ]
            if isinstance(answer, list)
            else None,
            note=data.get("note"),
            status=data.get("status"),
            order=data.get("order"),
            completion_required=data.get("completion_required") or data.get("completionRequired"),
            raw=dict(data),
        )

    def to_api(self) -> JsonDict:
        return clean(
            {
                "qid": self.question_id,
                "title": self.title,
                "question": self.question,
                "answer": [item.to_api() for item in self.answer]
                if self.answer is not None
                else None,
                "note": self.note,
                "status": self.status,
                "custom_fields": [
                    {"custom_field": field.to_api()} for field in self.custom_fields
                ]
                if self.custom_fields is not None
                else None,
                "input_fields": [{"input_field": field.to_api()} for field in self.input_fields]
                if self.input_fields is not None
                else None,
            }
        )


@dataclass(slots=True)
class Assessment:
    assessment_id: int | str | None = None
    cuid: str | None = None
    questionnaire_id: int | str | None = None
    tenant_id: int | str | None = None
    client_id: int | str | None = None
    client_name: str | None = None
    assessment_title: str | None = None
    assessment_date: int | None = None
    framework: Framework | None = None
    answers: list[AssessmentAnswer] | None = None
    questions: list[Question] | None = None
    reviewers: list[AssessmentReviewer] | None = None
    has_reviewers: bool | None = None
    all_approved: bool | None = None
    doc_type: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> Assessment:
        source = _nested_object(data)
        answers = source.get("answers")
        questions = source.get("questions")
        reviewers = source.get("reviewers")
        return cls(
            assessment_id=source.get("assess_id") or source.get("assessmentId"),
            cuid=source.get("cuid"),
            questionnaire_id=source.get("questionnaire_id") or source.get("questionnaireId"),
            tenant_id=source.get("tenant_id") or source.get("tenantId"),
            client_id=source.get("client_id") or source.get("clientId"),
            client_name=source.get("client_name") or source.get("clientName"),
            assessment_title=source.get("assessment_title") or source.get("title"),
            assessment_date=source.get("assessment_date") or source.get("assessmentDate"),
            framework=Framework.from_api(source.get("framework")),
            answers=[
                AssessmentAnswer.from_api(item) for item in answers if isinstance(item, dict)
            ]
            if isinstance(answers, list)
            else None,
            questions=[Question.from_api(item) for item in questions if isinstance(item, dict)]
            if isinstance(questions, list)
            else None,
            reviewers=[
                AssessmentReviewer.from_api(item) for item in reviewers if isinstance(item, dict)
            ]
            if isinstance(reviewers, list)
            else None,
            has_reviewers=source.get("has_reviewers") or source.get("hasReviewers"),
            all_approved=source.get("all_approved") or source.get("allApproved"),
            doc_type=source.get("doc_type"),
            raw=dict(data),
        )


@dataclass(slots=True)
class AssessmentQuestionPage:
    questions: list[Question]
    total_count: int | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> AssessmentQuestionPage:
        questions = data.get("questions")
        pagination = data.get("pagination")
        return cls(
            questions=[Question.from_api(item) for item in questions if isinstance(item, dict)]
            if isinstance(questions, list)
            else [],
            total_count=pagination.get("total") if isinstance(pagination, dict) else None,
            raw=dict(data),
        )


@dataclass(slots=True)
class AssessmentAnswerPage:
    answers: list[AssessmentAnswer]
    total_count: int | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> AssessmentAnswerPage:
        answers = data.get("answers")
        pagination = data.get("pagination")
        return cls(
            answers=[
                AssessmentAnswer.from_api(item) for item in answers if isinstance(item, dict)
            ]
            if isinstance(answers, list)
            else [],
            total_count=pagination.get("total") if isinstance(pagination, dict) else None,
            raw=dict(data),
        )


@dataclass(slots=True)
class AssessmentReviewer:
    user_id: int | str | None = None
    cuid: str | None = None
    email: str | None = None
    name: UserName | None = None
    full_name: str | None = None
    approved: bool | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> AssessmentReviewer:
        return cls(
            user_id=data.get("user_id") or data.get("userId"),
            cuid=data.get("cuid"),
            email=data.get("email"),
            name=UserName.from_api(data.get("name")),
            full_name=data.get("fullName"),
            approved=data.get("approved"),
            raw=dict(data),
        )


@dataclass(slots=True)
class ClientAssessmentInput:
    questionnaire_id: int | str
    answers: list[AssessmentAnswer] | None = None
    reviewer_ids: list[int | str] | None = None
    has_reviewers: bool | None = None
    all_approved: bool | None = None
    save_only: bool | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "questionnaire_id": self.questionnaire_id,
                "answers": [answer.to_api() for answer in self.answers]
                if self.answers is not None
                else None,
                "reviewers": self.reviewer_ids,
                "has_reviewers": self.has_reviewers,
                "all_approved": self.all_approved,
                "saveOnly": self.save_only,
            }
        )


@dataclass(slots=True)
class AssessmentCreateResult:
    status: str | None = None
    message: str | None = None
    document_id: str | None = None
    assessment_id: int | str | None = None
    raw: JsonDict | None = None

    @property
    def ok(self) -> bool:
        return (
            self.status == "success"
            or self.document_id is not None
            or self.assessment_id is not None
        )

    @classmethod
    def from_api(cls, data: JsonDict) -> AssessmentCreateResult:
        source = _nested_object(data)
        return cls(
            status=data.get("status"),
            message=source.get("message") or data.get("message"),
            document_id=source.get("doc_id") or data.get("doc_id"),
            assessment_id=data.get("assessment_id") or data.get("assessmentId"),
            raw=dict(data),
        )


@dataclass(slots=True)
class AssessmentReportCreateResult:
    status: str | None = None
    message: str | None = None
    report_id: int | str | None = None
    raw: JsonDict | None = None

    @property
    def ok(self) -> bool:
        return self.status == "success" or self.report_id is not None

    @classmethod
    def from_api(cls, data: JsonDict) -> AssessmentReportCreateResult:
        source = _nested_object(data)
        return cls(
            status=source.get("status") or data.get("status"),
            message=source.get("message") or data.get("message"),
            report_id=source.get("report_id") or source.get("reportId"),
            raw=dict(data),
        )


def _finding_severity(value: object) -> FindingSeverity | None:
    if isinstance(value, FindingSeverity):
        return value
    if isinstance(value, str):
        try:
            return FindingSeverity(value)
        except ValueError:
            return None
    return None


def _string_list(value: object) -> list[str] | None:
    if isinstance(value, list):
        return [str(item) for item in value]
    return None


def _nested_object(data: JsonDict) -> JsonDict:
    nested = data.get("data")
    if isinstance(nested, dict):
        return cast(JsonDict, nested)
    return data


def _custom_fields(value: object) -> list[CustomField] | None:
    if not isinstance(value, list):
        return None
    fields: list[CustomField] = []
    for item in value:
        if isinstance(item, dict):
            field = CustomField.from_api(cast(JsonDict, item))
            if field is not None:
                fields.append(field)
    return fields
