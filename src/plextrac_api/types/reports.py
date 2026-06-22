from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum, StrEnum

from plextrac_api.types.common import CustomField, JsonDict, SortOrder, clean


class ReportPageLimit(IntEnum):
    FIVE = 5
    TEN = 10
    TWENTY_FIVE = 25
    FIFTY = 50
    ONE_HUNDRED = 100
    ONE_THOUSAND = 1000


class ReportStatus(StrEnum):
    DRAFT = "Draft"
    READY_FOR_REVIEW = "Ready For Review"
    IN_REVIEW = "In Review"
    APPROVED = "Approved"
    PUBLISHED = "Published"


class ReportSortField(StrEnum):
    NAME = "name"
    STATUS = "status"


class ReportFilterField(StrEnum):
    NAME = "name"
    REVIEWERS = "reviewers"
    OPERATORS = "operators"
    CLIENTS = "clients"
    STATUS = "status"
    CUIDS = "cuids"


@dataclass(slots=True)
class ReportPagination:
    offset: int = 0
    limit: ReportPageLimit = ReportPageLimit.TWENTY_FIVE

    def to_api(self) -> JsonDict:
        return {"offset": self.offset, "limit": int(self.limit)}


@dataclass(slots=True)
class Narrative:
    narrative_id: str | None = None
    label: str | None = None
    tags: list[str] | None = None
    text: str | None = None
    is_from_narratives_db: bool | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict | None) -> Narrative | None:
        if not data:
            return None
        return cls(
            narrative_id=data.get("id") or data.get("narrativeId"),
            label=data.get("label"),
            tags=data.get("tags") if isinstance(data.get("tags"), list) else None,
            text=data.get("text"),
            is_from_narratives_db=data.get("isFromNarrativesDB"),
            raw=dict(data),
        )

    def to_api(self) -> JsonDict:
        return clean(
            {
                "id": self.narrative_id,
                "label": self.label,
                "tags": self.tags,
                "text": self.text,
                "isFromNarrativesDB": self.is_from_narratives_db,
            }
        )


@dataclass(slots=True)
class ReportInput:
    name: str | None = None
    status: ReportStatus | None = None
    include_evidence: bool | None = None
    tags: list[str] | None = None
    custom_fields: list[CustomField] | None = None
    narratives: list[Narrative] | None = None
    template: str | None = None
    start_date: str | None = None
    end_date: str | None = None
    fields_template: str | None = None
    is_track_changes: bool | None = None

    def to_api(self) -> JsonDict:
        return _report_payload(
            name=self.name,
            status=self.status,
            include_evidence=self.include_evidence,
            tags=self.tags,
            custom_fields=self.custom_fields,
            narratives=self.narratives,
            template=self.template,
            start_date=self.start_date,
            end_date=self.end_date,
            fields_template=self.fields_template,
            is_track_changes=self.is_track_changes,
        )


@dataclass(slots=True)
class ReportCreateResult:
    report_id: int | str | None = None
    status: str | None = None
    message: str | None = None
    raw: JsonDict | None = None

    @property
    def ok(self) -> bool:
        return _is_success_text(self.status) or _is_success_text(self.message)

    @classmethod
    def from_api(cls, data: JsonDict) -> ReportCreateResult:
        nested = data.get("data") if isinstance(data.get("data"), dict) else {}
        return cls(
            report_id=data.get("report_id")
            or data.get("reportId")
            or data.get("id")
            or nested.get("report_id")
            or nested.get("reportId")
            or nested.get("id"),
            status=data.get("status") or data.get("result"),
            message=data.get("message") or data.get("detail"),
            raw=dict(data),
        )


