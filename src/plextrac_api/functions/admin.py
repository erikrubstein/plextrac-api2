from __future__ import annotations

from typing import cast

from plextrac_api.functions.common import rest_request
from plextrac_api.types.admin import (
    AuditLogEntry,
    AuthenticationProvider,
    AuthenticationProviderConfiguration,
    AvailableSecurityRole,
    RoleNameAvailability,
    SamlConfiguration,
    SecurityRole,
    SecurityRolePermissionGroup,
    SecurityRoleResult,
    SecurityRoleUser,
    SLABenchmark,
    SLABenchmarkResult,
    TenantTag,
    TenantTagPage,
    TenantTagScope,
    UserPermissions,
)
from plextrac_api.types.auth import AuthSession
from plextrac_api.types.common import JsonDict, OperationResult, clean


def list_authentication_providers(
    session: AuthSession,
) -> list[AuthenticationProvider]:
    """List supported authentication providers."""
    data = rest_request(session, "GET", "/api/v2/authenticate/providers")
    return [AuthenticationProvider.from_api(item) for item in _raw_items(data)]


def get_tenant_authentication_provider_configuration(
    session: AuthSession,
    tenant_id: int | str,
) -> AuthenticationProviderConfiguration:
    """Get tenant authentication provider configuration."""
    data = rest_request(session, "GET", f"/api/v2/tenants/{tenant_id}/providers/plextrac")
    return AuthenticationProviderConfiguration.from_api(_object(data, "authentication provider configuration"))


