"""Generated PlexTrac endpoint functions.

Do not edit by hand. Run scripts/generate_endpoints.py to refresh.
"""

from __future__ import annotations

from typing import Any

from plextrac_api.functions.common import endpoint_request
from plextrac_api.types.auth import AuthSession


def client_asset(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: clientAsset"""
    return endpoint_request(session, "graph_ql_queries", "client_asset", **kwargs)