@dataclass(slots=True)
class Report:
    report_id: int | str | None = None
    cuid: str | None = None
    client_id: int | str | None = None
    name: str | None = None
    status: ReportStatus | None = None
    created_at: int | str | None = None
    include_evidence: bool | None = None
    report_type: str | None = None
    report_source: str | None = None
    tags: list[str] | None = None
    custom_fields: list[CustomField] | None = None
    narratives: list[Narrative] | None = None
    template: str | None = None
    fields_template: str | None = None
    template_name: str | None = None
    fields_template_name: str | None = None
    start_date: str | None = None
    end_date: str | None = None
    is_track_changes: bool | None = None
    findings_count: int | None = None
    doc_type: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> Report:
        custom_fields = data.get("custom_field")
        exec_summary = data.get("exec_summary")
        narrative_items = data.get("custom_fields")
        if isinstance(exec_summary, dict) and not narrative_items:
            narrative_items = exec_summary.get("custom_fields")

        return cls(
            report_id=data.get("report_id") or data.get("reportId") or data.get("id"),
            cuid=data.get("cuid"),
            client_id=data.get("client_id") or data.get("clientId"),
            name=data.get("name"),
            status=_report_status(data.get("status")),
            created_at=data.get("created_at") or data.get("createdAt"),
            include_evidence=_first_present(data, ("includeEvidence", "include_evidence")),
            report_type=data.get("reportType") or data.get("report_type"),
            report_source=data.get("reportSource") or data.get("report_source"),
            tags=data.get("tags") if isinstance(data.get("tags"), list) else None,
            custom_fields=[
                field
                for field in (CustomField.from_api(item) for item in custom_fields or [])
                if field is not None
            ]
            if isinstance(custom_fields, list)
            else None,
            narratives=[
                narrative
                for narrative in (Narrative.from_api(item) for item in narrative_items or [])
                if narrative is not None
            ]
            if isinstance(narrative_items, list)
            else None,
            template=data.get("template"),
            fields_template=data.get("fields_template") or data.get("fieldsTemplate"),
            template_name=data.get("template_name") or data.get("templateName"),
            fields_template_name=data.get("fields_template_name") or data.get("fieldsTemplateName"),
            start_date=data.get("start_date") or data.get("startDate"),
            end_date=data.get("end_date") or data.get("endDate"),
            is_track_changes=_first_present(data, ("isTrackChanges", "is_track_changes")),
            findings_count=data.get("findings") if isinstance(data.get("findings"), int) else None,
            doc_type=data.get("doc_type") or data.get("docType"),
            raw=dict(data),
        )


@dataclass(slots=True)
class ReportSummary:
    cuid: str | None = None
    report_id: int | str | None = None
    client_id: int | str | None = None
    name: str | None = None
    status: ReportStatus | None = None
    tags: list[str] | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> ReportSummary:
        values = data.get("data")
        doc_ids = data.get("doc_id")
        tags = _list_value(values, 10)
        return cls(
            cuid=data.get("cuid") or data.get("id"),
            report_id=_list_value(values, 0) or data.get("report_id") or data.get("reportId"),
            client_id=_list_value(doc_ids, 0) or data.get("client_id") or data.get("clientId"),
            name=_list_value(values, 1) or data.get("name"),
            status=_report_status(_list_value(values, 3) or data.get("status")),
            tags=tags if isinstance(tags, list) else data.get("tags"),
            raw=dict(data),
        )


@dataclass(slots=True)
class ReportPage:
    reports: list[Report]
    total_count: int | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict | list[JsonDict]) -> ReportPage:
        if isinstance(data, list):
            return cls(
                reports=[Report.from_api(item) for item in data if isinstance(item, dict)],
                raw={"data": data},
            )

        items = _first_list(data, ("reports", "data", "items", "results"))
        return cls(
            reports=[Report.from_api(item) for item in items if isinstance(item, dict)],
            total_count=_first_int(data, ("total", "totalCount", "count")),
            raw=dict(data),
        )


