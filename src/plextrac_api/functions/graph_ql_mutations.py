"""Generated PlexTrac endpoint functions.

Do not edit by hand. Run scripts/generate_endpoints.py to refresh.
"""

from __future__ import annotations

from typing import Any

from plextrac_api.functions.common import endpoint_request
from plextrac_api.types.auth import AuthSession


def finding_update(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: FindingUpdate"""
    return endpoint_request(session, "graph_ql_mutations", "finding_update", **kwargs)


def narrative_update(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: NarrativeUpdate"""
    return endpoint_request(session, "graph_ql_mutations", "narrative_update", **kwargs)

