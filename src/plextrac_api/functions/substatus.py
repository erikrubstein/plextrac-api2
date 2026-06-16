"""Generated PlexTrac endpoint functions.

Do not edit by hand. Run scripts/generate_endpoints.py to refresh.
"""

from __future__ import annotations

from typing import Any

from plextrac_api.functions.common import endpoint_request
from plextrac_api.types.auth import AuthSession


def list_substatus(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v3/substatus\n\nPlexTrac endpoint: List Substatus"""
    return endpoint_request(session, "substatus", "list_substatus", **kwargs)


def list(session: AuthSession, **kwargs: Any) -> Any:
    """Alias for `list_substatus`."""
    return list_substatus(session, **kwargs)


def create_substatus(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v3/substatus\n\nPlexTrac endpoint: Create Substatus"""
    return endpoint_request(session, "substatus", "create_substatus", **kwargs)


def create(session: AuthSession, **kwargs: Any) -> Any:
    """Alias for `create_substatus`."""
    return create_substatus(session, **kwargs)


def update_substatus(session: AuthSession, **kwargs: Any) -> Any:
    """PATCH /api/v3/substatus/{substatusCuid}\n\nPlexTrac endpoint: Update Substatus"""
    return endpoint_request(session, "substatus", "update_substatus", **kwargs)


def update(session: AuthSession, **kwargs: Any) -> Any:
    """Alias for `update_substatus`."""
    return update_substatus(session, **kwargs)


def delete_substatus(session: AuthSession, **kwargs: Any) -> Any:
    """DELETE /api/v3/substatus/{substatusCuid}\n\nPlexTrac endpoint: Delete Substatus"""
    return endpoint_request(session, "substatus", "delete_substatus", **kwargs)


def delete(session: AuthSession, **kwargs: Any) -> Any:
    """Alias for `delete_substatus`."""
    return delete_substatus(session, **kwargs)

