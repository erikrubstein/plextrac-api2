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
- Avoid Python built-in names for public parameters when a clear SDK name exists. Keep the
  documented PlexTrac field name at the wire boundary.

Example:

- PlexTrac's `Available Tenant Users` operation is exposed as `list_available_tenant_users` because
  it returns a list and sits beside `list_client_users`.

## Types Policy

Typed wrappers should be explicit. A polished function should not rely on ambiguous `**kwargs`
inputs or `Any`/`JsonDict` outputs.

Rules:

- Default to explicit structures, schemas, and expected values. Treat looseness as something that
  must be justified by the PlexTrac docs or observed API behavior, not as a convenience.
- Define request dataclasses for structured request bodies when the shape is documented and reused.
- Name reusable request dataclasses with an `Input` suffix when they represent create/update-style
  object payloads, such as `ClientInput`, `ReportInput`, and `FindingInput`.
- Define response dataclasses for documented response objects.
- Do not define request/input dataclasses that are used by only one public function. Use explicit
  function parameters for single-use request bodies.
- When a request/input dataclass is reused by multiple public functions, require that dataclass in
  those functions and do not also offer explicit keyword arguments as an alternative.
- Use concrete return types such as `Client`, `ClientPage`, `list[ClientUser]`, or
  `OperationResult`.
- Use `OperationResult` only for generic operation responses. If an endpoint returns unique
  information, define a dedicated result type that preserves it.
- Do not collapse explicit response fields into vague generic fields. For example, a response
  field named `report_id` should become `ReportCreateResult.report_id`, not
  `OperationResult.id`.
- Use explicit identifier names on domain models when PlexTrac documents them. For example,
  prefer `Client.client_id`, `Report.report_id`, and `Finding.flaw_id` over a generic `id`
  property. Keep separate CUID-style document identifiers in a `cuid` field when present.
- Keep raw API payloads available on response dataclasses when useful for debugging or forward
  compatibility, but never use `raw` to construct polished request payloads.
- Do not add public `extra` escape-hatch fields to polished request types or functions. Use the raw
  REST helper for unsupported payload keys instead.
- Do not expose generic `Sort` or `Filter` on polished functions when the endpoint documents field
  names. Define group-specific sort/filter field enums.
- If an endpoint accepts an object or list whose item shape is documented, model that item shape
  with a dataclass instead of `dict`.
- If an endpoint field is truly open-ended, keep the narrowest accurate type and document why in
  the type or function review notes. Examples include service-defined upload form fields or tenant
  custom role codes.
- Use `Enum` for documented finite value sets instead of `Literal` or plain `str`.
- Give enum members readable, unabbreviated names even when the API value is abbreviated.
- Serialize enums back to PlexTrac's documented wire values at the API boundary.
- Use `JsonDict` internally for payload assembly when needed, but do not treat it as the desired
  public return type for polished wrappers.

Examples:

- `SortOrder.ASCENDING` serializes to `"ASC"`.
- `ReportStatus.READY_FOR_REVIEW` serializes to `"Ready For Review"`.
- `ReportReplaceResult` is preferred over `OperationResult` for report text replacement because the
  response includes a meaningful `data` boolean.

Generated endpoint functions are allowed to use `**kwargs` and `Any` temporarily. They exist to
preserve broad coverage while individual groups are polished.

## Formatting Policy

Polished public function signatures should be easy to scan as typed API declarations.

Rules:

- Use multiline function signatures for polished public functions, even when the signature would
  fit on one line.
- Put one parameter per line, including `session`.
- Put `*` on its own line when keyword-only arguments are used.
- Put the closing parenthesis and return annotation on their own line.
- Private helpers may stay compact when their signatures are short and obvious.

## Docstring Policy

Polished functions should include concise docstrings that describe the operation from the SDK
user's point of view.

Rules:

- Put docstrings inside the function body, immediately after the function definition.
- Keep docstrings short and practical.
- Do not use docstrings to restate every parameter when type hints already make the signature clear.
- Mention version or transport details only when they are important to the user's decision.

## Generated vs Polished Functions

The SDK currently has two layers:

- Generated endpoint functions provide broad coverage from the PlexTrac Postman collection.
- Hand-written functions provide the desired long-term interface for high-value groups.

Generated functions should be considered scaffolding. As a group is polished, replace ambiguous
generated-style wrappers with explicit signatures and typed returns.

The `clients`, `reports`, `findings`, `assets`, `affected_assets`, `files`, `mailer`, `substatus`,
`analytics`, `tenant`, `templates`, `integrations`, `parser_actions`, and `scheduler` groups are the current models for polished groups:

- explicit function arguments
- reusable input dataclasses only when shared across functions
- concrete return types
- group-specific dataclasses
- documented finite value sets represented as enums
- documented sort/filter fields represented as enums
- canonical endpoint version only
- naming fixes where needed
- multiline public function signatures
- concise docstrings

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
7. Use explicit function parameters for single-use request bodies.
8. Use request dataclasses only when the same input type is reused across multiple public functions.
9. Do not provide both a request dataclass and explicit keyword alternatives for the same function.
10. Replace ambiguous `**kwargs` wrappers with explicit function arguments.
11. Replace `Any`/`JsonDict` public returns with concrete return types.
12. Replace documented finite string sets with enums that use readable member names.
13. Replace documented sort/filter field strings with group-specific enums.
14. Replace documented nested dictionaries with dataclasses.
15. Use dedicated result types instead of `OperationResult` when endpoint responses contain unique
    information.
16. Format public function signatures across multiple lines.
17. Add concise docstrings to polished functions.
18. Update endpoint coverage and docs.
19. Add tests for request shape, response parsing, enum serialization, and naming regressions.
