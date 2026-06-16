# Authentication

The API supports either a static bearer token or username/password login.

```python
from plextrac_api.functions.auth import session_from_token

session = session_from_token(base_url="https://example.plextrac.com", token="jwt")
```

```python
from plextrac_api.functions.auth import create_session

session = create_session(
    base_url="https://example.plextrac.com",
    username="user@example.com",
    password="secret",
)
```

When credentials are provided, the SDK logs in through `/api/v1/authenticate`.
PlexTrac JWT tokens expire quickly, so authenticated SDK requests refresh the current token through
`/api/v1/token/refresh` before sending a request when the decoded JWT expires within five minutes.

If the token is already expired, the SDK raises an authentication error and callers should create a
new session. A `401` response is not treated as the normal refresh trigger when the JWT expiration
is known, because PlexTrac requires refresh before expiration.

For MFA or custom login flows, obtain a token outside the SDK and pass it as `token`.
