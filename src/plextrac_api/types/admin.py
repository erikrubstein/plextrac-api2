from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from plextrac_api.types.assets import AssetCriticality
from plextrac_api.types.common import AuthenticationProviderName, JsonDict, clean
from plextrac_api.types.findings import FindingSeverity


class TenantTagScope(StrEnum):
    TENANT = "tenant"


class AuditLogEventType(StrEnum):
    LOGIN_SUCCESS = "LoginSuccess"
    LOGIN_FAIL = "LoginFail"
    LOGIN_LOCKOUT = "LoginLockout"
    USER_UNLOCKED = "UserUnlocked"
    USER_CREATED = "UserCreated"
    USER_DELETED = "UserDeleted"
    USER_ENABLED = "UserEnabled"
    USER_DISABLED = "UserDisabled"
    PASSWORD_CHANGED = "PasswordChanged"
    PASSWORD_CHANGED_BY_OTHER = "PasswordChangedByOther"
    TENANT_ROLE_CREATED = "TenantRoleCreated"
    TENANT_ROLE_DELETED = "TenantRoleDeleted"
    TENANT_ROLE_UPDATED = "TenantRoleUpdated"
    TENANT_ROLE_ASSIGNED = "TenantRoleAssigned"
    TENANT_ROLE_REMOVED = "TenantRoleRemoved"
    USER_CLIENT_ROLE_ASSIGNED = "UserClientRoleAssigned"
    USER_CLIENT_ROLE_REMOVED = "UserClientRoleRemoved"
    ADDED_TO_DEFAULT_GROUP = "AddedToDefaultGroup"
    CLIENT_LICENSE_UPDATED = "ClientLicenseUpdated"
    USER_LICENSE_UPDATED = "UserLicenseUpdated"


@dataclass(slots=True)
class AuthenticationProvider:
    provider: AuthenticationProviderName | None = None
    enabled: bool | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: object) -> AuthenticationProvider:
        if isinstance(data, str):
            return cls(provider=_authentication_provider(data), raw={"provider": data})
        if isinstance(data, dict):
            return cls(
                provider=_authentication_provider(data.get("provider") or data.get("name")),
                enabled=data.get("enabled"),
                raw=dict(data),
            )
        return cls(raw={"data": data})


@dataclass(slots=True)
class AuthenticationProviderConfiguration:
    enabled: bool | None = None
    provider: AuthenticationProviderName | None = None
    uri: str | None = None
    provider_client_id: str | None = None
    auth_server_id: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> AuthenticationProviderConfiguration:
        return cls(
            enabled=data.get("enabled"),
            provider=_authentication_provider(data.get("provider")),
            uri=data.get("uri"),
            provider_client_id=data.get("providerClientId"),
            auth_server_id=data.get("authServerId"),
            raw=dict(data),
        )


@dataclass(slots=True)
class SamlConfiguration:
    enabled: bool
    provider_name: str
    issuer: str
    certificate: str
    idp_sso_url: str
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> SamlConfiguration:
        return cls(
            enabled=bool(data.get("enabled")),
            provider_name=str(data.get("providerName") or data.get("provider_name") or ""),
            issuer=str(data.get("issuer") or ""),
            certificate=str(data.get("cert") or data.get("certificate") or ""),
            idp_sso_url=str(data.get("idpSSOUrl") or data.get("idp_sso_url") or ""),
            raw=dict(data),
        )

    def to_api(self) -> JsonDict:
        return {
            "enabled": self.enabled,
            "providerName": self.provider_name,
            "issuer": self.issuer,
            "cert": self.certificate,
            "idpSSOUrl": self.idp_sso_url,
        }


@dataclass(slots=True)
class UserPermissions:
    permissions: list[str]
    clients: JsonDict | None = None
    doc_type: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> UserPermissions:
        permissions = data.get("permissions")
        parsed_permissions = (
            [str(item) for item in permissions] if isinstance(permissions, list) else []
        )
        return cls(
            permissions=parsed_permissions,
            clients=data.get("clients") if isinstance(data.get("clients"), dict) else None,
            doc_type=data.get("doc_type"),
            raw=dict(data),
        )


