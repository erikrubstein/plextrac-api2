# Normal Group Methodology Audit Results

This document records the audit results for the polished normal API groups. The plan lives in
`docs/normal-group-methodology-audit-plan.md`.

## Step 1: Automated Checks

Scanned 19 polished normal groups and 331 public functions with an AST-based script.

### Pass

- Missing function modules: 0
- Public functions with `**kwargs`: 0
- Public functions with version suffixes: 0
- Public `extra` escape hatches: 0
- Polished groups still listed as generated: 0
- Polished groups missing from `HAND_WRITTEN_FUNCTION_GROUPS`: 0
- Generator parse errors: 0

### Needs Cleanup

- `src/plextrac_api/functions/affected_assets.py:68`
  - `bulk_get_affected_asset_statuses` returns `dict[str, AffectedAssetStatusUpdate]`.
  - This is typed, but it still violates the automated plan's no-public-`dict` check.
- `src/plextrac_api/types/runbooks.py:61`
  - `RunbookUserInput` is used by only one public function:
    `update_runbook_repository_user`.
- `src/plextrac_api/types/runbooks.py:251`
  - `RunbookAssetInput` is used by only one public function:
    `create_runbook_engagement_procedure_asset`.
- `src/plextrac_api/types/runbooks.py:27`
  - `RunbookTag` is public but not exported from `plextrac_api.types`.

### Review Candidates

- `src/plextrac_api/types/affected_assets.py` does not exist.
  - The affected-assets functions currently reuse affected-asset types from `types.assets`.
  - Decide whether this should remain an intentional exception or move group-specific types into a
    dedicated `types.affected_assets` module.
- `src/plextrac_api/functions/admin.py:50`
  - `update_tenant_authentication_provider_configuration(provider: str)` was a finite-value
    candidate.
  - Resolved after live verification with `AuthenticationProviderName`.
- Naming review candidates:
  - `src/plextrac_api/functions/reports.py:28` `count_report_search_occurrences`
  - `src/plextrac_api/functions/findings.py:25` `request_presigned_upload_url`
  - `src/plextrac_api/functions/mailer.py:34` `upsert_email_template`
  - `src/plextrac_api/functions/analytics.py:94` `retrieve_analytics_trends_opened_closed`
  - `src/plextrac_api/functions/analytics.py:108` `retrieve_analytics_trends_from_creation_to_close`
  - `src/plextrac_api/functions/analytics.py:122` `retrieve_analytics_trends_age_of_open_findings`
  - `src/plextrac_api/functions/analytics.py:136` `retrieve_analytics_trends_slas`
  - `src/plextrac_api/functions/analytics.py:150` `retrieve_analytics_trends_sla_findings`
  - `src/plextrac_api/functions/integrations.py:34` `upsert_integration`
  - `src/plextrac_api/functions/integrations.py:70` `sync_tenable_io_tags`
  - `src/plextrac_api/functions/integrations.py:123` `set_jira_projects`
  - `src/plextrac_api/functions/integrations.py:164` `reset_jira_issue_mappings`
  - `src/plextrac_api/functions/integrations.py:223` `unlink_jira_ticket_from_findings`
  - `src/plextrac_api/functions/parser_actions.py:19` `set_parser_plugin_actions_enabled`
  - `src/plextrac_api/functions/scheduler.py:175` `approve_engagement_schedule_event`
  - `src/plextrac_api/functions/users.py:105` `change_password`
  - `src/plextrac_api/functions/users.py:121` `forgot_password`
  - `src/plextrac_api/functions/users.py:137` `reset_user_password`
  - `src/plextrac_api/functions/users.py:153` `set_mfa_token`
  - `src/plextrac_api/functions/users.py:185` `set_user_disabled`
  - `src/plextrac_api/functions/users.py:219` `mark_user_notifications_read`
  - `src/plextrac_api/functions/admin.py:111` `upsert_saml_configuration`
  - `src/plextrac_api/functions/admin.py:347` `get_tenant_tag_by_name`
  - `src/plextrac_api/functions/assessments.py:93` `update_question_order`
