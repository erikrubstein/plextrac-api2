from __future__ import annotations

import hashlib
import hmac


def verify_signature(
    *,
    payload: bytes | str,
    signature: str,
    secret: str,
    algorithm: str = "sha256",
) -> bool:
    if isinstance(payload, str):
        payload = payload.encode()
    digestmod = getattr(hashlib, algorithm)
    expected = hmac.new(secret.encode(), payload, digestmod).hexdigest()
    supplied = signature.strip()
    if "=" in supplied:
        supplied = supplied.split("=", 1)[1]
    return hmac.compare_digest(expected, supplied)

