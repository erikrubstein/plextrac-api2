import hashlib
import hmac

from plextrac_api.functions.webhooks import verify_signature


def test_verify_signature_accepts_prefixed_hmac_digest():
    payload = b'{"event":"created"}'
    secret = "secret"
    digest = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()

    assert verify_signature(payload=payload, signature=f"sha256={digest}", secret=secret)

