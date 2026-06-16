from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Literal

JsonDict = dict[str, Any]
SortOrder = Literal["ASC", "DESC"]


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
    order: SortOrder = "ASC"

    def to_api(self) -> JsonDict:
        return {"by": self.by, "order": self.order}


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


@dataclass(slots=True)
class OperationResult:
    status: str | None = None
    message: str | None = None
    id: int | str | None = None
    raw: JsonDict | None = None

    @property
    def ok(self) -> bool:
        if self.raw and self.raw.get("ok") is True:
            return True
        if self.status is None:
            return False
        return self.status.lower() in {
            "ok",
            "success",
            "successful",
            "deleted",
            "created",
            "updated",
        }

    @classmethod
    def from_api(cls, data: JsonDict | list[JsonDict] | None) -> OperationResult:
        if isinstance(data, dict):
            return cls(
                status=data.get("status") or data.get("result"),
                message=data.get("message") or data.get("detail"),
                id=(
                    data.get("id")
                    or data.get("client_id")
                    or data.get("report_id")
                    or data.get("cuid")
                ),
                raw=dict(data),
            )
        return cls(raw={"data": data})
