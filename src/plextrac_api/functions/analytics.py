from __future__ import annotations

from plextrac_api.functions.common import rest_request
from plextrac_api.types.analytics import (
    AnalyticsAssetRecord,
    AnalyticsFilter,
    AnalyticsFindingRecord,
    AnalyticsRecord,
    AnalyticsResult,
    AnalyticsTrendFilter,
    AnalyticsTrendRecord,
    AssetAnalyticsFilter,
    FindingAnalyticsBootstrapFilter,
    SlaAnalyticsFilter,
)
from plextrac_api.types.auth import AuthSession


def retrieve_analytics(
    session: AuthSession,
    filters: AnalyticsFilter,
) -> AnalyticsResult[AnalyticsRecord]:
    """Retrieve client/report/finding analytics with the documented analytics filter."""
    data = rest_request(session, "POST", "/api/v1/clients/analytics", json=filters.to_api())
    return AnalyticsResult.from_api(data if isinstance(data, (dict, list)) else {"data": data})


def retrieve_analytics_findings(
    session: AuthSession,
    filters: AnalyticsFilter,
) -> AnalyticsResult[AnalyticsFindingRecord]:
    """Retrieve paginated analytics finding rows."""
    data = rest_request(session, "POST", "/api/v1/clients/analytics/findings", json=filters.to_api())
    return AnalyticsResult.from_api(
        data if isinstance(data, (dict, list)) else {"data": data},
        record_kind="finding",
        record_parser=AnalyticsFindingRecord.from_api,
    )


def retrieve_analytics_findings_aging(
    session: AuthSession,
    filters: AnalyticsFilter,
) -> AnalyticsResult[AnalyticsFindingRecord]:
    """Retrieve finding aging analytics."""
    data = rest_request(
        session,
        "POST",
        "/api/v1/clients/analytics/findings/aging",
        json=filters.to_api(),
    )
    return AnalyticsResult.from_api(
        data if isinstance(data, (dict, list)) else {"data": data},
        record_kind="finding",
        record_parser=AnalyticsFindingRecord.from_api,
    )


def get_finding_analytics_bootstrap(
    session: AuthSession,
    filters: FindingAnalyticsBootstrapFilter,
) -> AnalyticsResult[AnalyticsRecord]:
    """Retrieve bootstrap values for finding analytics filters."""
    data = rest_request(
        session,
        "POST",
        "/api/v2/findingAnalytics/bootstrap",
        json=filters.to_api(),
    )
    return AnalyticsResult.from_api(data if isinstance(data, (dict, list)) else {"data": data})


def retrieve_analytics_assets(
    session: AuthSession,
    filters: AssetAnalyticsFilter,
) -> AnalyticsResult[AnalyticsAssetRecord]:
    """Retrieve asset analytics overview data."""
    data = rest_request(
        session,
        "POST",
        "/api/v2/clients/analytics/assets/overview",
        json=filters.to_api(),
    )
    return AnalyticsResult.from_api(
        data if isinstance(data, (dict, list)) else {"data": data},
        record_kind="asset",
        record_parser=AnalyticsAssetRecord.from_api,
    )


def retrieve_analytics_assets_with_filter(
    session: AuthSession,
    filters: AssetAnalyticsFilter,
) -> AnalyticsResult[AnalyticsAssetRecord]:
    """Retrieve filtered asset analytics rows."""
    params = {
        "limit": filters.limit,
        "offset": filters.offset,
    }
    data = rest_request(
        session,
        "POST",
        "/api/v2/clients/analytics/assets",
        params={key: value for key, value in params.items() if value is not None},
        json=filters.to_api(),
    )
    return AnalyticsResult.from_api(
        data if isinstance(data, (dict, list)) else {"data": data},
        record_kind="asset",
        record_parser=AnalyticsAssetRecord.from_api,
    )


def retrieve_analytics_trends_opened_closed(
    session: AuthSession,
    filters: AnalyticsTrendFilter,
) -> AnalyticsResult[AnalyticsTrendRecord]:
    """Retrieve opened-versus-closed trend analytics."""
    data = rest_request(
        session,
        "POST",
        "/api/v2/clients/analytics/trends/opened-closed",
        json=filters.to_api(),
    )
    return AnalyticsResult.from_api(
        data if isinstance(data, (dict, list)) else {"data": data},
        record_parser=AnalyticsTrendRecord.from_api,
    )


def retrieve_analytics_trends_from_creation_to_close(
    session: AuthSession,
    filters: AnalyticsTrendFilter,
) -> AnalyticsResult[AnalyticsTrendRecord]:
    """Retrieve trend analytics for finding creation-to-close time."""
    data = rest_request(
        session,
        "POST",
        "/api/v2/clients/analytics/trends/from-creation-to-close",
        json=filters.to_api(),
    )
    return AnalyticsResult.from_api(
        data if isinstance(data, (dict, list)) else {"data": data},
        record_parser=AnalyticsTrendRecord.from_api,
    )


def retrieve_analytics_trends_slas(
    session: AuthSession,
    filters: SlaAnalyticsFilter,
) -> AnalyticsResult[AnalyticsTrendRecord]:
    """Retrieve SLA mean-time analytics."""
    data = rest_request(
        session,
        "POST",
        "/api/v2/sla/analytics/mean-time",
        json=filters.to_api(),
    )
    return AnalyticsResult.from_api(
        data if isinstance(data, (dict, list)) else {"data": data},
        record_parser=AnalyticsTrendRecord.from_api,
    )


def retrieve_analytics_trends_sla_findings(
    session: AuthSession,
    filters: SlaAnalyticsFilter,
) -> AnalyticsResult[AnalyticsFindingRecord]:
    """Retrieve SLA finding analytics."""
    data = rest_request(
        session,
        "POST",
        "/api/v2/sla/analytics/findings",
        json=filters.to_api(),
    )
    return AnalyticsResult.from_api(
        data if isinstance(data, (dict, list)) else {"data": data},
        record_kind="finding",
        record_parser=AnalyticsFindingRecord.from_api,
    )
