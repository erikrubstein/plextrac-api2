from __future__ import annotations

from plextrac_api.functions.common import rest_request
from plextrac_api.types.auth import AuthSession
from plextrac_api.types.common import OperationResult
from plextrac_api.types.substatus import Substatus, SubstatusInput


def list_substatuses(
    session: AuthSession,
) -> list[Substatus]:
    """List configured finding substatuses."""
    data = rest_request(session, "GET", "/api/v3/substatus")
    return _substatus_list(data)


def create_substatus(
    session: AuthSession,
    substatus: SubstatusInput,
) -> Substatus:
    """Create a finding substatus."""
    if substatus.status is None:
        raise TypeError("create_substatus requires substatus.status.")
    if substatus.value is None:
        raise TypeError("create_substatus requires substatus.value.")
    data = rest_request(session, "POST", "/api/v3/substatus", json=substatus.to_api())
    return _substatus_object(data, "PlexTrac create substatus response was not a JSON object.")


def update_substatus(
    session: AuthSession,
    substatus_cuid: str,
    substatus: SubstatusInput,
) -> Substatus:
    """Update a finding substatus."""
    data = rest_request(
        session,
        "PATCH",
        f"/api/v3/substatus/{substatus_cuid}",
        json=substatus.to_api(),
    )
    return _substatus_object(data, "PlexTrac update substatus response was not a JSON object.")


def delete_substatus(
    session: AuthSession,
    substatus_cuid: str,
) -> OperationResult:
    """Delete a finding substatus."""
    data = rest_request(session, "DELETE", f"/api/v3/substatus/{substatus_cuid}")
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def _substatus_list(data: object) -> list[Substatus]:
    if isinstance(data, list):
        return [Substatus.from_api(item) for item in data if isinstance(item, dict)]
    if isinstance(data, dict):
        items = data.get("data")
        if isinstance(items, list):
            return [Substatus.from_api(item) for item in items if isinstance(item, dict)]
    return []


def _substatus_object(data: object, error_message: str) -> Substatus:
    if isinstance(data, dict):
        nested = data.get("data")
        if isinstance(nested, dict):
            return Substatus.from_api(nested)
        return Substatus.from_api(data)
    raise ValueError(error_message)