@dataclass(slots=True)
class SecurityRoleUser:
    user_id: int | str | None = None
    cuid: str | None = None
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    full_name: str | None = None
    roles: list[str] | None = None
    disabled: bool | None = None
    can_remove_user_from_role: bool | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> SecurityRoleUser:
        roles = data.get("roles")
        return cls(
            user_id=data.get("user_id") or data.get("userId"),
            cuid=data.get("cuid"),
            email=data.get("email"),
            first_name=data.get("first") or _name_part(data, "first"),
            last_name=data.get("last") or _name_part(data, "last"),
            full_name=data.get("fullName"),
            roles=[str(role) for role in roles] if isinstance(roles, list) else None,
            disabled=data.get("disabled"),
            can_remove_user_from_role=data.get("canRemoveUserFromRole"),
            raw=dict(data),
        )


@dataclass(slots=True)
class AvailableSecurityRole:
    name: str | None = None
    cuid: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: object) -> AvailableSecurityRole:
        if isinstance(data, list):
            return cls(
                name=str(data[0]) if len(data) > 0 else None,
                cuid=str(data[1]) if len(data) > 1 else None,
                raw={"data": data},
            )
        if isinstance(data, dict):
            return cls(
                name=data.get("name") or data.get("title"),
                cuid=data.get("cuid") or data.get("id"),
                raw=dict(data),
            )
        return cls(raw={"data": data})


@dataclass(slots=True)
class SecurityRolePermission:
    key: str
    available_file_types: list[str] | None = None
    blocks: list[str] | None = None
    enabled: bool | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> SecurityRolePermission:
        return cls(
            key=str(data.get("key") or ""),
            available_file_types=_string_list(data.get("availableFileTypes")),
            blocks=_string_list(data.get("blocks")),
            enabled=data.get("enabled"),
            raw=dict(data),
        )

    def to_api(self) -> JsonDict:
        return clean(
            {
                "key": self.key,
                "availableFileTypes": self.available_file_types,
                "blocks": self.blocks,
                "enabled": self.enabled,
            }
        )


@dataclass(slots=True)
class SecurityRolePermissionSection:
    key: str
    permissions: list[SecurityRolePermission]
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> SecurityRolePermissionSection:
        permissions = data.get("permissions")
        return cls(
            key=str(data.get("key") or ""),
            permissions=[
                SecurityRolePermission.from_api(item)
                for item in permissions
                if isinstance(item, dict)
            ]
            if isinstance(permissions, list)
            else [],
            raw=dict(data),
        )

    def to_api(self) -> JsonDict:
        return {
            "key": self.key,
            "permissions": [permission.to_api() for permission in self.permissions],
        }


@dataclass(slots=True)
class SecurityRolePermissionGroup:
    key: str
    sections: list[SecurityRolePermissionSection]
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> SecurityRolePermissionGroup:
        sections = data.get("sections")
        return cls(
            key=str(data.get("key") or ""),
            sections=[
                SecurityRolePermissionSection.from_api(item)
                for item in sections
                if isinstance(item, dict)
            ]
            if isinstance(sections, list)
            else [],
            raw=dict(data),
        )

    def to_api(self) -> JsonDict:
        return {
            "key": self.key,
            "sections": [section.to_api() for section in self.sections],
        }


@dataclass(slots=True)
class SecurityRole:
    role_id: int | str | None = None
    key: str | None = None
    title: str | None = None
    description: str | None = None
    enabled: bool | None = None
    editable: bool | None = None
    can_disable: bool | None = None
    permissions: list[str] | None = None
    permission_configuration: list[SecurityRolePermissionGroup] | None = None
    total_permissions: int | None = None
    user_count: int | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> SecurityRole:
        permission_configuration = data.get("permissionConfiguration")
        return cls(
            role_id=data.get("id") or data.get("roleId"),
            key=data.get("key"),
            title=data.get("title") or data.get("name"),
            description=data.get("description"),
            enabled=data.get("enabled"),
            editable=data.get("editable"),
            can_disable=data.get("canDisable"),
            permissions=_string_list(data.get("permissions")),
            permission_configuration=[
                SecurityRolePermissionGroup.from_api(item)
                for item in permission_configuration
                if isinstance(item, dict)
            ]
            if isinstance(permission_configuration, list)
            else None,
            total_permissions=data.get("totalPermissions"),
            user_count=data.get("userCount"),
            raw=dict(data),
        )