def update_tenant_authentication_provider_configuration(
    session: AuthSession,
    tenant_id: int | str,
    *,
    enabled: bool,
    provider: str,
    uri: str,
    provider_client_id: str,
    provider_client_secret: str,
    auth_server_id: str | None = None,
) -> OperationResult:
    """Update tenant authentication provider configuration."""
    data = rest_request(
        session,
        "POST",
        f"/api/v2/tenants/{tenant_id}/providers/plextrac",
        json=clean({
            "enabled": enabled,
            "provider": provider,
            "uri": uri,
            "providerClientId": provider_client_id,
            "providerClientSecret": provider_client_secret,
            "authServerId": auth_server_id,
        }),
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def update_tenant_user_authentication_method(
    session: AuthSession,
    tenant_id: int | str,
    user_id: int | str,
    *,
    authentication_provider: str,
    mfa_enabled: bool,
    mfa_qrcode: str = "",
    mfa_secret: str = "",
    mfa_url: str = "",
) -> OperationResult:
    """Update the authentication method a tenant user can use."""
    data = rest_request(
        session,
        "PUT",
        f"/api/v2/authenticate/tenants/{tenant_id}/users/{user_id}/configuration",
        json={
            "authentication_provider": authentication_provider,
            "mfa": {
                "enabled": mfa_enabled,
                "qrcode": mfa_qrcode,
                "secret": mfa_secret,
                "url": mfa_url,
            },
        },
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def get_saml_configuration(
    session: AuthSession,
    tenant_id: int | str,
) -> SamlConfiguration:
    """Get the tenant SAML provider configuration."""
    data = rest_request(session, "GET", f"/api/v2/tenants/{tenant_id}/saml/plextrac")
    return SamlConfiguration.from_api(_object(data, "SAML configuration"))


def upsert_saml_configuration(
    session: AuthSession,
    tenant_id: int | str,
    configuration: SamlConfiguration,
) -> SamlConfiguration:
    """Create or update the tenant SAML provider configuration."""
    data = rest_request(
        session,
        "POST",
        f"/api/v2/tenants/{tenant_id}/saml/plextrac",
        json=configuration.to_api(),
    )
    return SamlConfiguration.from_api(_object(data, "SAML configuration"))


def get_user_permissions(
    session: AuthSession,
    tenant_id: int | str,
    user_id: int | str,
) -> UserPermissions:
    """Get RBAC permissions for a tenant user."""
    data = rest_request(session, "GET", f"/api/v2/tenants/{tenant_id}/user/{user_id}/permissions")
    return UserPermissions.from_api(_object(data, "user permissions"))


def list_security_role_users(
    session: AuthSession,
    tenant_id: int | str,
    role_key: str,
) -> list[SecurityRoleUser]:
    """List users associated with an RBAC security role."""
    data = rest_request(session, "GET", f"/api/v2/tenants/{tenant_id}/security/role/{role_key}/users")
    return [SecurityRoleUser.from_api(item) for item in _dict_items(data)]


def add_security_role_user(
    session: AuthSession,
    tenant_id: int | str,
    role_id: int | str,
    user_id: int | str,
) -> SecurityRole:
    """Add a user to an RBAC security role."""
    data = rest_request(
        session,
        "PUT",
        f"/api/v2/tenants/{tenant_id}/security/role/{role_id}/users",
        json={"userId": user_id},
    )
    return SecurityRole.from_api(_object(data, "security role"))


def remove_security_role_user(
    session: AuthSession,
    tenant_id: int | str,
    role_id: int | str,
    user_id: int | str,
) -> SecurityRole:
    """Remove a user from an RBAC security role."""
    data = rest_request(
        session,
        "DELETE",
        f"/api/v2/tenants/{tenant_id}/security/role/{role_id}/users/{user_id}",
    )
    return SecurityRole.from_api(_object(data, "security role"))


def list_available_security_roles(
    session: AuthSession,
    tenant_id: int | str,
) -> list[AvailableSecurityRole]:
    """List security roles available for assignment."""
    data = rest_request(session, "GET", f"/api/v2/tenants/{tenant_id}/security/role/available")
    return [AvailableSecurityRole.from_api(item) for item in _raw_items(data)]


def list_security_roles(
    session: AuthSession,
    tenant_id: int | str,
) -> list[SecurityRole]:
    """List RBAC security roles for a tenant."""
    data = rest_request(session, "GET", f"/api/v2/tenants/{tenant_id}/security/role")
    return [SecurityRole.from_api(item) for item in _dict_items(data)]


def get_security_role(
    session: AuthSession,
    tenant_id: int | str,
    role_id: int | str,
) -> SecurityRole:
    """Get one RBAC security role."""
    data = rest_request(session, "GET", f"/api/v2/tenants/{tenant_id}/security/role/{role_id}")
    return SecurityRole.from_api(_object(data, "security role"))


def check_security_role_name_availability(
    session: AuthSession,
    tenant_id: int | str,
    key: str,
) -> RoleNameAvailability:
    """Check whether a generated RBAC role key is available."""
    data = rest_request(
        session,
        "POST",
        f"/api/v2/tenants/{tenant_id}/security/role/availability",
        json={"key": key},
    )
    return RoleNameAvailability.from_api(_object(data, "security role availability"))


def create_security_role(
    session: AuthSession,
    tenant_id: int | str,
) -> SecurityRole:
    """Create a new RBAC security role."""
    data = rest_request(session, "POST", f"/api/v2/tenants/{tenant_id}/security/role")
    return SecurityRole.from_api(_object(data, "security role"))


def update_security_role_info(
    session: AuthSession,
    tenant_id: int | str,
    role_id: int | str,
    *,
    title: str,
    description: str,
    enabled: bool,
) -> SecurityRole:
    """Update an RBAC security role's display information."""
    data = rest_request(
        session,
        "PUT",
        f"/api/v2/tenants/{tenant_id}/security/role/{role_id}/info",
        json={"title": title, "description": description, "enabled": enabled},
    )
    return SecurityRole.from_api(_object(data, "security role"))


def update_security_role_permissions(
    session: AuthSession,
    tenant_id: int | str,
    role_id: int | str,
    *,
    permissions: list[str] | None = None,
    permission_configuration: list[SecurityRolePermissionGroup] | None = None,
) -> SecurityRole:
    """Update an RBAC security role's permissions."""
    payload = {
        "permissions": permissions,
        "permissionConfiguration": [
            group.to_api() for group in permission_configuration
        ]
        if permission_configuration is not None
        else None,
    }
    data = rest_request(
        session,
        "PUT",
        f"/api/v2/tenants/{tenant_id}/security/role/{role_id}/permissions",
        json={key: value for key, value in payload.items() if value is not None},
    )
    return SecurityRole.from_api(_object(data, "security role"))


def delete_security_role(
    session: AuthSession,
    tenant_id: int | str,
    role_id: int | str,
) -> SecurityRoleResult:
    """Delete an RBAC security role."""
    data = rest_request(session, "DELETE", f"/api/v2/tenants/{tenant_id}/security/role/{role_id}")
    return SecurityRoleResult.from_api(_object(data, "security role delete"))


def list_tenant_tags(
    session: AuthSession,
    tenant_id: int | str,
    *,
    limit: int = 10,
    offset: int = 0,
) -> TenantTagPage:
    """List tenant tags."""
    data = rest_request(
        session,
        "GET",
        f"/api/v1/tenant/{tenant_id}/tag",
        params={"limit": limit, "offset": offset},
    )
    return TenantTagPage.from_api(_object(data, "tenant tag list"))


def create_tenant_tag(
    session: AuthSession,
    tenant_id: int | str,
    *,
    name: str,
    owner_id: int | str | None = None,
    scope: TenantTagScope = TenantTagScope.TENANT,
) -> OperationResult:
    """Create a tenant tag."""
    data = rest_request(
        session,
        "POST",
        f"/api/v1/tenant/{tenant_id}/tag",
        json={"name": name, "scope": scope.value, "ownerId": owner_id or tenant_id},
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def delete_tenant_tag(
    session: AuthSession,
    tenant_id: int | str,
    tag_id: str,
) -> OperationResult:
    """Delete a tenant tag."""
    data = rest_request(session, "DELETE", f"/api/v1/tenant/{tenant_id}/tag/{tag_id}")
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def search_tenant_tags(
    session: AuthSession,
    tenant_id: int | str,
    *,
    text: str,
    limit: int = 20,
    offset: int = 0,
) -> TenantTagPage:
    """Search tenant tags by text."""
    data = rest_request(
        session,
        "GET",
        f"/api/v1/tenant/{tenant_id}/tag/search",
        params={"text": text, "limit": limit, "offset": offset},
    )
    return TenantTagPage.from_api(_object(data, "tenant tag search"))


def find_tenant_tag(
    session: AuthSession,
    tenant_id: int | str,
    *,
    name: str,
) -> TenantTag:
    """Find a tenant tag by exact name."""
    data = rest_request(
        session,
        "POST",
        f"/api/v1/tenant/{tenant_id}/tag/find",
        json={"name": name},
    )
    return TenantTag.from_api(_object(data, "tenant tag"))


def list_sla_benchmarks(
    session: AuthSession,
) -> list[SLABenchmark]:
    """List SLA benchmarks."""
    data = rest_request(session, "GET", "/api/v2/sla/benchmarks")
    return [SLABenchmark.from_api(item) for item in _dict_items(data)]


def create_sla_benchmark(
    session: AuthSession,
    benchmark: SLABenchmark,
) -> SLABenchmark:
    """Create an SLA benchmark."""
    data = rest_request(session, "POST", "/api/v2/sla/benchmarks", json=benchmark.to_api())
    return SLABenchmark.from_api(_object(data, "SLA benchmark"))


def get_sla_benchmark(
    session: AuthSession,
    sla_benchmark_id: int | str,
) -> SLABenchmark:
    """Get one SLA benchmark."""
    data = rest_request(session, "GET", f"/api/v2/sla/benchmarks/{sla_benchmark_id}")
    return SLABenchmark.from_api(_object(data, "SLA benchmark"))


def update_sla_benchmark(
    session: AuthSession,
    sla_benchmark_id: int | str,
    benchmark: SLABenchmark,
) -> SLABenchmarkResult:
    """Update an SLA benchmark."""
    data = rest_request(
        session,
        "PUT",
        f"/api/v2/sla/benchmarks/{sla_benchmark_id}",
        json=benchmark.to_api(),
    )
    return SLABenchmarkResult.from_api(_object(data, "SLA benchmark update"))


def delete_sla_benchmark(
    session: AuthSession,
    sla_benchmark_id: int | str,
) -> SLABenchmarkResult:
    """Delete an SLA benchmark."""
    data = rest_request(session, "DELETE", f"/api/v2/sla/benchmarks/{sla_benchmark_id}")
    return SLABenchmarkResult.from_api(_object(data, "SLA benchmark delete"))


def list_audit_log_entries(
    session: AuthSession,
    *,
    limit: int = 5,
    offset: int = 0,
) -> list[AuditLogEntry]:
    """List audit log entries."""
    data = rest_request(session, "GET", "/api/v2/auditlog", params={"limit": limit, "offset": offset})
    return [AuditLogEntry.from_api(item) for item in _dict_items(data)]


def _object(data: object, label: str) -> JsonDict:
    if isinstance(data, dict):
        nested = data.get("data")
        if isinstance(nested, dict):
            return cast(JsonDict, nested)
        return cast(JsonDict, data)
    raise ValueError(f"PlexTrac {label} response was not a JSON object.")


def _dict_items(data: object) -> list[JsonDict]:
    if isinstance(data, dict):
        nested = data.get("data")
        if isinstance(nested, list):
            return [cast(JsonDict, item) for item in nested if isinstance(item, dict)]
        return []
    return [cast(JsonDict, item) for item in data if isinstance(item, dict)] if isinstance(data, list) else []


def _raw_items(data: object) -> list[object]:
    if isinstance(data, dict):
        nested = data.get("data")
        if isinstance(nested, list):
            return nested
        return []
    return data if isinstance(data, list) else []
