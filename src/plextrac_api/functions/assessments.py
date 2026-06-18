from __future__ import annotations

from pathlib import Path
from typing import BinaryIO, cast

from plextrac_api.functions.common import rest_request
from plextrac_api.types.assessments import (
    AnswerType,
    AnswerTypeInput,
    Assessment,
    AssessmentAnswer,
    AssessmentAnswerPage,
    AssessmentCreateResult,
    AssessmentQuestionPage,
    AssessmentReportCreateResult,
    AssessmentReviewer,
    AssessmentSortOrder,
    ClientAssessmentInput,
    Question,
    QuestionInput,
    Questionnaire,
    QuestionnaireExport,
    QuestionnaireInput,
    QuestionnaireResult,
    TenantAssessmentSort,
)
from plextrac_api.types.auth import AuthSession
from plextrac_api.types.common import JsonDict, OperationResult


def list_questions(
    session: AuthSession,
    questionnaire_id: int | str,
    *,
    limit: int = 50,
    offset: int = 0,
) -> list[Question]:
    """List questions for a questionnaire."""
    data = rest_request(
        session,
        "GET",
        f"/api/v2/assessments/questionnaires/{questionnaire_id}/questions",
        params={"limit": limit, "offset": offset},
    )
    return [Question.from_api(item) for item in _dict_items(data)]


def get_question(
    session: AuthSession,
    questionnaire_id: int | str,
    question_id: int | str,
) -> Question:
    """Get one questionnaire question."""
    data = rest_request(
        session,
        "GET",
        f"/api/v2/assessments/questionnaires/{questionnaire_id}/questions/{question_id}",
    )
    return Question.from_api(_object(data, "question"))


def create_question(
    session: AuthSession,
    questionnaire_id: int | str,
    question: QuestionInput,
) -> Question:
    """Create a questionnaire question."""
    data = rest_request(
        session,
        "POST",
        f"/api/v2/assessments/questionnaires/{questionnaire_id}/questions",
        json=question.to_api(),
    )
    return Question.from_api(_object(data, "question"))


