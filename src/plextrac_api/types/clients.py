from __future__ import annotations

from dataclasses import dataclass

from plextrac_api.types.assets import Asset
from plextrac_api.types.common import CustomField, JsonDict, UserRole, clean
from plextrac_api.types.findings import Finding


@dataclass(slots=True)
class ClientUserAssignment:
    username: str
    role: str
    classification_id: str | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "username": self.username,
                "role": self.role,
                "classificationId": self.classification_id,
            }
        )


@dataclass(slots=True)
class BulkClientUserAssignment:
    email: str
    role: str
    first_name: str | None = None
    last_name: str | None = None
    default_group: bool | None = None
    tenant_classification_level: str | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "default_group": self.default_group,
                "email": self.email,
                "name": clean({"first": self.first_name, "last": self.last_name}),
                "role": self.role,
                "tenantClassificationLevel": self.tenant_classification_level,
            }
        )


@dataclass(slots=True)
class ClientUser:
    username: str | None = None
    email: str | None = None
    role: str | None = None
    classification_id: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> ClientUser:
        name = data.get("name")
        return cls(
            username=data.get("username"),
            email=data.get("email") or data.get("username"),
            role=data.get("role"),
            classification_id=data.get("classificationId") or data.get("tenantClassificationLevel"),
            first_name=name.get("first") if isinstance(name, dict) else data.get("firstName"),
            last_name=name.get("last") if isinstance(name, dict) else data.get("lastName"),
            raw=dict(data),
        )


@dataclass(slots=True)
class ClientDraft:
    name: str
    tags: list[str] | None = None
    description: str | None = None
    point_of_contact: str | None = None
    point_of_contact_email: str | None = None
    custom_fields: list[CustomField] | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "name": self.name,
                "tags": self.tags,
                "description": self.description,
                "poc": self.point_of_contact,
                "poc_email": self.point_of_contact_email,
                "custom_field": [
                    clean({"label": field.label, "value": field.value})
                    for field in self.custom_fields or []
                ]
                if self.custom_fields is not None
                else None,
            }
        )


@dataclass(slots=True)
class ClientPatch:
    name: str | None = None
    tags: list[str] | None = None
    description: str | None = None
    point_of_contact: str | None = None
    point_of_contact_email: str | None = None
    custom_fields: list[CustomField] | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "name": self.name,
                "tags": self.tags,
                "description": self.description,
                "poc": self.point_of_contact,
                "poc_email": self.point_of_contact_email,
                "custom_field": [
                    clean({"label": field.label, "value": field.value})
                    for field in self.custom_fields or []
                ]
                if self.custom_fields is not None
                else None,
            }
        )


@dataclass(slots=True)
class Client:
    id: int | str | None = None
    name: str | None = None
    tenant_id: int | str | None = None
    classification_id: str | None = None
    description: str | None = None
    point_of_contact: str | None = None
    point_of_contact_email: str | None = None
    role: str | None = None
    tags: list[str] | None = None
    custom_fields: list[CustomField] | None = None
    users: dict[str, UserRole] | None = None
    doc_type: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> Client:
        custom_fields = data.get("custom_field")
        users = data.get("users")
        return cls(
            id=data.get("client_id") or data.get("id") or data.get("cuid"),
            name=data.get("name"),
            tenant_id=data.get("tenant_id"),
            classification_id=data.get("classificationId"),
            description=data.get("description"),
            point_of_contact=data.get("poc"),
            point_of_contact_email=data.get("poc_email"),
            role=data.get("role"),
            tags=data.get("tags") if isinstance(data.get("tags"), list) else None,
            custom_fields=[
                field
                for field in (CustomField.from_api(item) for item in custom_fields or [])
                if field is not None
            ]
            if isinstance(custom_fields, list)
            else None,
            users={
                email: role
                for email, role in (
                    (email, UserRole.from_api(value))
                    for email, value in users.items()
                    if isinstance(value, dict)
                )
                if role is not None
            }
            if isinstance(users, dict)
            else None,
            doc_type=data.get("doc_type"),
            raw=dict(data),
        )


@dataclass(slots=True)
class ClientPage:
    clients: list[Client]
    total_count: int | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict | list[JsonDict]) -> ClientPage:
        if isinstance(data, list):
            return cls(
                clients=[Client.from_api(item) for item in data if isinstance(item, dict)],
                raw={"data": data},
            )

        items = _first_list(data, ("clients", "data", "items", "results"))
        return cls(
            clients=[Client.from_api(item) for item in items if isinstance(item, dict)],
            total_count=_first_int(data, ("total", "totalCount", "count")),
            raw=dict(data),
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


@dataclass(slots=True)
class ClientFindingPage:
    findings: list[Finding]
    total_count: int | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict | list[JsonDict]) -> ClientFindingPage:
        if isinstance(data, list):
            return cls(
                findings=[Finding.from_api(item) for item in data if isinstance(item, dict)],
                raw={"data": data},
            )
        items = _first_list(data, ("findings", "data", "items", "results"))
        return cls(
            findings=[Finding.from_api(item) for item in items if isinstance(item, dict)],
            total_count=_first_int(data, ("total", "totalCount", "count")),
            raw=dict(data),
        )


@dataclass(slots=True)
class ClientAssetPage:
    assets: list[Asset]
    total_count: int | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict | list[JsonDict]) -> ClientAssetPage:
        if isinstance(data, list):
            return cls(
                assets=[Asset.from_api(item) for item in data if isinstance(item, dict)],
                raw={"data": data},
            )
        items = _first_list(data, ("assets", "data", "items", "results"))
        return cls(
            assets=[Asset.from_api(item) for item in items if isinstance(item, dict)],
            total_count=_first_int(data, ("total", "totalCount", "count")),
            raw=dict(data),
        )