@dataclass(slots=True)
class SecurityRoleResult:
    status: str | None = None
    role_id: int | str | None = None
    raw: JsonDict | None = None

    @property
    def ok(self) -> bool:
        return self.status == "success" or self.role_id is not None

    @classmethod
    def from_api(cls, data: JsonDict) -> SecurityRoleResult:
        return cls(
            status=data.get("status"),
            role_id=data.get("data") or data.get("id") or data.get("roleId"),
            raw=dict(data),
        )


@dataclass(slots=True)
class RoleNameAvailability:
    available: bool | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> RoleNameAvailability:
        return cls(available=data.get("available"), raw=dict(data))


@dataclass(slots=True)
class TenantTag:
    tag_id: str | None = None
    name: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> TenantTag:
        return cls(tag_id=data.get("id"), name=data.get("name"), raw=dict(data))


@dataclass(slots=True)
class TenantTagPage:
    tags: list[TenantTag]
    total_count: int | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> TenantTagPage:
        count = data.get("count")
        total_count = None
        if isinstance(count, dict):
            total_count = count.get("totalDocs")
        elif isinstance(count, list) and count and isinstance(count[0], dict):
            total_count = count[0].get("totalDocs")
        tags = data.get("tags")
        return cls(
            tags=[TenantTag.from_api(item) for item in tags if isinstance(item, dict)]
            if isinstance(tags, list)
            else [],
            total_count=total_count,
            raw=dict(data),
        )


@dataclass(slots=True)
class SLABenchmarkNotificationSettings:
    hours_before_expiration_notify: int | None = None
    recipients: list[str] | None = None
    send_daily_notification_to_assigned_user: bool | None = None
    send_exceeded_notification_to_assigned_user: bool | None = None
    send_nearing_notification_to_assigned_user: bool | None = None
    send_daily_notification_to_recipients: bool | None = None
    send_exceeded_notification_to_recipients: bool | None = None
    send_nearing_notification_to_recipients: bool | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict | None) -> SLABenchmarkNotificationSettings | None:
        if not isinstance(data, dict):
            return None
        return cls(
            hours_before_expiration_notify=data.get("hoursBeforeExpirationNotify"),
            recipients=_string_list(data.get("recipients")),
            send_daily_notification_to_assigned_user=data.get(
                "sendDailyNotificationToAssignedUser"
            ),
            send_exceeded_notification_to_assigned_user=data.get(
                "sendExceededNotificationToAssignedUser"
            ),
            send_nearing_notification_to_assigned_user=data.get(
                "sendNearingNotificationToAssignedUser"
            ),
            send_daily_notification_to_recipients=data.get("sendDailyNotificationToRecipients"),
            send_exceeded_notification_to_recipients=data.get(
                "sendExceededNotificationToRecipients"
            ),
            send_nearing_notification_to_recipients=data.get(
                "sendNearingNotificationToRecipients"
            ),
            raw=dict(data),
        )

    def to_api(self) -> JsonDict:
        return clean(
            {
                "hoursBeforeExpirationNotify": self.hours_before_expiration_notify,
                "recipients": self.recipients,
                "sendDailyNotificationToAssignedUser": (
                    self.send_daily_notification_to_assigned_user
                ),
                "sendExceededNotificationToAssignedUser": (
                    self.send_exceeded_notification_to_assigned_user
                ),
                "sendNearingNotificationToAssignedUser": (
                    self.send_nearing_notification_to_assigned_user
                ),
                "sendDailyNotificationToRecipients": self.send_daily_notification_to_recipients,
                "sendExceededNotificationToRecipients": (
                    self.send_exceeded_notification_to_recipients
                ),
                "sendNearingNotificationToRecipients": self.send_nearing_notification_to_recipients,
            }
        )