- Nested input dataclass review candidates:
  - `src/plextrac_api/types/integrations.py:110` `JiraIssueMappingInput`
  - `src/plextrac_api/types/integrations.py:126` `JiraIssueTypeMappingInput`
  - `src/plextrac_api/types/users.py:54` `TenantUserInput`
  - `src/plextrac_api/types/content_library.py:15` `ContentLibraryUserInput`
  - `src/plextrac_api/types/runbooks.py:177` `RunbookExecutionStepInput`

### Notes

- The naming candidates are mechanical findings based on verb prefixes. Some may be acceptable
  domain verbs, but each should be reviewed against the methodology.
- The nested input dataclass candidates are not direct public function parameters. Some may be
  valid nested request item types rather than methodology violations.

## Step 2: Manual Review

Reviewed the polished normal groups against the methodology using the automated output as a guide.

### Pass

- All 331 polished public functions have docstrings.
- All polished public function signatures use multiline formatting.
- No polished public functions expose `**kwargs`.
- No polished public functions expose `_v1`, `_v2`, or similar version suffixes.
- No polished public request types expose `extra` payload escape hatches.
- `OperationResult` usage is mostly limited to generic update, delete, import, bulk-action, toggle,
  and trigger-style endpoints.
- Documented sort, filter, status, source, and template values are generally modeled with enums.
- Public `JsonDict` usage is mostly confined to internal helpers, `to_api`, `from_api`, and `raw`
  response fields.

### Resolved Cleanup Findings

- `bulk_get_affected_asset_statuses` returned `dict[str, AffectedAssetStatusUpdate]`.
  - Resolved with `AffectedAssetStatusMap`.
- `src/plextrac_api/functions/runbooks.py:122`
  - `update_runbook_engagement_procedure_asset` exposed both `asset` and `input` parameters for
    `RunbookAssetInput`.
  - Resolved by removing the public `input` parameter.
- `src/plextrac_api/functions/runbooks.py:508`
  - `update_runbook_repository_user` passed `"data": user` into GraphQL variables instead of
    `user.to_api()`.
  - Resolved by serializing the input dataclass.
- `src/plextrac_api/types/runbooks.py:27`
  - `RunbookTag` was public and used by public response types, but it was not exported from
    `plextrac_api.types`.
  - Resolved by exporting it.
- Analytics trend function names were noun-first.
  - Resolved by renaming them with the `retrieve_` verb prefix.
- `save_integration` was less precise than the rest of the SDK naming.
  - Resolved as `upsert_integration`.
- `find_tenant_tag` did not clearly communicate exact-name lookup.
  - Resolved as `get_tenant_tag_by_name`.
- `change_question_order` was less consistent than other update-style functions.
  - Resolved as `update_question_order`.

### Intentional Exceptions

- `RunbookUserInput` is not actually a single-use input type.
  - It is used for engagement procedure operators, repository user creation, and repository user
    updates. The automated step missed list item usage.
- `RunbookAssetInput` is not actually a single-use input type.
  - It is used directly and as nested list input in runbook procedure/asset workflows.
- The affected-asset types currently live in `types.assets`.
  - This is defensible because findings also use `AffectedAsset` as a nested response model.
  - A dedicated `types.affected_assets` module may still be cleaner later, but this is not an
    immediate correctness issue.
- Parser names remain plain strings.
  - They are tenant/service-defined values returned by `list_tenant_parsers`, not a verified fixed
    enum.
- Content-library permission levels remain plain strings.
  - They may be finite, but the audit did not verify an exhaustive documented value list.
- Generic `Sort` and `Filter` remain in `types.common`, but polished functions are not exposing
  them directly.

### Follow-up Candidates

- Admin authentication providers were live-verified and modeled as `AuthenticationProviderName`.
- Verify whether `list_client_assessments(sort: int = 0)` has a documented finite value set or
  should receive a named enum/newtype.
- Verify whether generic integration `product: str` and `settings: JsonDict` can be tightened.
  - If PlexTrac documents product-specific schemas, model those explicitly.
  - If products/settings are intentionally open-ended, document that exception near the type or
    function.
- Consider whether `request_presigned_upload_url` should become `create_presigned_upload_url` or
  `get_presigned_upload_url`.
  - The current name is understandable, but it does not start with one of the common SDK verbs.
- Consider whether user workflow names should be polished further:
  - `forgot_password`
  - `set_mfa_token`
  - `set_user_disabled`

