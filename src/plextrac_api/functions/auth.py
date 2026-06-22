from __future__ import annotations

import json
from pathlib import Path

import httpx

from plextrac_api.functions.common import (
    PlexTracAuthError,
    _parse_response,
    build_auth_headers,
)
from plextrac_api.functions.common import (
    refresh_session as _refresh_session,
)
from plextrac_api.types.auth import AuthSession
from plextrac_api.types.common import JsonDict


def create_session(
    base_url: str,
    username: str,
    password: str,
    *,
    mfa_code: str | None = None,
    session_path: str | Path | None = None,
) -> AuthSession:
    """Log in with PlexTrac credentials and return an authenticated session."""

    payload: JsonDict = {"username": username, "password": password}
    if mfa_code:
        payload["code"] = mfa_code

    with httpx.Client(base_url=base_url.rstrip("/"), timeout=30.0) as client:
        response = client.post(
            "/api/v1/authenticate",
            json=payload,
            headers=build_auth_headers(),
        )
    data = _parse_response(response)
    if not isinstance(data, dict):
        raise PlexTracAuthError("PlexTrac auth response was not a JSON object.")
    session = AuthSession.from_auth_response(
        data,
        base_url=base_url,
        username=username,
        password=password,
    )
    if session_path is not None:
        save_session(session, session_path)
    return session


def session_from_token(
    base_url: str,
    token: str,
    *,
    cookie: str | None = None,
    refresh_token: str | None = None,
    tenant_id: int | str | None = None,
) -> AuthSession:
    """Create a session from an existing PlexTrac bearer token."""

    return AuthSession.from_token(
        base_url=base_url,
        token=token,
        cookie=cookie,
        refresh_token=refresh_token,
        tenant_id=tenant_id,
    )


def refresh_session(
    session: AuthSession,
    *,
    session_path: str | Path | None = None,
) -> AuthSession:
    """Refresh a PlexTrac session token in place."""

    refreshed = _refresh_session(session)
    if session_path is not None:
        save_session(refreshed, session_path)
    return refreshed


def save_session(
    session: AuthSession,
    path: str | Path,
    *,
    include_password: bool = False,
) -> None:
    """Persist session details for reuse, excluding the password unless requested."""

    session_path = Path(path)
    session_path.parent.mkdir(parents=True, exist_ok=True)
    session_path.write_text(
        json.dumps(session.to_dict(include_password=include_password), indent=2),
        encoding="utf-8",
    )
    try:
        session_path.chmod(0o600)
    except OSError:
        pass


def load_session(path: str | Path) -> AuthSession:
    """Load a saved PlexTrac session from disk."""

    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Saved session file must contain a JSON object.")
    return AuthSession.from_dict(data)
