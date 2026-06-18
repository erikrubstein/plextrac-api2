from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from plextrac_api.types.common import JsonDict


class EmailTemplateKind(StrEnum):
    FORGOTTEN_PASSWORD = "FORGOTTEN_PASSWORD"


@dataclass(slots=True)
class EmailTemplate:
    template: EmailTemplateKind | None = None
    subject: str | None = None
    body: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> EmailTemplate:
        template_value = (
            data.get("template")
            or data.get("templateKey")
            or data.get("type")
            or data.get("name")
        )
        return cls(
            template=_email_template_kind(template_value),
            subject=data.get("subject"),
            body=data.get("body"),
            raw=dict(data),
        )


def _email_template_kind(value: object) -> EmailTemplateKind | None:
    if isinstance(value, EmailTemplateKind):
        return value
    if isinstance(value, str):
        try:
            return EmailTemplateKind(value)
        except ValueError:
            return None
    return None
