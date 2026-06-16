# PlexTrac Python API Roadmap

Last reviewed: 2026-06-15

## Direction

This project should follow the same broad organization as the Monarch API project:

- `plextrac_api.functions.*` contains grouped API functions.
- `plextrac_api.types.*` contains dataclass types.
- `AuthSession` is passed explicitly into every function that calls PlexTrac.
- There is no single client object with hundreds of methods.

Example:

```python
from plextrac_api.functions.auth import create_session
from plextrac_api.functions import clients, reports, findings

session = create_session(
    base_url="https://example.plextrac.com",
    username="user@example.com",
    password="secret",
)

client_page = clients.list_clients(session)
report = reports.get_report(session, client_id="client-id", report_id="report-id")
finding = findings.get(session, clientId="client-id", reportId="report-id", findingId="finding-id")
```

## Current Shape

```text
src/plextrac_api/
  functions/
    auth.py
    common.py
    clients.py
    reports.py
    findings.py
    ...
  types/
    auth.py
    common.py
    clients.py
    reports.py
    findings.py
    assets.py
    evidence.py
  generated/
    endpoints.py
```

The generated function modules are based on the PlexTrac Postman collection snapshot and expose
357 supported endpoint functions after collapsing duplicate versioned operations to the latest
documented version. The hand-written types currently cover the documented common object structures:
clients, reports, findings, assets, affected assets, evidence, and shared supporting types.

## Design Rules

The durable SDK design rules live in [docs/methodology.md](docs/methodology.md). In short:

1. Prefer grouped plain functions over a single giant client object.
2. Pass `AuthSession` explicitly.
3. Expose only the latest supported documented version for each operation.
4. Fix naming inconsistencies when it makes the Python SDK clearer.
5. Replace generated `**kwargs`/`Any` wrappers with explicit typed functions as groups are polished.

## Next Pass

1. Add live integration test configuration.
2. Validate real PlexTrac auth and refresh response shapes.
3. Polish the next high-value generated groups with explicit signatures and return types:
   - `findings`
   - `assets`
4. Add upload/download helpers for files, findings imports, and asset imports.
5. Add pagination helpers after observing real endpoint response shapes.
6. Add endpoint generator `--fetch` support so the Postman collection can be refreshed directly.

## GraphQL Policy

REST remains the primary integration surface. GraphQL is still exposed because PlexTrac documents
GraphQL operations, especially Runbooks, but it should remain a raw/generated capability unless a
real workflow requires hand-polished wrappers.

Current GraphQL count in the generated snapshot:

- `graph_ql_queries`: 1 operation
- `graph_ql_mutations`: 2 operations
- `runbooks`: 60 GraphQL operations

## Webhooks Policy

Webhook event examples are not outbound API calls from this package to PlexTrac. Keep receiver-side
helpers, such as HMAC signature verification, but defer broader webhook polish until there is a
concrete event-driven workflow.

## Release Criteria

- Unit tests pass without PlexTrac credentials.
- Ruff passes.
- Package installs from `pyproject.toml`.
- Common dataclass types are documented and tested.
- Generated function modules can be refreshed from the endpoint snapshot.
