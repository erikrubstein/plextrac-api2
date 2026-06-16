# SDK Methodology

This document defines how this SDK should translate the documented PlexTrac API into a Python
package. When PlexTrac's documentation, generated names, or endpoint versions are awkward, these
rules describe the SDK shape we prefer.

## Goals

The SDK should feel organized, typed, and approachable. It should expose PlexTrac functionality
without becoming one enormous client object full of unrelated methods.

Primary goals:

- Keep the package close to PlexTrac's documented API groups.
- Prefer explicit functions and dataclasses over dynamic catch-all objects.
- Make common workflows pleasant without hiding the underlying HTTP API.
- Keep generated coverage useful, but treat hand-polished wrappers as the final SDK surface.

## Package Shape

Public API calls live in grouped function modules:

```text
plextrac_api.functions.clients
plextrac_api.functions.reports
plextrac_api.functions.findings
```

Types live beside those groups:

```text
plextrac_api.types.common
plextrac_api.types.clients
plextrac_api.types.reports
plextrac_api.types.findings
```

Rules:

- Do not create a single `PlexTrac` object with hundreds of methods.
- Pass `AuthSession` explicitly as the first argument to functions that call PlexTrac.
- Keep shared HTTP behavior, GraphQL behavior, and errors in `functions.common`.
- Keep cross-cutting dataclasses in `types.common`.
- Keep group-specific dataclasses in the matching `types.<group>` module.
- Keep reusable request-shaping types such as `Pagination`, `Sort`, and `Filter` in
  `types.common`.

## Endpoint Version Policy

The SDK should expose one preferred function per operation.

Rules:

- If PlexTrac documents multiple versions of the same operation, expose only the latest supported
  documented version.
- If an operation only exists as `v1`, keep it, but do not include `_v1` in the public function name.
- If an operation only exists as `v2`, keep it, but do not include `_v2` in the public function name.
- Version details belong in docstrings, endpoint coverage docs, and generated metadata, not in the
  normal function name.

Examples:

- `get_authenticated_user_v2` becomes `get_authenticated_user`.
- `import_client_assets_v2` becomes `import_client_assets`.
- `runbook_engagement_list_v2` becomes `runbook_engagement_list`.

## Naming Policy

Function names should be Pythonic and consistent, even when the source documentation is not.

Rules:

- Prefer action-oriented verbs: `list_`, `get_`, `create_`, `update_`, `delete_`, `import_`,
  `export_`.
- Preserve PlexTrac terminology when it is clear.
- Fix names when the documented name is misleading, inconsistent, misspelled, or too awkward for
  normal use.
- Prefer consistency inside a group over strict title-to-function mechanical conversion.
- Add generator overrides for intentional naming fixes so regenerated files stay stable.

Example:

- PlexTrac's `Available Tenant Users` operation is exposed as `list_available_tenant_users` because
  it returns a list and sits beside `list_client_users`.

## Types Policy

Typed wrappers should be explicit. A polished function should not rely on ambiguous `**kwargs`
inputs or `Any`/`JsonDict` outputs.

Rules:

- Define request dataclasses for structured request bodies when the shape is documented and reused.
- Define response dataclasses for documented response objects.
- Use concrete return types such as `Client`, `ClientPage`, `list[ClientUser]`, or
  `OperationResult`.
- Keep raw API payloads available on dataclasses when useful for forward compatibility.
- Use `JsonDict` internally for payload assembly when needed, but do not treat it as the desired
  public return type for polished wrappers.

Generated endpoint functions are allowed to use `**kwargs` and `Any` temporarily. They exist to
preserve broad coverage while individual groups are polished.

## Generated vs Polished Functions

The SDK currently has two layers:

- Generated endpoint functions provide broad coverage from the PlexTrac Postman collection.
- Hand-written functions provide the desired long-term interface for high-value groups.

Generated functions should be considered scaffolding. As a group is polished, replace ambiguous
generated-style wrappers with explicit signatures and typed returns.

The `clients` and `reports` groups are the current models for polished groups:

- explicit function arguments
- concrete return types
- group-specific dataclasses
- canonical endpoint version only
- naming fixes where needed

## REST, GraphQL, And Webhooks

REST is the primary SDK surface.

GraphQL policy:

- Expose documented GraphQL operations when they exist.
- Keep GraphQL mostly raw/generated until a real workflow justifies polished wrappers.
- Do not assume GraphQL is a complete replacement for REST.

Webhook policy:

- Webhooks are inbound events, not SDK calls to PlexTrac.
- Keep receiver-side helpers such as signature verification.
- Defer broader webhook modeling until there is a concrete event-driven workflow.

## Compatibility Policy

This SDK prioritizes a clean Python interface over mirroring every historical PlexTrac API variant.

Rules:

- Do not expose deprecated or superseded versions solely for completeness.
- Keep raw request helpers available for edge cases.
- When the SDK intentionally renames or collapses an operation, document that decision in the
  generator, endpoint coverage, or this methodology.

## Implementation Checklist For A Group

When polishing an API group:

1. Review the documented endpoints and response examples.
2. Identify duplicate versions and select the latest supported endpoint per operation.
3. Choose consistent Python function names.
4. Add any required generator naming overrides.
5. Define shared dataclasses in `types.common` only when they are cross-cutting.
6. Define group-specific dataclasses in `types.<group>`.
7. Replace ambiguous `**kwargs` wrappers with explicit function arguments.
8. Replace `Any`/`JsonDict` public returns with concrete return types.
9. Update endpoint coverage and docs.
10. Add tests for request shape, response parsing, and naming regressions.
