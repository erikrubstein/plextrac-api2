from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import cast

from plextrac_api.types.common import CustomField, JsonDict, clean


class ExportTemplateType(str, Enum):
    CUSTOM = "custom"


@dataclass(slots=True)
class TemplateSection:
    label: str | None = None
    text: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict | None) -> TemplateSection | None:
        if not data:
            return None
        return cls(label=data.get("label"), text=data.get("text"), raw=dict(data))

    def to_api(self) -> JsonDict:
        return clean({"label": self.label, "text": self.text})


@dataclass(slots=True)
class TemplateField:
    label: str | None = None
    value: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict | None) -> TemplateField | None:
        if not data:
            return None
        return cls(label=data.get("label"), value=data.get("value"), raw=dict(data))

    def to_api(self) -> JsonDict:
        return clean({"label": self.label, "value": self.value})


@dataclass(slots=True)
class ReportTemplateInput:
    template_name: str | None = None
    export_template: str | None = None
    custom_fields: list[TemplateSection] | None = None
    report_custom_fields: list[CustomField] | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "template_name": self.template_name,
                "export_template": self.export_template,
                "custom_fields": [field.to_api() for field in self.custom_fields]
                if self.custom_fields is not None
                else None,
                "report_custom_fields": [field.to_api() for field in self.report_custom_fields]
                if self.report_custom_fields is not None
                else None,
            }
        )


@dataclass(slots=True)
class ReportTemplate:
    template_id: str | None = None
    template_name: str | None = None
    export_template: str | None = None
    tenant_id: int | str | None = None
    custom_fields: list[TemplateSection] | None = None
    report_custom_fields: list[CustomField] | None = None
    doc_type: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> ReportTemplate:
        payload = _nested_payload(data)
        custom_fields = payload.get("custom_fields")
        report_custom_fields = payload.get("report_custom_fields")
        return cls(
            template_id=payload.get("doc_id") or payload.get("id"),
            template_name=payload.get("template_name") or payload.get("name"),
            export_template=payload.get("export_template"),
            tenant_id=payload.get("tenant_id"),
            custom_fields=[
                field
                for field in (
                    TemplateSection.from_api(item)
                    for item in custom_fields
                    if isinstance(item, dict)
                )
                if field is not None
            ]
            if isinstance(custom_fields, list)
            else None,
            report_custom_fields=[
                field
                for field in (
                    CustomField.from_api(item)
                    for item in report_custom_fields
                    if isinstance(item, dict)
                )
                if field is not None
            ]
            if isinstance(report_custom_fields, list)
            else None,
            doc_type=payload.get("doc_type"),
            raw=dict(data),
        )


@dataclass(slots=True)
class FindingTemplateInput:
    template_name: str | None = None
    fields: dict[str, TemplateField] | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "template_name": self.template_name,
                "fields": {key: field.to_api() for key, field in self.fields.items()}
                if self.fields is not None
                else None,
            }
        )


@dataclass(slots=True)
class FindingTemplate:
    template_id: str | None = None
    template_name: str | None = None
    tenant_id: int | str | None = None
    fields: dict[str, TemplateField] | None = None
    doc_type: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> FindingTemplate:
        payload = _nested_payload(data)
        fields = payload.get("fields")
        return cls(
            template_id=payload.get("doc_id") or payload.get("id"),
            template_name=payload.get("template_name") or payload.get("name"),
            tenant_id=payload.get("tenant_id"),
            fields={
                key: field
                for key, field in (
                    (key, TemplateField.from_api(value))
                    for key, value in fields.items()
                    if isinstance(value, dict)
                )
                if field is not None
            }
            if isinstance(fields, dict)
            else None,
            doc_type=payload.get("doc_type"),
            raw=dict(data),
        )


@dataclass(slots=True)
class ExportTemplate:
    template_id: str | None = None
    name: str | None = None
    file_id: str | None = None
    type: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, template_id: str, data: JsonDict) -> ExportTemplate:
        return cls(
            template_id=template_id,
            name=data.get("name"),
            file_id=data.get("id"),
            type=data.get("type"),
            raw=dict(data),
        )


@dataclass(slots=True)
class TemplateOperationResult:
    status: str | None = None
    message: str | None = None
    template_id: str | None = None
    name: str | None = None
    raw: JsonDict | None = None

    @property
    def ok(self) -> bool:
        return self.status == "success" or self.template_id is not None or self.name is not None

    @classmethod
    def from_api(cls, data: JsonDict) -> TemplateOperationResult:
        return cls(
            status=data.get("status"),
            message=data.get("message"),
            template_id=data.get("doc_id") or data.get("id"),
            name=data.get("name"),
            raw=dict(data),
        )


def _nested_payload(data: JsonDict) -> JsonDict:
    payload = data.get("data")
    return cast(JsonDict, payload) if isinstance(payload, dict) else data