def update_question(
    session: AuthSession,
    questionnaire_id: int | str,
    question_id: int | str,
    question: QuestionInput,
) -> OperationResult:
    """Update a questionnaire question."""
    data = rest_request(
        session,
        "PUT",
        f"/api/v2/assessments/questionnaires/{questionnaire_id}/questions/{question_id}",
        json=question.to_api(),
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def change_question_order(
    session: AuthSession,
    questionnaire_id: int | str,
    question_id: int | str,
    *,
    order: int,
) -> OperationResult:
    """Change a questionnaire question's display order."""
    data = rest_request(
        session,
        "PUT",
        f"/api/v2/assessments/questionnaires/{questionnaire_id}/questions/{question_id}/order",
        json={"order": order},
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def delete_question(
    session: AuthSession,
    questionnaire_id: int | str,
    question_id: int | str,
) -> OperationResult:
    """Delete a questionnaire question."""
    data = rest_request(
        session,
        "DELETE",
        f"/api/v2/assessments/questionnaires/{questionnaire_id}/questions/{question_id}",
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def list_answer_types(
    session: AuthSession,
    tenant_id: int | str,
    client_id: int | str,
    *,
    limit: int = 10,
    offset: int = 0,
) -> list[AnswerType]:
    """List answer types available to a tenant/client."""
    data = rest_request(
        session,
        "POST",
        f"/api/v2/tenant/{tenant_id}/client/{client_id}/answertypes",
        json={"pagination": {"limit": limit, "offset": offset}},
    )
    return [AnswerType.from_api(item) for item in _dict_items(data)]


def get_answer_type(
    session: AuthSession,
    tenant_id: int | str,
    client_id: int | str,
    answer_type_id: int | str,
) -> AnswerType:
    """Get one answer type."""
    data = rest_request(
        session,
        "GET",
        f"/api/v2/tenant/{tenant_id}/client/{client_id}/answertypes/{answer_type_id}",
    )
    return AnswerType.from_api(_object(data, "answer type"))


def update_answer_type(
    session: AuthSession,
    tenant_id: int | str,
    client_id: int | str,
    answer_type_id: int | str,
    answer_type: AnswerTypeInput,
) -> AnswerType:
    """Update an answer type."""
    data = rest_request(
        session,
        "PUT",
        f"/api/v2/tenant/{tenant_id}/client/{client_id}/answertypes/{answer_type_id}",
        json=answer_type.to_api(),
    )
    return AnswerType.from_api(_object(data, "answer type"))


def create_answer_type(
    session: AuthSession,
    tenant_id: int | str,
    client_id: int | str,
    answer_type: AnswerTypeInput,
) -> AnswerType:
    """Create an answer type."""
    data = rest_request(
        session,
        "POST",
        f"/api/v2/tenant/{tenant_id}/client/{client_id}/answertypes/create",
        json=answer_type.to_api(),
    )
    return AnswerType.from_api(_object(data, "answer type"))


def delete_answer_type(
    session: AuthSession,
    tenant_id: int | str,
    client_id: int | str,
    answer_type_id: int | str,
) -> OperationResult:
    """Delete an answer type."""
    data = rest_request(
        session,
        "DELETE",
        f"/api/v2/tenant/{tenant_id}/client/{client_id}/answertypes/{answer_type_id}",
    )
    return OperationResult.from_api({"data": data})


def list_questionnaires(
    session: AuthSession,
    tenant_id: int | str,
) -> list[Questionnaire]:
    """List questionnaires for a tenant."""
    data = rest_request(session, "GET", f"/api/v1/tenant/{tenant_id}/assessments")
    return [Questionnaire.from_api(item) for item in _dict_items(data)]


def get_questionnaire(
    session: AuthSession,
    questionnaire_id: int | str,
) -> Questionnaire:
    """Get one questionnaire."""
    data = rest_request(session, "GET", f"/api/v2/assessments/questionnaires/{questionnaire_id}")
    return Questionnaire.from_api(_object(data, "questionnaire"))


def create_questionnaire(
    session: AuthSession,
    questionnaire: QuestionnaireInput,
) -> QuestionnaireResult:
    """Create a questionnaire."""
    data = rest_request(
        session,
        "POST",
        "/api/v2/assessments/questionnaires",
        json=questionnaire.to_api(),
    )
    return QuestionnaireResult.from_api(_object(data, "questionnaire result"))


def update_questionnaire(
    session: AuthSession,
    questionnaire_id: int | str,
    questionnaire: QuestionnaireInput,
) -> QuestionnaireResult:
    """Update a questionnaire."""
    data = rest_request(
        session,
        "PUT",
        f"/api/v2/assessments/questionnaires/{questionnaire_id}",
        json=questionnaire.to_api(),
    )
    return QuestionnaireResult.from_api(_object(data, "questionnaire result"))


def delete_questionnaire(
    session: AuthSession,
    tenant_id: int | str,
    questionnaire_id: int | str,
) -> OperationResult:
    """Delete a questionnaire."""
    data = rest_request(
        session,
        "DELETE",
        f"/api/v1/tenant/{tenant_id}/assessment/{questionnaire_id}",
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def export_questionnaire(
    session: AuthSession,
    questionnaire_id: int | str,
) -> QuestionnaireExport:
    """Export a questionnaire definition."""
    data = rest_request(session, "GET", f"/api/v2/assessments/questionnaires/{questionnaire_id}/export")
    return QuestionnaireExport.from_api(_object(data, "questionnaire export"))


def import_questionnaire(
    session: AuthSession,
    file: str | Path | BinaryIO,
    *,
    filename: str | None = None,
    content_type: str | None = None,
) -> QuestionnaireResult:
    """Import a questionnaire definition."""
    data = _upload_file(
        session,
        "/api/v2/import/questionnaire",
        file,
        filename=filename,
        content_type=content_type,
        fallback_name="questionnaire.json",
    )
    return QuestionnaireResult.from_api(_object(data, "questionnaire import"))


def list_tenant_assessments(
    session: AuthSession,
    tenant_id: int | str,
    *,
    limit: int = 10,
    offset: int = 0,
    order: AssessmentSortOrder = AssessmentSortOrder.ASCENDING,
    sort: TenantAssessmentSort = TenantAssessmentSort.ALL_DESCENDING,
) -> list[Assessment]:
    """List assessments for a tenant."""
    data = rest_request(
        session,
        "GET",
        f"/api/v2/tenants/{tenant_id}/assessments",
        params={"limit": limit, "offset": offset, "order": order.value, "sort": sort.value},
    )
    items = data.get("assessments") if isinstance(data, dict) else None
    return [Assessment.from_api(item) for item in items if isinstance(item, dict)] if isinstance(items, list) else []


def list_client_assessments(
    session: AuthSession,
    tenant_id: int | str,
    client_id: int | str,
    *,
    limit: int = 10,
    offset: int = 0,
    order: AssessmentSortOrder = AssessmentSortOrder.ASCENDING,
    sort: int = 0,
) -> list[Assessment]:
    """List assessments for a client using the latest paginated endpoint."""
    data = rest_request(
        session,
        "GET",
        f"/api/v2/tenants/{tenant_id}/clients/{client_id}/assessments",
        params={"limit": limit, "offset": offset, "order": order.value, "sort": sort},
    )
    items = data.get("assessments") if isinstance(data, dict) else None
    return [Assessment.from_api(item) for item in items if isinstance(item, dict)] if isinstance(items, list) else []


def get_client_assessment_details(
    session: AuthSession,
    tenant_id: int | str,
    client_id: int | str,
    assessment_id: int | str,
) -> Assessment:
    """Get a client assessment with questions and answers."""
    data = rest_request(
        session,
        "GET",
        f"/api/v1/tenant/{tenant_id}/client/{client_id}/assessment/{assessment_id}",
    )
    return Assessment.from_api(_object(data, "client assessment"))


def get_client_assessment(
    session: AuthSession,
    tenant_id: int | str,
    client_id: int | str,
    assessment_id: int | str,
) -> Assessment:
    """Get one client assessment."""
    data = rest_request(
        session,
        "GET",
        f"/api/v2/tenants/{tenant_id}/clients/{client_id}/assessments/{assessment_id}",
    )
    return Assessment.from_api(_object(data, "client assessment"))


def get_assessment_by_cuid(
    session: AuthSession,
    assessment_cuid: str,
) -> Assessment:
    """Get one assessment by CUID."""
    data = rest_request(session, "GET", f"/api/v2/assessments/{assessment_cuid}")
    return Assessment.from_api(_object(data, "assessment"))


def list_assessment_questions(
    session: AuthSession,
    tenant_id: int | str,
    client_id: int | str,
    assessment_id: int | str,
    *,
    limit: int = 3,
    offset: int = 0,
    order: AssessmentSortOrder = AssessmentSortOrder.ASCENDING,
) -> AssessmentQuestionPage:
    """List questions for a client assessment."""
    data = rest_request(
        session,
        "GET",
        f"/api/v2/tenants/{tenant_id}/clients/{client_id}/assessments/{assessment_id}/questions",
        params={"limit": limit, "offset": offset, "order": order.value},
    )
    return AssessmentQuestionPage.from_api(_object(data, "assessment questions"))


def list_assessment_answers(
    session: AuthSession,
    tenant_id: int | str,
    client_id: int | str,
    assessment_id: int | str,
    *,
    limit: int = 3,
    offset: int = 0,
    order: AssessmentSortOrder = AssessmentSortOrder.ASCENDING,
) -> AssessmentAnswerPage:
    """List answers for a client assessment."""
    data = rest_request(
        session,
        "GET",
        f"/api/v2/tenants/{tenant_id}/clients/{client_id}/assessments/{assessment_id}/answers",
        params={"limit": limit, "offset": offset, "order": order.value},
    )
    return AssessmentAnswerPage.from_api(_object(data, "assessment answers"))


def update_assessment_answers(
    session: AuthSession,
    tenant_id: int | str,
    client_id: int | str,
    assessment_id: int | str,
    answers: list[AssessmentAnswer],
) -> Assessment:
    """Update answers for a client assessment."""
    data = rest_request(
        session,
        "PUT",
        f"/api/v2/tenants/{tenant_id}/clients/{client_id}/assessments/{assessment_id}/answers",
        json={"answers": [answer.to_api() for answer in answers]},
    )
    return Assessment.from_api(_object(data, "assessment"))


def list_assessment_reviewers(
    session: AuthSession,
    tenant_id: int | str,
    client_id: int | str,
    assessment_id: int | str,
) -> list[AssessmentReviewer]:
    """List reviewers for a client assessment."""
    data = rest_request(
        session,
        "GET",
        f"/api/v2/tenants/{tenant_id}/clients/{client_id}/assessments/{assessment_id}/reviewers",
    )
    items = data.get("reviewers") if isinstance(data, dict) else None
    return [AssessmentReviewer.from_api(item) for item in items if isinstance(item, dict)] if isinstance(items, list) else []


def create_client_assessment(
    session: AuthSession,
    tenant_id: int | str,
    client_id: int | str,
    assessment: ClientAssessmentInput,
) -> AssessmentCreateResult:
    """Create a client assessment from a questionnaire."""
    data = rest_request(
        session,
        "POST",
        f"/api/v1/tenant/{tenant_id}/client/{client_id}/assessment",
        json=assessment.to_api(),
    )
    return AssessmentCreateResult.from_api(_object(data, "assessment create result"))


def update_client_assessment(
    session: AuthSession,
    tenant_id: int | str,
    client_id: int | str,
    assessment_id: int | str,
    assessment: ClientAssessmentInput,
) -> AssessmentCreateResult:
    """Update a client assessment."""
    data = rest_request(
        session,
        "PUT",
        f"/api/v1/tenant/{tenant_id}/client/{client_id}/assessment/{assessment_id}",
        json=assessment.to_api(),
    )
    return AssessmentCreateResult.from_api(_object(data, "assessment update result"))


def delete_client_assessment(
    session: AuthSession,
    tenant_id: int | str,
    client_id: int | str,
    assessment_id: int | str,
) -> AssessmentCreateResult:
    """Delete a client assessment."""
    data = rest_request(
        session,
        "DELETE",
        f"/api/v1/tenant/{tenant_id}/client/{client_id}/assessment/{assessment_id}",
    )
    return AssessmentCreateResult.from_api(_object(data, "assessment delete result"))


def create_report_from_assessment_questionnaire(
    session: AuthSession,
    tenant_id: int | str,
    client_id: int | str,
    assessment_id: int | str,
    *,
    questionnaire_id: int | str,
    answers: list[AssessmentAnswer] | None = None,
) -> AssessmentReportCreateResult:
    """Create a report from an assessment questionnaire."""
    data = rest_request(
        session,
        "POST",
        f"/api/v1/tenant/{tenant_id}/client/{client_id}/assessment/{assessment_id}/report",
        json={
            "questionnaire_id": questionnaire_id,
            "answers": [answer.to_api() for answer in answers] if answers is not None else [],
        },
    )
    return AssessmentReportCreateResult.from_api(_object(data, "assessment report create result"))


def copy_assessment_questionnaire(
    session: AuthSession,
    tenant_id: int | str,
    client_id: int | str,
    assessment_id: int | str,
) -> AssessmentCreateResult:
    """Copy an assessment questionnaire."""
    data = rest_request(
        session,
        "POST",
        f"/api/v2/tenants/{tenant_id}/clients/{client_id}/assessments/{assessment_id}/copy",
    )
    return AssessmentCreateResult.from_api(_object(data, "assessment copy result"))


def _upload_file(
    session: AuthSession,
    path: str,
    file: str | Path | BinaryIO,
    *,
    filename: str | None,
    content_type: str | None,
    fallback_name: str,
) -> object:
    close_after = None
    if isinstance(file, (str, Path)):
        file_path = Path(file)
        close_after = file_path.open("rb")
        file_obj: BinaryIO = close_after
        upload_name = filename or file_path.name
    else:
        file_obj = file
        upload_name = filename or Path(getattr(file, "name", fallback_name)).name

    files = {"file": (upload_name, file_obj, content_type) if content_type else (upload_name, file_obj)}
    try:
        return rest_request(session, "POST", path, files=files)
    finally:
        if close_after is not None:
            close_after.close()


def _object(data: object, label: str) -> JsonDict:
    if isinstance(data, dict):
        nested = data.get("data")
        if isinstance(nested, dict):
            return cast(JsonDict, nested)
        return cast(JsonDict, data)
    raise ValueError(f"PlexTrac {label} response was not a JSON object.")


def _dict_items(data: object) -> list[JsonDict]:
    if isinstance(data, dict):
        nested = data.get("data")
        if isinstance(nested, list):
            return [cast(JsonDict, item) for item in nested if isinstance(item, dict)]
        return []
    return [cast(JsonDict, item) for item in data if isinstance(item, dict)] if isinstance(data, list) else []
