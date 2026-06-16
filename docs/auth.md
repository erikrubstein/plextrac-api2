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
If a request returns `401` and a refresh token is available, it attempts one refresh
through `/api/v1/token/refresh` and retries the original request once.

For MFA or custom login flows, obtain a token outside the SDK and pass it as `token`.
