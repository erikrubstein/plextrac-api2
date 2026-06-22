# Temporary API Review Methodology

This is a temporary working note for the group-by-group plextrac-api2 SDK review. Remove it when
the review pass is complete or when the methodology has been folded into permanent docs.

## Goal

Make the public SDK surface consistent before building larger CLI or MCP layers.

For each API group, confirm that:

- Function names are explicit, stable, and grouped by product area.
- Public dataclass fields are semantic Python `snake_case`, not raw PlexTrac keys.
- IDs are context-specific, such as `client_id`, `report_id`, `finding_id`, `asset_id`,
  `tenant_id`, `role_id`, and `benchmark_id`.
- `from_api()` maps raw PlexTrac response keys into refined Python names.
- `to_api()` maps refined Python names back to PlexTrac wire keys.
- Raw response data remains available where the SDK already preserves it.
- The SDK avoids duplicate aliases for the same concept unless compatibility requires them.
- Return types are typed where the structure is stable enough to justify it.

## Group Order

Review function groups alphabetically by module name, starting with:

1. `admin.py`
2. `affected_assets.py`
3. `analytics.py`
4. `assessments.py`
5. `assets.py`
6. `clients.py`
7. `content_library.py`
8. `files.py`
9. `findings.py`
10. `integrations.py`
11. `mailer.py`
12. `parser_actions.py`
13. `reports.py`
14. `runbooks.py`
15. `scheduler.py`
16. `substatus.py`
17. `templates.py`
18. `tenant.py`
19. `users.py`
20. `webhooks.py`

`auth.py` and `common.py` are support modules. Review them separately when auth/session/error
behavior is in scope.

## Per-Group Review Checklist

For each group:

1. Inventory endpoints from `AGENTS.md` and `src/plextrac_api/generated/endpoints.py`.
2. Inspect the public function module under `src/plextrac_api/functions/`.
3. Inspect matching types under `src/plextrac_api/types/`.
4. Compare function parameters against route path params, query params, and body fields.
5. Normalize public field names while preserving wire keys in `to_api()` / `from_api()`.
6. Check response models for ambiguous fields like `id`, `name`, `type`, `status`, and raw
   camelCase keys.
7. Add or refine dataclasses/enums where stable structure is known.
8. Keep public polished functions explicit: no public `**kwargs`, `Any`, or `JsonDict` returns.
9. Update tests for request shape, parsing, enum values, and exports.
10. Update README or AGENTS only when public behavior or review guidance changes.

## Live Test Methodology

Live tests are allowed, but they must be explicit and guarded. They should not become default unit
tests.

For each live probe:

- Prefer read-only endpoints first.
- Use existing demo/session helpers only when local credentials are already configured.
- Print structural summaries, statuses, and IDs created during the probe; do not print secrets or
  large customer payloads.
- Record whether the result confirms documented behavior, contradicts documentation, or remains
  inconclusive because of permissions or missing data.
- If behavior differs from documentation, prefer live behavior but note the source of the decision.

## Destructive Endpoint Rules

Destructive endpoints may be tested only against data created by the current test run.

Required flow:

1. Create a uniquely named test object with an obvious marker.
2. Store the returned ID locally in the script/run context.
3. Perform the destructive action only against that exact ID.
4. Verify the object was removed or changed as expected.
5. Clean up any remaining created test data.

Never delete, overwrite, assign, unassign, or bulk-modify tenant data discovered from list/search
endpoints unless it was created by the current probe and the ID is known with certainty.

## Test Expectations

Offline unit tests should remain deterministic:

- `to_api()` tests prove refined fields serialize to PlexTrac wire keys.
- `from_api()` tests prove raw PlexTrac response keys parse into semantic fields.
- Function tests prove path interpolation, params, body shape, and return typing.
- Export tests prove public types are available from `plextrac_api.types`.

Live tests should live in demos/scripts or ad hoc probes, not in `tests/unit`.

## Completion Criteria For A Group

A group pass is complete when:

- Naming has been reviewed and obvious inconsistencies are fixed.
- Stable request and response shapes are typed.
- Tests cover changed names and mappings.
- Live behavior has been checked where feasible.
- Destructive behavior, if tested, used only known-created data.
- `.venv/bin/python -m pytest tests/unit` passes.
- `.venv/bin/python -m ruff check .` passes.
- The review notes are clear enough to inform CLI/MCP design.