@dataclass(slots=True)
class ReportPtracExport:
    report_info: JsonDict | None = None
    findings: list[JsonDict] | None = None
    summary: JsonDict | None = None
    evidence: JsonDict | list[JsonDict] | None = None
    client_info: JsonDict | None = None
    procedures: list[JsonDict] | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> ReportPtracExport:
        report_info = data.get("report_info")
        findings = data.get("flaws_array")
        summary = data.get("summary")
        evidence = data.get("evidence")
        client_info = data.get("client_info")
        procedures = data.get("procedures")
        return cls(
            report_info=report_info if isinstance(report_info, dict) else None,
            findings=findings if isinstance(findings, list) else None,
            summary=summary if isinstance(summary, dict) else None,
            evidence=evidence if isinstance(evidence, (dict, list)) else None,
            client_info=client_info if isinstance(client_info, dict) else None,
            procedures=procedures if isinstance(procedures, list) else None,
            raw=dict(data),
        )


@dataclass(slots=True)
class ReportSort:
    by: ReportSortField
    order: SortOrder = SortOrder.ASCENDING

    def to_api(self) -> JsonDict:
        return {"by": self.by.value, "order": self.order.value}


@dataclass(slots=True)
class ReportFilter:
    by: ReportFilterField
    value: str | list[str] | list[int]

    def to_api(self) -> JsonDict:
        return {"by": self.by.value, "value": self.value}


@dataclass(slots=True)
class ReportSearchOccurrenceResult:
    count: int | None = None
    status: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> ReportSearchOccurrenceResult:
        count = data.get("count")
        if not isinstance(count, int):
            count = data.get("data")
        return cls(
            count=count if isinstance(count, int) else None,
            status=data.get("status"),
            raw=dict(data),
        )


@dataclass(slots=True)
class ReportReplaceResult:
    replaced: bool | None = None
    status: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> ReportReplaceResult:
        replaced = data.get("data")
        return cls(
            replaced=replaced if isinstance(replaced, bool) else None,
            status=data.get("status"),
            raw=dict(data),
        )


@dataclass(slots=True)
class ReportExhibit:
    exhibit_id: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> ReportExhibit:
        return cls(exhibit_id=data.get("id") or data.get("exhibitId"), raw=dict(data))


def _report_payload(
    *,
    name: str | None = None,
    status: ReportStatus | None = None,
    include_evidence: bool | None = None,
    tags: list[str] | None = None,
    custom_fields: list[CustomField] | None = None,
    narratives: list[Narrative] | None = None,
    template: str | None = None,
    start_date: str | None = None,
    end_date: str | None = None,
    fields_template: str | None = None,
    is_track_changes: bool | None = None,
) -> JsonDict:
    return clean(
        {
            "name": name,
            "status": status.value if status is not None else None,
            "includeEvidence": include_evidence,
            "tags": tags,
            "custom_field": [field.to_api() for field in custom_fields or []]
            if custom_fields is not None
            else None,
            "exec_summary": {"custom_fields": [item.to_api() for item in narratives]}
            if narratives is not None
            else None,
            "template": template,
            "start_date": start_date,
            "end_date": end_date,
            "fields_template": fields_template,
            "isTrackChanges": is_track_changes,
        }
    )


def _first_list(data: JsonDict, keys: tuple[str, ...]) -> list[JsonDict]:
    for key in keys:
        value = data.get(key)
        if isinstance(value, list):
            return value
        if isinstance(value, dict):
            nested = _first_list(value, keys)
            if nested:
                return nested
    return []


def _first_int(data: JsonDict, keys: tuple[str, ...]) -> int | None:
    for key in keys:
        value = data.get(key)
        if isinstance(value, int):
            return value
        if isinstance(value, dict):
            nested = _first_int(value, keys)
            if nested is not None:
                return nested
    return None


def _report_status(value: object) -> ReportStatus | None:
    if isinstance(value, ReportStatus):
        return value
    if isinstance(value, str):
        try:
            return ReportStatus(value)
        except ValueError:
            return None
    return None


def _list_value(value: object, index: int) -> object:
    if isinstance(value, list) and len(value) > index:
        return value[index]
    return None


def _first_present(data: JsonDict, keys: tuple[str, ...]) -> object:
    for key in keys:
        if key in data:
            return data[key]
    return None


def _is_success_text(value: object) -> bool:
    if not isinstance(value, str):
        return False
    return value.lower() in {
        "ok",
        "success",
        "successful",
        "created",
    }
