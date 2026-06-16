from __future__ import annotations

from dataclasses import dataclass

from plextrac_api.types.common import CustomField, JsonDict


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


@dataclass(slots=True)
class Report:
    id: int | str | None = None
    client_id: int | str | None = None
    name: str | None = None
    status: str | None = None
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
            status=data.get("status"),
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
