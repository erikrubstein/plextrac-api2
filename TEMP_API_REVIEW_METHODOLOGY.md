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

Each group is reviewed in three separate user-prompted steps. Do not advance from one step to the
next until the user asks for it.

### Step 1: Naming And Schemas

For each group, first perform a static naming and schema review:

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

### Step 2: Non-Mutating Live Tests

After naming and schema changes are reviewed and tested offline, run live non-mutating probes only
when the user prompts for this step.

- Prefer true read-only endpoints.
- For POST endpoints that are semantically reads/searches, use minimal payloads and avoid broad
  scans when a narrower fixture can be discovered.
- Print structural summaries, counts, response shapes, and whether typed parsing succeeds.
- Stop broad discovery scans if they become slow or noisy; record the result as inconclusive rather
  than hammering the tenant.
- Do not create, update, delete, import, assign, or bulk-modify data in this step.

### Step 3: Careful Mutating Live Tests

Run mutating tests only after the user explicitly prompts for this step.

- Create uniquely named disposable data with an obvious marker.
- Exercise mutating endpoints only against IDs created in the current probe.
- Verify each mutation through a read-back endpoint.
- Clean up in reverse dependency order with marker verification before each delete.
- Run a read-only marker audit afterward to confirm no created artifacts remain.

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

## Group Progress Notes

- `auth.py`: Steps 1-3 completed locally. Public auth helpers include login, token-backed session
  creation, refresh, save, and load. `AuthSession` preserves `tenant_id` from auth/refresh
  responses. Live tests covered stored-session loading, explicit token refresh, save/load, and a
  fresh credential login when credentials were available. MFA QR generation and activation were not
  run because they can alter the current user's MFA setup.
- `admin.py`: Steps 1-3 completed and committed.
- `affected_assets.py`: Steps 1-3 completed and committed.
- `analytics.py`: Steps 1-3 completed and committed. Removed the documented but unavailable
  age-of-open-findings trend endpoint from the polished public surface.
- `assessments.py`: Steps 1-3 completed locally. Live testing confirmed that client assessment
  creation requires an explicit `answers: []` payload even when no answers are supplied, question
  creation rejects `order`, question update requires `order`, and questionnaire update currently
  returns a backend 500 even with the only validation-accepted `assessment_title`/`framework_id`
  payload. The redundant v1 `list_client_assessments_legacy` operation is documented in endpoint
  inventory but not exposed in the polished API; use the v2 `list_client_assessments` wrapper.
  All disposable live artifacts were deleted and marker audits were empty.
- `assets.py`: Steps 1-3 completed locally. Public asset models now use `asset_type` instead of
  the ambiguous `type`, parse additional raw camelCase response keys, and keep the deprecated v1
  client asset list out of the latest generated inventory. The scanner-output endpoint remains
  documented in assets but is not exposed there; use `findings.get_scanner_output`. Live testing
  confirmed tenant/client/report asset reads, get, create, update, single delete, bulk delete, and
  import queueing. The CSV import job did not create a visible marked asset during delayed audits;
  all created direct assets were deleted and marker audits were empty.
- `clients.py`: Steps 1-3 completed locally. Public client input/response models now use `poc`
  and `poc_email`, `ClientPageLimit` is constrained to the documented list-client values
  `[5, 25, 50, 100]`, and `Client.from_api()` / `ClientCreateResult.from_api()` tolerate
  additional raw ID key variants while exposing semantic Python fields. Live testing confirmed
  list clients, tenant clients, get client, client users, available tenant users, default client
  finding pagination, and filtered `ALL` client finding pagination. It also found that tenant
  client list records can wrap the client object under `data`, so `Client.from_api()` now unwraps
  that shape while preserving raw data. Careful mutating tests confirmed create, update, add logo,
  delete logo, and delete against a marked disposable client. Client user assign/bulk assign/remove
  returned `Unauthorized` for this live account, so those remain permission-limited/inconclusive.
  All disposable live artifacts were deleted and marker audits were empty. The documented client
  asset endpoint remains owned by the `assets` group.
- `content_library.py`: Steps 1-3 completed locally. Public response models now unwrap nested
  `data` response objects, parse additional ID key variants, map narrative section `label` to
  Python `title`, and parse user `first`/`last` name keys. Live testing found NarrativesDB section
  and user list endpoints require default pagination, so those wrappers now send
  `{"pagination": {"offset": 0, "limit": 25}}` by default. Live testing also found narrative
  section create requires caller-provided `section_id` as wire `id` plus `repositoryId`, writeup
  create/update expects `repositoryId`, and v1 writeup get/update/delete paths require numeric
  `doc_id`. Bulk writeup delete expects string writeup IDs under `writeups`. Repository creation
  endpoints returned `Unauthorized` for this account, so repository create/update/delete remain
  permission-limited. Disposable section and writeup mutations against existing repositories were
  created, updated/deleted where supported, and marker audits were empty. The documented
  `copy_section_to_narrative_repository` endpoint rejected tested payloads and is not exposed in
  the polished module.
