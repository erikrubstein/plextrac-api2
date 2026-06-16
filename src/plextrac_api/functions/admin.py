"""Generated PlexTrac endpoint functions.

Do not edit by hand. Run scripts/generate_endpoints.py to refresh.
"""

from __future__ import annotations

from typing import Any

from plextrac_api.functions.common import endpoint_request
from plextrac_api.types.auth import AuthSession


def get_available_authentication_providers(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/authenticate/providers\n\nPlexTrac endpoint: Get Available Authentication Providers"""
    return endpoint_request(session, "admin", "get_available_authentication_providers", **kwargs)


def get_tenant_provider_authentication_configuration(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/tenants/{tenantId}/providers/plextrac\n\nPlexTrac endpoint: Get Tenant Provider Authentication Configuration"""
    return endpoint_request(session, "admin", "get_tenant_provider_authentication_configuration", **kwargs)


def update_tenant_authentication_provider_configuration(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/tenants/{tenantId}/providers/plextrac\n\nPlexTrac endpoint: Update Tenant Authentication Provider Configuration"""
    return endpoint_request(session, "admin", "update_tenant_authentication_provider_configuration", **kwargs)


def update_tenant_user_authentication_method(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v2/authenticate/tenants/{tenantId}/users/{userId}/configuration\n\nPlexTrac endpoint: Update Tenant User Authentication Method"""
    return endpoint_request(session, "admin", "update_tenant_user_authentication_method", **kwargs)


def get_saml_provider(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/tenants/{tenantId}/saml/plextrac\n\nPlexTrac endpoint: Get Saml Provider"""
    return endpoint_request(session, "admin", "get_saml_provider", **kwargs)


def upsert_saml_configuration(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/tenants/{tenantId}/saml/plextrac\n\nPlexTrac endpoint: Upsert Saml Configuration"""
    return endpoint_request(session, "admin", "upsert_saml_configuration", **kwargs)


def get_user_permissions(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/tenants/{tenantId}/user/{userId}/permissions\n\nPlexTrac endpoint: Get User Permissions"""
    return endpoint_request(session, "admin", "get_user_permissions", **kwargs)


def get_role_users(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/tenants/{tenantId}/security/role/{roleKey}/users\n\nPlexTrac endpoint: Get Role Users"""
    return endpoint_request(session, "admin", "get_role_users", **kwargs)


def add_role_user(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v2/tenants/{tenantId}/security/role/{roleId}/users\n\nPlexTrac endpoint: Add Role User"""
    return endpoint_request(session, "admin", "add_role_user", **kwargs)


def remove_role_user(session: AuthSession, **kwargs: Any) -> Any:
    """DELETE /api/v2/tenants/{tenantId}/security/role/{roleId}/users/{userId}\n\nPlexTrac endpoint: Remove Role User"""
    return endpoint_request(session, "admin", "remove_role_user", **kwargs)


def get_available_security_roles(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/tenants/{tenantId}/security/role/available\n\nPlexTrac endpoint: Get Available Security Roles"""
    return endpoint_request(session, "admin", "get_available_security_roles", **kwargs)


def get_security_roles(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/tenants/{tenantId}/security/role\n\nPlexTrac endpoint: Get Security Roles"""
    return endpoint_request(session, "admin", "get_security_roles", **kwargs)


def get_security_role(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/tenants/{tenantId}/security/role/{roleId}\n\nPlexTrac endpoint: Get Security Role"""
    return endpoint_request(session, "admin", "get_security_role", **kwargs)


def get_role_name_availability(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/tenants/{tenantId}/security/role/availability\n\nPlexTrac endpoint: Get Role Name Availability"""
    return endpoint_request(session, "admin", "get_role_name_availability", **kwargs)


def create_security_role(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/tenants/{tenantId}/security/role\n\nPlexTrac endpoint: Create Security Role"""
    return endpoint_request(session, "admin", "create_security_role", **kwargs)


def update_security_role_info(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v2/tenants/{tenantId}/security/role/{roleId}/info\n\nPlexTrac endpoint: Update Security Role Info"""
    return endpoint_request(session, "admin", "update_security_role_info", **kwargs)


def update_security_role_permission(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v2/tenants/{tenantId}/security/role/{roleId}/permissions\n\nPlexTrac endpoint: Update Security Role Permission"""
    return endpoint_request(session, "admin", "update_security_role_permission", **kwargs)


def delete_security_role(session: AuthSession, **kwargs: Any) -> Any:
    """DELETE /api/v2/tenants/{tenantId}/security/role/{roleId}\n\nPlexTrac endpoint: Delete Security Role"""
    return endpoint_request(session, "admin", "delete_security_role", **kwargs)


def list_tenant_tags(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/tenant/{tenantId}/tag\n\nPlexTrac endpoint: List Tenant Tags"""
    return endpoint_request(session, "admin", "list_tenant_tags", **kwargs)


def create_tenant_tag(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v1/tenant/{tenantId}/tag\n\nPlexTrac endpoint: Create Tenant Tag"""
    return endpoint_request(session, "admin", "create_tenant_tag", **kwargs)


def delete_tenant_tag(session: AuthSession, **kwargs: Any) -> Any:
    """DELETE /api/v1/tenant/{tenantId}/tag/{tagId}\n\nPlexTrac endpoint: Delete Tenant Tag"""
    return endpoint_request(session, "admin", "delete_tenant_tag", **kwargs)


def search_tenant_tags(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/tenant/{tenantId}/tag/search\n\nPlexTrac endpoint: Search Tenant Tags"""
    return endpoint_request(session, "admin", "search_tenant_tags", **kwargs)


def find_tenant_tag(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v1/tenant/{tenantId}/tag/find\n\nPlexTrac endpoint: Find Tenant Tag"""
    return endpoint_request(session, "admin", "find_tenant_tag", **kwargs)


def get_sla_benchmarks(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/sla/benchmarks\n\nPlexTrac endpoint: Get SLA Benchmarks"""
    return endpoint_request(session, "admin", "get_sla_benchmarks", **kwargs)


def create_sla_benchmark(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/sla/benchmarks\n\nPlexTrac endpoint: Create SLA Benchmark"""
    return endpoint_request(session, "admin", "create_sla_benchmark", **kwargs)


def get_sla_benchmark(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/sla/benchmarks/{slaBenchmarkId}\n\nPlexTrac endpoint: Get SLA Benchmark"""
    return endpoint_request(session, "admin", "get_sla_benchmark", **kwargs)


def update_sla_benchmark(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v2/sla/benchmarks/{slaBenchmarkId}\n\nPlexTrac endpoint: Update SLA Benchmark"""
    return endpoint_request(session, "admin", "update_sla_benchmark", **kwargs)


def delete_sla_benchmark(session: AuthSession, **kwargs: Any) -> Any:
    """DELETE /api/v2/sla/benchmarks/{slaBenchmarkId}\n\nPlexTrac endpoint: Delete SLA Benchmark"""
    return endpoint_request(session, "admin", "delete_sla_benchmark", **kwargs)


def get_audit_log(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/auditlog\n\nPlexTrac endpoint: Get Audit Log"""
    return endpoint_request(session, "admin", "get_audit_log", **kwargs)