@dataclass(slots=True)
class SLABenchmark:
    name: str
    days_to_close: int
    finding_severity: list[FindingSeverity]
    enabled: bool
    benchmark_id: int | str | None = None
    finding_tags: list[str] | None = None
    asset_criticality: list[AssetCriticality] | None = None
    asset_tags: list[str] | None = None
    notification_settings: SLABenchmarkNotificationSettings | None = None
    tenant_id: int | str | None = None
    doc_type: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> SLABenchmark:
        return cls(
            benchmark_id=data.get("id") or data.get("slaBenchmarkId"),
            name=str(data.get("name") or ""),
            days_to_close=int(data.get("daysToClose") or 0),
            finding_severity=[
                parsed
                for parsed in (_finding_severity(item) for item in data.get("findingSeverity", []))
                if parsed is not None
            ],
            finding_tags=_string_list(data.get("findingTags")),
            asset_criticality=[
                parsed
                for parsed in (
                    _asset_criticality(item) for item in data.get("assetCriticality", [])
                )
                if parsed is not None
            ],
            asset_tags=_string_list(data.get("assetTags")),
            enabled=bool(data.get("enabled")),
            notification_settings=SLABenchmarkNotificationSettings.from_api(
                data.get("notificationSettings")
            ),
            tenant_id=data.get("tenantId") or data.get("tenant_id"),
            doc_type=data.get("doc_type"),
            raw=dict(data),
        )

    def to_api(self) -> JsonDict:
        return clean(
            {
                "name": self.name,
                "daysToClose": self.days_to_close,
                "findingSeverity": [severity.value for severity in self.finding_severity],
                "findingTags": self.finding_tags,
                "assetCriticality": [
                    criticality.value for criticality in self.asset_criticality
                ]
                if self.asset_criticality is not None
                else None,
                "assetTags": self.asset_tags,
                "enabled": self.enabled,
                "notificationSettings": self.notification_settings.to_api()
                if self.notification_settings is not None
                else None,
            }
        )


@dataclass(slots=True)
class SLABenchmarkResult:
    status: str | None = None
    benchmark_id: int | str | None = None
    raw: JsonDict | None = None

    @property
    def ok(self) -> bool:
        return self.status == "success" or self.benchmark_id is not None

    @classmethod
    def from_api(cls, data: JsonDict) -> SLABenchmarkResult:
        return cls(
            status=data.get("status"),
            benchmark_id=data.get("data") or data.get("id") or data.get("slaBenchmarkId"),
            raw=dict(data),
        )


@dataclass(slots=True)
class AuditLogEntry:
    cuid: str | None = None
    user_info: str | None = None
    message: str | None = None
    event_type: AuditLogEventType | None = None
    timestamp: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> AuditLogEntry:
        return cls(
            cuid=data.get("cuid"),
            user_info=data.get("user_info") or data.get("userInfo"),
            message=data.get("message"),
            event_type=_audit_log_event_type(data.get("event_type") or data.get("eventType")),
            timestamp=data.get("timestamp"),
            raw=dict(data),
        )


def _name_part(data: JsonDict, part: str) -> str | None:
    name = data.get("name")
    if isinstance(name, dict):
        value = name.get(part)
        return str(value) if value is not None else None
    return None


def _string_list(value: object) -> list[str] | None:
    if isinstance(value, list):
        return [str(item) for item in value]
    return None


def _authentication_provider(value: object) -> AuthenticationProviderName | None:
    if isinstance(value, AuthenticationProviderName):
        return value
    if isinstance(value, str):
        try:
            return AuthenticationProviderName(value)
        except ValueError:
            return None
    return None


def _finding_severity(value: object) -> FindingSeverity | None:
    if isinstance(value, FindingSeverity):
        return value
    if isinstance(value, str):
        try:
            return FindingSeverity(value)
        except ValueError:
            return None
    return None


def _asset_criticality(value: object) -> AssetCriticality | None:
    if isinstance(value, AssetCriticality):
        return value
    if isinstance(value, str):
        try:
            return AssetCriticality(value)
        except ValueError:
            return None
    return None


def _audit_log_event_type(value: object) -> AuditLogEventType | None:
    if isinstance(value, AuditLogEventType):
        return value
    if isinstance(value, str):
        try:
            return AuditLogEventType(value)
        except ValueError:
            return None
    return None
