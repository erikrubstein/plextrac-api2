from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from plextrac_api.types.common import JsonDict, clean
from plextrac_api.types.findings import FindingSeverity


class ParserActionType(StrEnum):
    DEFAULT = "DEFAULT"
    LINK = "LINK"
    IGNORE = "IGNORE"


class ParserActionSearchType(StrEnum):
    DEFAULT = "DEFAULT"
    LINK = "LINK"
    IGNORE = "IGNORE"


class ParserPluginSource(StrEnum):
    ACUNETIX = "acunetix"
    BURP = "burp"
    BURP_HTML = "burphtml"
    CHECKMARX = "checkmarx"
    CORE_IMPACT = "coreimpact"
    CUSTOM = "custom"
    HCL_APPSCAN = "hclappscan"
    HORIZON = "horizon"
    INVICTI = "invicti"
    NESSUS = "nessus"
    NETSPARKER = "netsparker"
    NEXPOSE = "nexpose"
    NIPPER = "nipper"
    NMAP = "nmap"
    NODEWARE = "nodeware"
    NODEZERO = "nodezero"
    OPENVAS = "openvas"
    OWASP_ZAP = "owaspzap"
    PENTERA = "pentera"
    QUALYS = "qualys"
    RAPIDFIRE = "rapidfire"
    SCYTHE = "scythe"
    VERACODE = "veracode"


@dataclass(slots=True)
class Parser:
    name: str | None = None
    parser_id: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> Parser:
        return cls(
            name=data.get("name") or data.get("parserName"),
            parser_id=data.get("source") or data.get("parserId"),
            raw=dict(data),
        )


@dataclass(slots=True)
class ParserActionInput:
    action_id: int | str | None = None
    severity: FindingSeverity | None = None
    title: str | None = None
    action: ParserActionType = ParserActionType.DEFAULT
    link_id: int | str | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "id": self.action_id,
                "severity": self.severity.value if self.severity is not None else None,
                "title": self.title,
                "action": self.action.value,
                "link_id": self.link_id,
            }
        )


@dataclass(slots=True)
class ParserAction:
    action_id: int | str | None = None
    severity: FindingSeverity | None = None
    title: str | None = None
    action: ParserActionType | None = None
    link_id: int | str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> ParserAction:
        return cls(
            action_id=data.get("id") or data.get("actionId"),
            severity=_severity(data.get("severity")),
            title=data.get("title"),
            action=_action(data.get("action")),
            link_id=data.get("link_id") or data.get("linkId"),
            raw=dict(data),
        )


@dataclass(slots=True)
class ParserPluginImportResult:
    status: str | None = None
    message: str | None = None
    imported_count: int | None = None
    raw: JsonDict | None = None

    @property
    def ok(self) -> bool:
        return self.status == "success" or self.imported_count is not None

    @classmethod
    def from_api(cls, data: JsonDict) -> ParserPluginImportResult:
        return cls(
            status=data.get("status"),
            message=data.get("message"),
            imported_count=data.get("imported") or data.get("importedCount"),
            raw=dict(data),
        )


def _severity(value: object) -> FindingSeverity | None:
    if isinstance(value, FindingSeverity):
        return value
    if isinstance(value, str):
        try:
            return FindingSeverity(value)
        except ValueError:
            return None
    return None


def _action(value: object) -> ParserActionType | None:
    if isinstance(value, ParserActionType):
        return value
    if isinstance(value, str):
        try:
            return ParserActionType(value)
        except ValueError:
            return None
    return None
