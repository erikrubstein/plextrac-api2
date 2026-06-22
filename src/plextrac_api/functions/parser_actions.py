from __future__ import annotations

from pathlib import Path
from typing import BinaryIO

from plextrac_api.functions.common import rest_request
from plextrac_api.types.auth import AuthSession
from plextrac_api.types.common import OperationResult
from plextrac_api.types.parser_actions import (
    Parser,
    ParserAction,
    ParserActionInput,
    ParserActionSearchType,
    ParserPluginImportResult,
    ParserPluginSource,
)


def set_parser_plugin_actions_enabled(
    session: AuthSession,
    tenant_id: int | str,
    *,
    enabled: bool,
) -> OperationResult:
    """Set whether global parser-action mapping is enabled."""
    data = rest_request(
        session,
        "POST",
        f"/api/v1/tenant/{tenant_id}/integrationconfig/parserConfig",
        json={"enabled": enabled},
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def get_tenant_parsers(
    session: AuthSession,
    tenant_id: int | str,
) -> list[Parser]:
    """List parser sources available to a tenant."""
    data = rest_request(session, "GET", f"/api/v1/tenant/{tenant_id}/actions")
    return [Parser.from_api(item) for item in data if isinstance(item, dict)] if isinstance(data, list) else []


def list_tenant_parser_actions(
    session: AuthSession,
    tenant_id: int | str,
    parser_id: str,
    *,
    limit: int = 985,
    skip: int = 0,
    action_type: ParserActionSearchType = ParserActionSearchType.DEFAULT,
    query: str | None = None,
) -> list[ParserAction]:
    """List parser actions for one parser source."""
    params = {
        "limit": limit,
        "skip": skip,
        "type": action_type.value,
        "query": query,
    }
    data = rest_request(
        session,
        "GET",
        f"/api/v1/tenant/{tenant_id}/actions/{parser_id}",
        params={key: value for key, value in params.items() if value is not None},
    )
    return [ParserAction.from_api(item) for item in data if isinstance(item, dict)] if isinstance(data, list) else []


def get_tenant_parser_action(
    session: AuthSession,
    tenant_id: int | str,
    parser_id: str,
    action_id: int | str,
) -> ParserAction:
    """Get one parser action."""
    data = rest_request(
        session,
        "GET",
        f"/api/v1/tenant/{tenant_id}/actions/{parser_id}/action/{action_id}",
    )
    if not isinstance(data, dict):
        raise ValueError("PlexTrac parser action response was not a JSON object.")
    return ParserAction.from_api(data)


def create_tenant_parser_action(
    session: AuthSession,
    tenant_id: int | str,
    parser_id: str,
    action: ParserActionInput,
) -> ParserAction:
    """Create a parser action for a parser source."""
    data = rest_request(
        session,
        "POST",
        f"/api/v1/tenant/{tenant_id}/actions/{parser_id}/action",
        json=action.to_api(),
    )
    if not isinstance(data, dict):
        raise ValueError("PlexTrac parser action response was not a JSON object.")
    return ParserAction.from_api(data)


def update_parser_action(
    session: AuthSession,
    tenant_id: int | str,
    parser_id: str,
    action_id: int | str,
    action: ParserActionInput,
) -> ParserAction:
    """Update one parser action."""
    data = rest_request(
        session,
        "PUT",
        f"/api/v1/tenant/{tenant_id}/actions/{parser_id}/action/{action_id}",
        json=action.to_api(),
    )
    if not isinstance(data, dict):
        raise ValueError("PlexTrac parser action response was not a JSON object.")
    return ParserAction.from_api(data)


def bulk_update_tenant_parser_actions(
    session: AuthSession,
    tenant_id: int | str,
    parser_id: str,
    actions: list[ParserActionInput],
) -> list[ParserAction]:
    """Bulk update parser actions for a parser source."""
    data = rest_request(
        session,
        "PUT",
        f"/api/v1/tenant/{tenant_id}/actions/{parser_id}/bulk",
        json=[action.to_api() for action in actions],
    )
    return [ParserAction.from_api(item) for item in data if isinstance(item, dict)] if isinstance(data, list) else []


def import_parser_plugins(
    session: AuthSession,
    tenant_id: int | str,
    source: ParserPluginSource,
    file: str | Path | BinaryIO,
    *,
    filename: str | None = None,
    content_type: str | None = None,
) -> ParserPluginImportResult:
    """Import parser actions from a scan file."""
    close_after = None
    if isinstance(file, (str, Path)):
        file_path = Path(file)
        close_after = file_path.open("rb")
        file_obj: BinaryIO = close_after
        upload_name = filename or file_path.name
    else:
        file_obj = file
        upload_name = filename or Path(getattr(file, "name", "parser-upload")).name

    files = {"file": (upload_name, file_obj, content_type) if content_type else (upload_name, file_obj)}
    try:
        data = rest_request(
            session,
            "POST",
            f"/api/v1/tenant/{tenant_id}/actions/upload/{source.value}",
            files=files,
        )
    finally:
        if close_after is not None:
            close_after.close()
    return ParserPluginImportResult.from_api(data if isinstance(data, dict) else {"data": data})
