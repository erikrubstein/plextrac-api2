"""Generated PlexTrac endpoint functions.

Do not edit by hand. Run scripts/generate_endpoints.py to refresh.
"""

from __future__ import annotations

from typing import Any

from plextrac_api.functions.common import endpoint_request
from plextrac_api.types.auth import AuthSession


def retrieve_analytics(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v1/clients/analytics\n\nPlexTrac endpoint: Retrieve Analytics"""
    return endpoint_request(session, "analytics", "retrieve_analytics", **kwargs)


def retrieve_analytics_findings(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v1/clients/analytics/findings\n\nPlexTrac endpoint: Retrieve Analytics Findings"""
    return endpoint_request(session, "analytics", "retrieve_analytics_findings", **kwargs)


def retreive_analytics_findings_aging(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v1/clients/analytics/findings/aging\n\nPlexTrac endpoint: Retreive Analytics Findings Aging"""
    return endpoint_request(session, "analytics", "retreive_analytics_findings_aging", **kwargs)


def get_finding_analytics_bootstrap(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/findingAnalytics/bootstrap\n\nPlexTrac endpoint: Get Finding Analytics Bootstrap"""
    return endpoint_request(session, "analytics", "get_finding_analytics_bootstrap", **kwargs)


def retrieve_analytics_assets(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/clients/analytics/assets/overview\n\nPlexTrac endpoint: Retrieve Analytics Assets"""
    return endpoint_request(session, "analytics", "retrieve_analytics_assets", **kwargs)


def retrieve_analytics_assets_with_filter(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/clients/analytics/assets\n\nPlexTrac endpoint: Retrieve Analytics Assets with Filter"""
    return endpoint_request(session, "analytics", "retrieve_analytics_assets_with_filter", **kwargs)


def analytics_trends_opened_closed(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/clients/analytics/trends/opened-closed\n\nPlexTrac endpoint: Analytics - Trends - Opened Closed"""
    return endpoint_request(session, "analytics", "analytics_trends_opened_closed", **kwargs)


def analytics_trends_from_creation_to_close(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/clients/analytics/trends/from-creation-to-close\n\nPlexTrac endpoint: Analytics - Trends - From creation to close"""
    return endpoint_request(session, "analytics", "analytics_trends_from_creation_to_close", **kwargs)


def analytics_trends_age_of_open_findings(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/clients/analytics/trends/age-of-open-findings\n\nPlexTrac endpoint: Analytics - Trends - Age of open findings"""
    return endpoint_request(session, "analytics", "analytics_trends_age_of_open_findings", **kwargs)


def analytics_trends_slas(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/sla/analytics/mean-time\n\nPlexTrac endpoint: Analytics - Trends - SLAs"""
    return endpoint_request(session, "analytics", "analytics_trends_slas", **kwargs)


def analytics_trends_sla_findings(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/sla/analytics/findings\n\nPlexTrac endpoint: Analytics - Trends - SLA Findings"""
    return endpoint_request(session, "analytics", "analytics_trends_sla_findings", **kwargs)