## Step 3: Test Coverage Review

Reviewed the focused unit tests for polished normal groups and ran the current test suite.

Command:

```bash
.venv/bin/python -m pytest tests/unit
```

Result:

- 70 passed

### Coverage Matrix

Each polished normal group has at least one function-level test and at least one type-level test.

| Group | Function-Level Tests | Type-Level Tests |
| --- | ---: | ---: |
| `clients` | 2 direct group tests plus shared request/auth behavior tests | 2 direct type tests plus shared identifier/result checks |
| `reports` | 3 | 2 direct type tests plus shared result/content-library coverage |
| `findings` | 2 | 2 direct type tests plus shared nested-type coverage |
| `assets` | 2 | 3 direct type tests plus affected-asset nested coverage |
| `affected_assets` | 2 | 2 |
| `files` | 2 | 1 |
| `mailer` | 1 | 1 |
| `substatus` | 1 | 1 |
| `analytics` | 1 | 1 |
| `tenant` | 1 | 1 direct type test plus shared nested-type coverage |
| `templates` | 2 | 1 direct type test plus mailer template enum coverage |
| `integrations` | 1 | 1 |
| `parser_actions` | 1 | 1 |
| `scheduler` | 1 | 1 |
| `users` | 1 | 1 |
| `admin` | 4 | 1 |
| `assessments` | 3 | 2 direct type tests plus report parsing coverage |
| `content_library` | 3 | 1 |
| `runbooks` | 3 | 1 |

### Pass

- The test suite is currently green.
- Every polished normal group has at least one function behavior test.
- Every polished normal group has at least one type parsing or serialization test.
- Request-shape coverage exists across all polished groups at least at the representative workflow
  level.
- Response parsing coverage exists across all polished groups at least at the representative model
  level.
- Enum serialization coverage exists for the groups that currently define the most important enum
  inputs.
- Upload/form-data workflows have focused tests for files, reports, templates, content library,
  runbooks, and files.
- Runbook GraphQL variable-shape coverage exists for repository creation and GraphQL list parsing.
- Shared auth/request behavior is covered by request error and token-refresh tests.

### Resolved Test Additions

- Added tests for the step 2 runbook issues:
  - `update_runbook_engagement_procedure_asset` should have a variable-shape test proving there is
    only one asset payload path and no public `input` parameter.
  - `update_runbook_repository_user` should have a variable-shape test proving `RunbookUserInput`
    is serialized with `.to_api()`.
- Added tests for replacing the `bulk_get_affected_asset_statuses` public `dict` return:
  - response parsing should assert the new result type and map access behavior.
- Added export/registry coverage for `RunbookTag`.
- Added naming regression tests for renamed functions from step 2.

### Follow-up Candidates

- Broaden per-group coverage beyond representative endpoints over time.
  - Current coverage is good for methodology drift detection, but it is not exhaustive endpoint
    coverage.
- Add tests for operation-result response variants where live PlexTrac examples show meaningful
  differences.
- Add tests around intentional string-valued inputs if they remain intentionally open-ended:
  - admin authentication provider strings
  - content-library permission levels
  - generic integration product/settings
  - parser names
- Add response parsing tests for more list/detail variants in large groups such as `runbooks`,
  `content_library`, `admin`, and `assessments`.

## Step 4: Consolidated Audit Output

This section converts the audit findings into the queue we should use for cleanup work.

### Pass

- The polished normal groups are broadly aligned with the methodology.
- The current public surface has no `**kwargs`, no version suffixes, no public `extra` escape
  hatches, and no missing docstrings.
- Function signatures are consistently multiline.
- The generator configuration correctly treats polished normal groups as hand-written.
- The current unit suite is green with 72 passing tests.
- Every polished normal group has representative function-level and type-level coverage.

### Implemented Cleanup

1. Runbook request-shape issues are fixed.
   - Removed the alternate `input` parameter from `update_runbook_engagement_procedure_asset`.
   - Serialized `RunbookUserInput` with `.to_api()` in `update_runbook_repository_user`.
   - Added focused GraphQL variable-shape tests for both changes.
2. `RunbookTag` is exported.
   - Added it to `plextrac_api.types`.
   - Added registry/type coverage.
