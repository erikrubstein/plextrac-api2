from __future__ import annotations

import hashlib
import hmac
import json
from collections.abc import Mapping

from plextrac_api.types.common import JsonDict
from plextrac_api.types.webhooks import (
    ParsedWebhookEvent,
    WebhookEventType,
    WebhookSignatureAlgorithm,
    webhook_event_from_api,
)

WEBHOOK_SIGNATURE_HEADER = "x-authorization-hmac-256"

def verify_signature(
    *,
    payload: bytes | str,
    signature: str,
    secret: str,
    algorithm: WebhookSignatureAlgorithm = WebhookSignatureAlgorithm.SHA256,
) -> bool:
    """Verify a PlexTrac webhook HMAC signature."""
    if isinstance(payload, str):
        payload = payload.encode()
    digestmod = getattr(hashlib, algorithm.value)
    expected = hmac.new(secret.encode(), payload, digestmod).hexdigest()
    supplied = signature.strip()
    if "=" in supplied:
        supplied = supplied.split("=", 1)[1]
    return hmac.compare_digest(expected, supplied)


def signature_from_headers(
    headers: Mapping[str, str],
) -> str | None:
    """Return PlexTrac's webhook signature header from a case-insensitive header mapping."""
    for key, value in headers.items():
        if key.lower() == WEBHOOK_SIGNATURE_HEADER:
            return value
    return None


def parse_webhook_event(
    payload: bytes | str | JsonDict,
    *,
    event_type: WebhookEventType | None = None,
) -> ParsedWebhookEvent:
    """Parse a PlexTrac webhook payload into the matching documented event type."""
    data = _payload_dict(payload)
    return webhook_event_from_api(data, event_type)


def parse_verified_webhook_event(
    *,
    payload: bytes | str,
    signature: str,
    secret: str,
    event_type: WebhookEventType | None = None,
) -> ParsedWebhookEvent:
    """Verify a PlexTrac webhook signature, then parse the event payload."""
    if not verify_signature(payload=payload, signature=signature, secret=secret):
        raise ValueError("Invalid PlexTrac webhook signature.")
    return parse_webhook_event(payload, event_type=event_type)


def _payload_dict(payload: bytes | str | JsonDict) -> JsonDict:
    if isinstance(payload, dict):
        return payload
    if isinstance(payload, bytes):
        payload = payload.decode()
    data = json.loads(payload)
    if not isinstance(data, dict):
        raise ValueError("PlexTrac webhook payload must be a JSON object.")
    return data
