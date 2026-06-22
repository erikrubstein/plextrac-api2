from __future__ import annotations

from plextrac_api.functions.common import rest_request
from plextrac_api.types.auth import AuthSession
from plextrac_api.types.common import OperationResult
from plextrac_api.types.mailer import EmailTemplate, EmailTemplateInput, EmailTemplateKind


def list_mailer_templates(
    session: AuthSession,
    tenant_id: int | str,
) -> list[EmailTemplate]:
    """List mailer templates configured for a tenant."""
    data = rest_request(session, "GET", f"/api/v2/tenants/{tenant_id}/mailer/templates")
    return _template_list(data)


def get_email_template(
    session: AuthSession,
    tenant_id: int | str,
    template: EmailTemplateKind = EmailTemplateKind.FORGOTTEN_PASSWORD,
) -> EmailTemplate:
    """Get one tenant email template."""
    data = rest_request(
        session,
        "GET",
        f"/api/v2/tenants/{tenant_id}/mailer/templates/{template.value}",
    )
    if not isinstance(data, dict):
        raise ValueError("PlexTrac email template response was not a JSON object.")
    return EmailTemplate.from_api(data)


def upsert_email_template(
    session: AuthSession,
    tenant_id: int | str,
    email_template: EmailTemplateInput,
    *,
    template: EmailTemplateKind = EmailTemplateKind.FORGOTTEN_PASSWORD,
) -> OperationResult:
    """Create or replace one tenant email template."""
    data = rest_request(
        session,
        "PUT",
        f"/api/v2/tenants/{tenant_id}/mailer/templates/{template.value}",
        json=email_template.to_api(),
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def _template_list(data: object) -> list[EmailTemplate]:
    if isinstance(data, list):
        return [EmailTemplate.from_api(item) for item in data if isinstance(item, dict)]
    if isinstance(data, dict):
        items = data.get("data") or data.get("templates")
        if isinstance(items, list):
            return [EmailTemplate.from_api(item) for item in items if isinstance(item, dict)]
    return []
