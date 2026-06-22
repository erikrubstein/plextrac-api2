from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing import Any

JsonDict = dict[str, Any]


class SortOrder(StrEnum):
    ASCENDING = "ASC"
    DESCENDING = "DESC"


class AuthenticationProviderName(StrEnum):
    PLEXTRAC = "plextrac"
    OKTA = "okta"
    GOOGLE = "google"
    AZURE = "azure"
    OPENID_CONNECT = "openid_connect"


def clean(data: JsonDict) -> JsonDict:
    return {key: value for key, value in data.items() if value is not None}


@dataclass(slots=True)
class Pagination:
    offset: int = 0
    limit: int = 25

    def to_api(self) -> JsonDict:
        return {"offset": self.offset, "limit": self.limit}


@dataclass(slots=True)
class Sort:
    by: str
    order: SortOrder = SortOrder.ASCENDING

    def to_api(self) -> JsonDict:
        return {"by": self.by, "order": self.order.value}


@dataclass(slots=True)
class Filter:
    by: str
    value: str | int | bool | list[str] | list[int]

    def to_api(self) -> JsonDict:
        return {"by": self.by, "value": self.value}


@dataclass(slots=True)
class CustomField:
    label: str | None = None
    value: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict | None) -> CustomField | None:
        if not data:
            return None
        return cls(label=data.get("label"), value=data.get("value"), raw=dict(data))

    def to_api(self) -> JsonDict:
        return clean({"label": self.label, "value": self.value})


@dataclass(slots=True)
class UserRole:
    role: str | None = None
    classification_id: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict | None) -> UserRole | None:
        if not data:
            return None
        return cls(
            role=data.get("role"),
            classification_id=data.get("classificationId"),
            raw=dict(data),
        )


@dataclass(slots=True)
class Port:
    number: str | None = None
    service: str | None = None
    protocol: str | None = None
    version: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict | None) -> Port | None:
        if not data:
            return None
        return cls(
            number=data.get("number"),
            service=data.get("service"),
            protocol=data.get("protocol"),
            version=data.get("version"),
            raw=dict(data),
        )

    def to_api(self) -> JsonDict:
        return clean(
            {
                "number": self.number,
                "service": self.service,
                "protocol": self.protocol,
                "version": self.version,
            }
        )


@dataclass(slots=True)
class VulnerableParameter:
    id: str | None = None
    text: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict | None) -> VulnerableParameter | None:
        if not data:
            return None
        return cls(id=data.get("id"), text=data.get("text"), raw=dict(data))

    def to_api(self) -> JsonDict:
        return clean({"id": self.id, "text": self.text})


@dataclass(slots=True)
class ObjectReference:
    id: str | None = None
    name: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict | None) -> ObjectReference | None:
        if not data:
            return None
        return cls(
            id=data.get("id") or data.get("cuid"),
            name=data.get("name") or data.get("asset") or data.get("title"),
            raw=dict(data),
        )

    def to_api(self) -> JsonDict:
        return clean({"id": self.id, "name": self.name})


@dataclass(slots=True)
class OperationResult:
    status: str | None = None
    message: str | None = None
    raw: JsonDict | None = None

    @property
    def ok(self) -> bool:
        if self.raw:
            for key in ("ok", "success", "created", "updated", "deleted"):
                if self.raw.get(key) is True:
                    return True
        return _is_success_text(self.status) or _is_success_text(self.message)

    @classmethod
    def from_api(cls, data: JsonDict | list[JsonDict] | None) -> OperationResult:
        if isinstance(data, dict):
            status = data.get("status") or data.get("result")
            message = data.get("message") or data.get("detail")
            return cls(
                status=status or ("success" if "data" in data and message is None else None),
                message=message,
                raw=dict(data),
            )
        return cls(status="success", raw={"ok": True, "data": data})


def _is_success_text(value: object) -> bool:
    if not isinstance(value, str):
        return False
    normalized = value.lower().strip(" .!")
    return normalized in {
        "ok",
        "success",
        "successful",
        "deleted",
        "created",
        "updated",
    }
