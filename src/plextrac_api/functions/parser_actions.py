"""Generated PlexTrac endpoint functions.

Do not edit by hand. Run scripts/generate_endpoints.py to refresh.
"""

from __future__ import annotations

from typing import Any

from plextrac_api.functions.common import endpoint_request
from plextrac_api.types.auth import AuthSession


def enable_disable_parser_plugin_actions(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v1/tenant/{tenantId}/integrationconfig/parserConfig\n\nPlexTrac endpoint: Enable/Disable Parser Plugin Actions"""
    return endpoint_request(session, "parser_actions", "enable_disable_parser_plugin_actions", **kwargs)


def get_tenant_parsers(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/tenant/{tenantId}/actions\n\nPlexTrac endpoint: Get Tenant Parsers"""
    return endpoint_request(session, "parser_actions", "get_tenant_parsers", **kwargs)


def get_tenant_parser_actions(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/tenant/{tenantId}/actions/{parserName}\n\nPlexTrac endpoint: Get Tenant Parser Actions"""
    return endpoint_request(session, "parser_actions", "get_tenant_parser_actions", **kwargs)


def get_tenant_parser_action(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/tenant/{tenantId}/actions/{parserName}/action/{actionId}\n\nPlexTrac endpoint: Get Tenant Parser Action"""
    return endpoint_request(session, "parser_actions", "get_tenant_parser_action", **kwargs)


def create_tenant_parser_action(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v1/tenant/{tenantId}/actions/{parserName}/action\n\nPlexTrac endpoint: Create Tenant Parser Action"""
    return endpoint_request(session, "parser_actions", "create_tenant_parser_action", **kwargs)


def update_parser_action(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v1/tenant/{tenantId}/actions/{parserName}/action/{actionId}\n\nPlexTrac endpoint: Update Parser Action"""
    return endpoint_request(session, "parser_actions", "update_parser_action", **kwargs)


def update(session: AuthSession, **kwargs: Any) -> Any:
    """Alias for `update_parser_action`."""
    return update_parser_action(session, **kwargs)


def bulk_update_tenant_parser_actions(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v1/tenant/{tenantId}/actions/{parserName}/bulk\n\nPlexTrac endpoint: Bulk Update Tenant Parser Actions"""
    return endpoint_request(session, "parser_actions", "bulk_update_tenant_parser_actions", **kwargs)


def import_parser_plugins(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v1/tenant/{tenantId}/actions/upload/{source}\n\nPlexTrac endpoint: Import Parser Plugins"""
    return endpoint_request(session, "parser_actions", "import_parser_plugins", **kwargs)

