from __future__ import annotations

import base64
import json
import time
from dataclasses import dataclass

from plextrac_api.types.common import JsonDict


@dataclass(slots=True)
class AuthSession:
    base_url: str
    token: str
    refresh_token: str | None = None
    expires_at: float | None = None
    username: str | None = None
    password: str | None = None

    @classmethod
    def from_auth_response(
        cls,
        data: JsonDict,
        *,
        base_url: str,
        username: str | None = None,
        password: str | None = None,
    ) -> AuthSession:
        token = _first_string(data, ("token", "jwt", "jwtToken", "accessToken", "access_token"))
        refresh_token = _first_string(data, ("refreshToken", "refresh_token"))

        nested = data.get("data")
        if not token and isinstance(nested, dict):
            token = _first_string(
                nested,
                ("token", "jwt", "jwtToken", "accessToken", "access_token"),
            )
            refresh_token = refresh_token or _first_string(
                nested,
                ("refreshToken", "refresh_token"),
            )

        if not token:
            raise ValueError("PlexTrac auth response did not include a token.")

        return cls(
            base_url=base_url.rstrip("/"),
            token=token,
            refresh_token=refresh_token,
            expires_at=jwt_expiration(token),
            username=username,
            password=password,
        )

    @classmethod
    def from_token(
        cls,
        *,
        base_url: str,
        token: str,
        refresh_token: str | None = None,
    ) -> AuthSession:
        return cls(
            base_url=base_url.rstrip("/"),
            token=token,
            refresh_token=refresh_token,
            expires_at=jwt_expiration(token),
        )

    @classmethod
    def from_dict(cls, data: JsonDict) -> AuthSession:
        token = data.get("token")
        base_url = data.get("base_url")
        if not isinstance(token, str) or not token:
            raise ValueError("Saved session did not include a token.")
        if not isinstance(base_url, str) or not base_url:
            raise ValueError("Saved session did not include base_url.")
        return cls(
            base_url=base_url.rstrip("/"),
            token=token,
            refresh_token=data.get("refresh_token"),
            expires_at=data.get("expires_at"),
            username=data.get("username"),
            password=data.get("password"),
        )

    def to_dict(self, *, include_password: bool = False) -> JsonDict:
        data: JsonDict = {
            "base_url": self.base_url,
            "token": self.token,
            "refresh_token": self.refresh_token,
            "expires_at": self.expires_at,
            "username": self.username,
        }
        if include_password:
            data["password"] = self.password
        return {key: value for key, value in data.items() if value is not None}

    def is_expiring(self, *, within_seconds: int = 60) -> bool:
        if self.expires_at is None:
            return False
        return time.time() >= self.expires_at - within_seconds


def jwt_expiration(token: str | None) -> float | None:
    if not token or token.count(".") < 2:
        return None
    try:
        payload_segment = token.split(".")[1]
        payload_segment += "=" * (-len(payload_segment) % 4)
        payload = json.loads(base64.urlsafe_b64decode(payload_segment.encode()))
    except Exception:
        return None
    exp = payload.get("exp")
    if isinstance(exp, (int, float)):
        return float(exp)
    return None


def _first_string(data: JsonDict, keys: tuple[str, ...]) -> str | None:
    for key in keys:
        value = data.get(key)
        if isinstance(value, str) and value:
            return value
    return None
