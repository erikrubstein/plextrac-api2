from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from plextrac_api.types.common import AuthenticationProviderName, JsonDict, clean
from plextrac_api.types.findings import Finding, FindingFilter, FindingPagination, FindingSort


class DefaultUserRole(StrEnum):
    ADMIN = "ADMIN"
    STANDARD_USER = "STD_USER"
    ANALYST = "ANALYST"


class UserSortField(StrEnum):
    FIRST_NAME = "firstName"
    LAST_NAME = "lastName"
    EMAIL = "email"


class UserSortOrder(StrEnum):
    ASCENDING = "ASCEND"
    DESCENDING = "DESEND"


class UserNotificationReadFilter(StrEnum):
    UNREAD = "unread"
    READ = "read"
    ALL = "any"


@dataclass(slots=True)
class UserName:
    first: str | None = None
    last: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict | None) -> UserName | None:
        if not isinstance(data, dict):
            return None
        return cls(
            first=data.get("first") or data.get("firstName"),
            last=data.get("last") or data.get("lastName"),
            raw=dict(data),
        )

    def to_api(self) -> JsonDict:
        return clean({"first": self.first, "last": self.last})


@dataclass(slots=True)
class TenantUserInput:
    email: str
    role: DefaultUserRole | str
    first_name: str | None = None
    last_name: str | None = None
    default_group: bool | None = None
    tenant_classification_level: str | None = None

    def to_api(self) -> JsonDict:
        role = self.role.value if isinstance(self.role, DefaultUserRole) else self.role
        return clean(
            {
                "email": self.email,
                "role": role,
                "name": clean({"first": self.first_name, "last": self.last_name}),
                "default_group": self.default_group,
                "tenantClassificationLevel": self.tenant_classification_level,
            }
        )


@dataclass(slots=True)
class CurrentUserUpdate:
    first_name: str | None = None
    last_name: str | None = None
    authentication_provider: AuthenticationProviderName | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "name": clean({"first": self.first_name, "last": self.last_name}),
                "authenticationProvider": self.authentication_provider.value
                if self.authentication_provider is not None
                else None,
            }
        )


@dataclass(slots=True)
class AuthenticatedUser:
    user_id: int | str | None = None
    user_cuid: str | None = None
    email: str | None = None
    username: str | None = None
    name: UserName | None = None
    tenant_id: int | str | None = None
    tenant_cuid: str | None = None
    tenant_name: str | None = None
    role: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> AuthenticatedUser:
        return cls(
            user_id=_first_present(data, ("user_id", "userId", "id")),
            user_cuid=_first_present(data, ("cuid", "userCuid")),
            email=data.get("email"),
            username=data.get("username"),
            name=UserName.from_api(data.get("name")),
            tenant_id=_first_present(data, ("tenant_id", "tenantId")),
            tenant_cuid=_first_present(data, ("tenantCuid",)),
            tenant_name=data.get("tenantName"),
            role=data.get("role"),
            raw=dict(data),
        )


@dataclass(slots=True)
class TenantUser:
    user_id: int | str | None = None
    email: str | None = None
    username: str | None = None
    name: UserName | None = None
    role: str | None = None
    disabled: bool | None = None
    locked: bool | None = None
    last_login: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> TenantUser:
        return cls(
            user_id=_first_present(data, ("user_id", "userId", "id")),
            email=data.get("email") or data.get("username"),
            username=data.get("username"),
            name=UserName.from_api(data.get("name"))
            or UserName(first=data.get("firstName"), last=data.get("lastName")),
            role=data.get("role"),
            disabled=data.get("disabled"),
            locked=data.get("locked"),
            last_login=data.get("lastLogin") or data.get("last_login"),
            raw=dict(data),
        )


@dataclass(slots=True)
class TenantUserPage:
    users: list[TenantUser]
    total_count: int | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> TenantUserPage:
        users = _first_present(data, ("data", "users", "items"))
        return cls(
            users=[TenantUser.from_api(item) for item in users if isinstance(item, dict)]
            if isinstance(users, list)
            else [],
            total_count=_first_present(data, ("total", "totalCount")),
            raw=dict(data),
        )


@dataclass(slots=True)
class UserNotification:
    notification_id: int | str | None = None
    message: str | None = None
    read: bool | None = None
    created_at: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> UserNotification:
        return cls(
            notification_id=_first_present(data, ("id", "notificationId")),
            message=data.get("message"),
            read=data.get("read"),
            created_at=data.get("createdAt") or data.get("created_at"),
            raw=dict(data),
        )


@dataclass(slots=True)
class UserFindingSearch:
    filters: list[FindingFilter] | None = None
    pagination: FindingPagination | None = None
    sort: list[FindingSort] | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "filters": [item.to_api() for item in self.filters]
                if self.filters is not None
                else None,
                "pagination": self.pagination.to_api()
                if self.pagination is not None
                else None,
                "sort": [item.to_api() for item in self.sort] if self.sort is not None else None,
            }
        )


@dataclass(slots=True)
class UserFindingSearchResult:
    findings: list[Finding]
    total_count: int | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> UserFindingSearchResult:
        findings = _first_present(data, ("data", "findings", "items"))
        return cls(
            findings=[Finding.from_api(item) for item in findings if isinstance(item, dict)]
            if isinstance(findings, list)
            else [],
            total_count=_first_present(data, ("total", "totalCount")),
            raw=dict(data),
        )


def _first_present(data: JsonDict, keys: tuple[str, ...]) -> object:
    for key in keys:
        if key in data:
            return data[key]
    return None
