from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from plextrac_api.types.common import CustomField, JsonDict, SortOrder, clean


class ReportStatus(str, Enum):
    DRAFT = "Draft"
    READY_FOR_REVIEW = "Ready For Review"
    IN_REVIEW = "In Review"
    APPROVED = "Approved"
    PUBLISHED = "Published"


class ReportSortField(str, Enum):
    NAME = "name"
    STATUS = "status"


class ReportFilterField(str, Enum):
    NAME = "name"
    REVIEWERS = "reviewers"
    OPERATORS = "operators"
    CLIENTS = "clients"
    STATUS = "status"
    CUIDS = "cuids"


@dataclass(slots=True)
class Narrative:
    id: str | None = None
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
            id=data.get("id"),
            label=data.get("label"),
            tags=data.get("tags") if isinstance(data.get("tags"), list) else None,
            text=data.get("text"),
            is_from_narratives_db=data.get("isFromNarrativesDB"),
            raw=dict(data),
        )

    def to_api(self) -> JsonDict:
        return clean(
            {
                "id": self.id,
                "label": self.label,
                "tags": self.tags,
                "text": self.text,
                "isFromNarrativesDB": self.is_from_narratives_db,
            }
        )


@dataclass(slots=True)
class ReportDraft:
    name: str
    status: ReportStatus | None = None
    include_evidence: bool | None = None
    tags: list[str] | None = None
    custom_fields: list[CustomField] | None = None
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
            template=self.template,
            start_date=self.start_date,
            end_date=self.end_date,
            fields_template=self.fields_template,
            is_track_changes=self.is_track_changes,
        )


@dataclass(slots=True)
class ReportPatch:
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
class Report:
    id: int | str | None = None
    client_id: int | str | None = None
    name: str | None = None
    status: ReportStatus | None = None
    include_evidence: bool | None = None
    report_type: str | None = None
    tags: list[str] | None = None
    custom_fields: list[CustomField] | None = None
    narratives: list[Narrative] | None = None
    template: str | None = None
    fields_template: str | None = None
    start_date: str | None = None
    end_date: str | None = None
    is_track_changes: bool | None = None
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
            id=data.get("report_id") or data.get("id") or data.get("cuid"),
            client_id=data.get("client_id"),
            name=data.get("name"),
            status=_report_status(data.get("status")),
            include_evidence=data.get("includeEvidence"),
            report_type=data.get("reportType"),
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
            fields_template=data.get("fields_template"),
            start_date=data.get("start_date"),
            end_date=data.get("end_date"),
            is_track_changes=data.get("isTrackChanges"),
            doc_type=data.get("doc_type"),
            raw=dict(data),
        )


@dataclass(slots=True)
class ReportSummary:
    id: str | None = None
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
            id=data.get("id"),
            report_id=_list_value(values, 0) or data.get("report_id") or data.get("id"),
            client_id=_list_value(doc_ids, 0) or data.get("client_id"),
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
        return cls(
            count=data.get("count") if isinstance(data.get("count"), int) else None,
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
    id: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> ReportExhibit:
        return cls(id=data.get("id"), raw=dict(data))


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
            "custom_field": [
                clean({"label": field.label, "value": field.value})
                for field in custom_fields or []
            ]
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