- `files.py`: Steps 1-3 completed locally. Public `ArtifactRelation` now uses semantic
  `object_id` while serializing to PlexTrac wire key `id`; live testing confirmed relation IDs
  must be sent as strings. Artifact and upload response parsers tolerate nested `data` wrappers
  and additional raw ID/url key variants. Live testing confirmed client-scoped artifact listing,
  disposable artifact upload, readback, download, delete, and marker audit. Tenant image upload was
  skipped because the backend rejects arbitrary scopes and no known valid disposable scope was
  configured.
- `findings.py`: Steps 1-3 completed locally. Public finding result/object fields now expose
  `finding_id` instead of PlexTrac's raw `flaw_id`, finding sort/filter enums use
  `FINDING_ID` while preserving the documented `flawId`/`flaw_id` wire values, and evidence/import
  helper types use semantic `evidence_id`, `import_id`, and `code_sample_id` names. Live testing
  found report findings pagination rejects the documented `99999` limit and only accepts
  `[1, 10, 50, 100]`, so `FindingPageLimit` intentionally does not expose `ALL`; the default
  remains 10. Live testing also found finding `fields` are object maps keyed by field name rather
  than lists, scanner output returns an empty JSON list when no scanner output exists, status
  updates require singular `comment`, bulk evidence requires `id`/`caption`/`code`/`assets`, and
  bulk finding delete uses the v1 key `flaws`. The metadata bulk-update and bulk status-update
  endpoints rejected their documented update fields or returned backend 500s, so they are not
  exposed in the polished module. The single evidence update endpoint requires GUID-style asset IDs,
  while this tenant's client and affected asset IDs are CUIDs, so it is not exposed; use the
  successfully live-tested bulk evidence endpoint. The deprecated bulk evidence read endpoint
  remains intentionally unexposed; use `get_scanner_output` for that documented workflow. Careful
  mutating tests created and deleted marked disposable reports, assets, findings, status updates,
  and bulk evidence; marker audits were empty.
- `integrations.py`: Steps 1-3 completed locally. Public Tenable tag responses now expose
  `tag_id` instead of generic `id`, and integration configuration functions/types now use
  `configuration_id` instead of `config_id` while preserving PlexTrac `configId` parsing. The
  documented `IntegrationConfigurationType.COBALT` wire value remains PlexTrac's misspelled
  `"Colbalt"`. Live non-mutating tests confirmed the legacy Jira projects endpoint returns an
  empty list for this tenant. Integration configurations returned `Unauthorized`, Tenable tags and
  tested tenant product integration lookups returned `Not Found`, and mutating Jira connection /
  integration configuration creation returned `Unauthorized`; no disposable integration artifacts
  were created.
- `mailer.py`: Steps 1-3 completed locally. Public upsert payloads now use
  `EmailTemplateInput` for the documented `subject`/`body` request shape. Live non-mutating tests
  for listing mailer templates and reading the forgotten-password template returned `Unauthorized`
  for this account. The only mutating endpoint updates the tenant's real `FORGOTTEN_PASSWORD`
  email template and has no disposable create/delete path; because the account also could not read
  the current template for safe restoration, live mutation was intentionally skipped.
- `parser_actions.py`: Steps 1-3 completed locally. Public parser responses now expose
  `parser_id` instead of raw `source`, and parser action request/response models expose
  `action_id` instead of generic `id` while preserving PlexTrac wire keys. Live non-mutating tests
  returned `Unauthorized` at the tenant parser list endpoint for this account. Mutating tests were
  intentionally skipped: parser plugin action enablement is tenant-wide with no read endpoint in
  this group for restoration, parser action creation/import have no documented delete path, and
  update/bulk update would alter existing tenant parser mappings.
- `reports.py`: Steps 1-3 completed locally. Public report response models now map raw report
  `id` values to `report_id`, report list `cuid` values to `cuid`, narrative raw `id` values to
  `narrative_id`, and exhibit raw `id` values to `exhibit_id`. Live testing confirmed report list
  pagination accepts `[5, 10, 25, 50, 100, 1000]`, and `.ptrac` export returns structured JSON
  rather than bytes, so `export_report_to_ptrac` now returns `ReportPtracExport`. Mutating tests
  created, updated, search/replaced, bulk-tagged, bulk-statused, reviewer-assigned, exported,
  imported, bulk-deleted, and single-deleted marked disposable reports only. Word export worked on
  the disposable report; PDF export returned a PlexTrac backend error for the empty report. Final
  marker audits were empty.
