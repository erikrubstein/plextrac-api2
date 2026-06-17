from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, IntEnum

from plextrac_api.types.common import CustomField, JsonDict, SortOrder, UserRole, clean
from plextrac_api.types.findings import Finding, FindingSeverity, FindingStatus, FindingVisibility


class ClientPageLimit(IntEnum):
    FIVE = 5
    TWENTY_FIVE = 25
    FIFTY = 50
    ONE_HUNDRED = 100


class ClientSortField(str, Enum):
    NAME = "name"
    ASSET = "asset"


class ClientFilterField(str, Enum):
    NAME = "name"
    ASSET = "asset"
    TAGS = "tags"


class ClientFindingSortField(str, Enum):
    ASSIGNED_TO = "assignedTo"
    DATE_FROM = "dateFrom"
    DATE_TO = "dateTo"
    REPORT_ID = "reportId"
    SEVERITY = "severity"
    STATUS = "status"
    SUBSTATUS = "subStatus"
    VISIBILITY = "visibility"


class ClientFindingFilterField(str, Enum):
    ASSIGNED_TO = "assignedTo"
    COMMON_IDENTIFIERS = "commonIdentifiers"
    DATE_FROM = "dateFrom"
    DATE_TO = "dateTo"
    REPORT_ID = "reportId"
    SEARCH_TERM = "searchTerm"
    SEVERITY = "severity"
    STATUS = "status"
    SUBSTATUS = "subStatus"
    TAGS = "tags"
    VISIBILITY = "visibility"


ClientFindingFilterValue = (
    str
    | int
    | FindingSeverity
    | FindingStatus
    | FindingVisibility
    | list[str]
    | list[FindingSeverity]
    | list[FindingStatus]
    | list[FindingVisibility]
)


@dataclass(slots=True)
class ClientPagination:
    offset: int = 0
    limit: ClientPageLimit = ClientPageLimit.TWENTY_FIVE

    def to_api(self) -> JsonDict:
        return {"offset": self.offset, "limit": int(self.limit)}


@dataclass(slots=True)
class ClientSort:
    by: ClientSortField
    order: SortOrder = SortOrder.ASCENDING

    def to_api(self) -> JsonDict:
        return {"by": self.by.value, "order": self.order.value}


@dataclass(slots=True)
class ClientFilter:
    by: ClientFilterField
    value: str | list[str]

    def to_api(self) -> JsonDict:
        return {"by": self.by.value, "value": self.value}


@dataclass(slots=True)
class ClientFindingSort:
    by: ClientFindingSortField
    order: SortOrder = SortOrder.ASCENDING

    def to_api(self) -> JsonDict:
        return {"by": self.by.value, "order": self.order.value}


@dataclass(slots=True)
class ClientFindingFilter:
    by: ClientFindingFilterField
    value: ClientFindingFilterValue

    def to_api(self) -> JsonDict:
        return {"by": self.by.value, "value": _api_value(self.value)}


@dataclass(slots=True)
class ClientUserAssignment:
    role: str
    username: str | None = None
    email: str | None = None
    classification_id: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    default_group: bool | None = None
    tenant_classification_level: str | None = None

    def to_assign_api(self) -> JsonDict:
        return clean(
            {
                "username": self.username or self.email,
                "role": self.role,
                "classificationId": self.classification_id,
            }
        )

    def to_bulk_api(self) -> JsonDict:
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
class ClientInput:
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
                "custom_field": [field.to_api() for field in self.custom_fields or []]
                if self.custom_fields is not None
                else None,
            }
        )


@dataclass(slots=True)
class ClientCreateResult:
    client_id: int | str | None = None
    created: bool | None = None
    status: str | None = None
    message: str | None = None
    raw: JsonDict | None = None

    @property
    def ok(self) -> bool:
        return (
            self.created is True
            or _is_success_text(self.status)
            or _is_success_text(self.message)
        )

    @classmethod
    def from_api(cls, data: JsonDict) -> ClientCreateResult:
        created = data.get("created")
        return cls(
            client_id=data.get("client_id"),
            created=created if isinstance(created, bool) else None,
            status=data.get("status") or data.get("result"),
            message=data.get("message") or data.get("detail"),
            raw=dict(data),
        )


@dataclass(slots=True)
class Client:
    client_id: int | str | None = None
    cuid: str | None = None
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
            client_id=data.get("client_id"),
            cuid=data.get("cuid"),
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


def _api_value(value: object) -> object:
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, list):
        return [_api_value(item) for item in value]
    return value


def _is_success_text(value: object) -> bool:
    if not isinstance(value, str):
        return False
    return value.lower() in {
        "ok",
        "success",
        "successful",
        "created",
    }


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