3. The affected-assets public `dict` return is replaced.
   - Added `AffectedAssetStatusMap` for `bulk_get_affected_asset_statuses`.
   - Preserved keyed status access without exposing a bare `dict` return annotation.
   - Updated tests for the new result type.
4. Confirmed naming issues are polished.
   - Renamed analytics trend functions to verb-first names.
   - Renamed `save_integration` to `upsert_integration`.
   - Renamed `find_tenant_tag` to `get_tenant_tag_by_name`.
   - Renamed `change_question_order` to `update_question_order`.
   - Updated generator naming overrides, generated metadata, endpoint coverage docs, and naming
     regression tests.

### Intentional Exceptions To Keep

- `RunbookUserInput` and `RunbookAssetInput` are valid reusable input types.
- Affected-asset models can remain in `types.assets` for now because they are shared with findings.
- Parser names can remain plain strings because they are tenant/service-defined.
- Content-library permission levels can remain plain strings until an exhaustive value set is
  verified.
- Generic `Sort` and `Filter` can remain in `types.common` because polished functions do not expose
  them directly.

### Verification Queue

These should be researched or live-tested before changing public types:

1. Assessment client-list `sort`.
   - Determine whether `sort: int = 0` has named finite values.
2. Generic integrations.
   - Determine whether `product` and `settings` are intentionally open-ended or documented per
     product.
3. User workflow names.
   - Decide whether `forgot_password`, `set_mfa_token`, and `set_user_disabled` should be renamed
     now or left as acceptable workflow verbs.
4. Presigned upload naming.
   - Decide whether `request_presigned_upload_url` should become `create_presigned_upload_url` or
     stay as-is.

### Suggested Commit Boundaries

- Commit 1: runbook request-shape fixes and tests.
- Commit 2: `RunbookTag` export and registry test.
- Commit 3: affected-assets result type and tests.
- Commit 4: naming polish with generator/docs/test updates.
- Commit 5: verified enum/type tightening, only after the verification queue is resolved.

## Step 5: Implementation Pass

Implemented the actionable cleanup recommendations from the audit.

### Pass

- Runbook request-shape issues are fixed and covered by tests.
- `RunbookTag` is exported and covered by type tests.
- `bulk_get_affected_asset_statuses` now returns `AffectedAssetStatusMap` instead of a bare
  `dict`.
- Confirmed naming fixes are applied in function modules, generator overrides, generated endpoint
  metadata, endpoint coverage docs, and regression tests.
- Live-verified authentication provider values are modeled as `AuthenticationProviderName`.
- The follow-up automated scan reports no `**kwargs`, no ambiguous public return annotations, and no
  public version suffixes across polished normal groups.
- `count_report_search_occurrences` remains as an intentional naming exception because `count_` is
  a precise action verb for that operation.

### Verification

Command:

```bash
.venv/bin/python -m pytest tests/unit
```

Result:

- 72 passed

### Still Deferred

- Assessment sort values, generic integration product/settings types, and intentionally open-ended
  strings still require documentation, broader permissions, or clearer live-response evidence before
  tightening.

## Step 6: Live Read-Only Verification

Ran non-destructive live probes using the git-ignored demo session.

### Verified And Implemented

- `/api/v2/authenticate/providers` returned:
  - `plextrac`
  - `okta`
  - `google`
  - `azure`
  - `openid_connect`
- Added shared `AuthenticationProviderName` in `types.common` with those values.
- Updated admin authentication-provider update functions to accept `AuthenticationProviderName`.
- Updated user profile update serialization to use the same shared enum.
- Updated authentication-provider response types to parse the enum while preserving raw payloads.

### Observed But Not Tightened

- `list_client_assessments(sort=...)` requires a numeric `sort` value.
- Live read-only calls accepted several numeric values, but did not reveal stable names or an
  exhaustive value set.
- The SDK should keep `sort: int = 0` until PlexTrac documentation or stronger evidence maps the
  numeric values to named semantics.

### Blocked By Permissions

- Tenant authentication provider configuration returned unauthorized for this account.
- Tenant users, tenant parser actions, and integration configuration endpoints also returned
  unauthorized or not found.
- Generic integration `product` and `settings` should remain open-ended until a tenant with the
  relevant integration/admin permissions can provide representative read-only responses.
