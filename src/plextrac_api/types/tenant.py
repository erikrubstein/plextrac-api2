from __future__ import annotations

from dataclasses import dataclass

from plextrac_api.types.common import JsonDict
from plextrac_api.types.findings import FindingVisibility


@dataclass(slots=True)
class TenantPointOfContact:
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict | None) -> TenantPointOfContact | None:
        if not data:
            return None
        return cls(
            first_name=data.get("first"),
            last_name=data.get("last"),
            email=data.get("email"),
            raw=dict(data),
        )


@dataclass(slots=True)
class TenantSettings:
    visibility: FindingVisibility | None = None
    rapid_templating: bool | None = None
    sender_email_address: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict | None) -> TenantSettings | None:
        if not data:
            return None
        return cls(
            visibility=_visibility(data.get("visibility")),
            rapid_templating=data.get("rapidTemplating"),
            sender_email_address=data.get("senderEmailAddress"),
            raw=dict(data),
        )

@dataclass(slots=True)
class Tenant:
    tenant_id: int | str | None = None
    cuid: str | None = None
    name: str | None = None
    address: str | None = None
    point_of_contact: TenantPointOfContact | None = None
    settings: TenantSettings | None = None
    icon: str | None = None
    doc_type: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> Tenant:
        return cls(
            tenant_id=data.get("tenant_id") or data.get("tenantId"),
            cuid=data.get("cuid"),
            name=data.get("name"),
            address=data.get("address"),
            point_of_contact=TenantPointOfContact.from_api(data.get("poc")),
            settings=TenantSettings.from_api(data.get("settings")),
            icon=data.get("icon"),
            doc_type=data.get("doc_type"),
            raw=dict(data),
        )


@dataclass(slots=True)
class NotificationSettings:
    reminder_days: int | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> NotificationSettings:
        return cls(reminder_days=data.get("reminderDays"), raw=dict(data))


@dataclass(slots=True)
class TenantRiskCounts:
    open: int | None = None
    closed: int | None = None
    in_process: int | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict | None) -> TenantRiskCounts | None:
        if not data:
            return None
        return cls(
            open=data.get("open"),
            closed=data.get("closed"),
            in_process=data.get("in_process"),
            raw=dict(data),
        )


@dataclass(slots=True)
class TenantAnalytics:
    status: str | None = None
    message: str | None = None
    tenant_risk: dict[str, TenantRiskCounts] | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> TenantAnalytics:
        risk = data.get("tenant_risk")
        return cls(
            status=data.get("status"),
            message=data.get("message"),
            tenant_risk={
                key: parsed
                for key, parsed in (
                    (key, TenantRiskCounts.from_api(value))
                    for key, value in risk.items()
                    if isinstance(value, dict)
                )
                if parsed is not None
            }
            if isinstance(risk, dict)
            else None,
            raw=dict(data),
        )


@dataclass(slots=True)
class RootInfo:
    text: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> RootInfo:
        return cls(text=data.get("text"), raw=dict(data))


def _visibility(value: object) -> FindingVisibility | None:
    if isinstance(value, FindingVisibility):
        return value
    if isinstance(value, str):
        try:
            return FindingVisibility(value)
        except ValueError:
            return None
    return None
