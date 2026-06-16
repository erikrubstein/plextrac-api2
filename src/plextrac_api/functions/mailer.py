"""Generated PlexTrac endpoint functions.

Do not edit by hand. Run scripts/generate_endpoints.py to refresh.
"""

from __future__ import annotations

from typing import Any

from plextrac_api.functions.common import endpoint_request
from plextrac_api.types.auth import AuthSession


def get_mailer_templates(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/tenants/{tenantId}/mailer/templates\n\nPlexTrac endpoint: Get Mailer Templates"""
    return endpoint_request(session, "mailer", "get_mailer_templates", **kwargs)


def get_email_template(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/tenants/{tenantId}/mailer/templates/FORGOTTEN_PASSWORD\n\nPlexTrac endpoint: Get Email Template"""
    return endpoint_request(session, "mailer", "get_email_template", **kwargs)


def upsert_email_template(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v2/tenants/{tenantId}/mailer/templates/FORGOTTEN_PASSWORD\n\nPlexTrac endpoint: Upsert Email Template"""
    return endpoint_request(session, "mailer", "upsert_email_template", **kwargs)

