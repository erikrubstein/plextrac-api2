# Normal Group Methodology Audit Plan

This plan defines how to audit the polished normal API groups before moving on to the deferred
groups. It is a working checklist, not the audit result.

## Scope

Audit the polished normal groups:

- `clients`
- `reports`
- `findings`
- `assets`
- `affected_assets`
- `files`
- `mailer`
- `substatus`
- `analytics`
- `tenant`
- `templates`
- `integrations`
- `parser_actions`
- `scheduler`
- `users`
- `admin`
- `assessments`
- `content_library`
- `runbooks`

Defer these groups:

- `auth`
- `webhooks`
- `graph_ql_queries`
- `graph_ql_mutations`
- `QA Workflow`

## Automated Checks

Use AST-based scans where possible for:

- public functions with `**kwargs`
- public functions returning `Any`, `JsonDict`, `dict`, or no return annotation
- public parameters typed as bare `str` where the parameter name suggests a finite value set, such
  as `status`, `type`, `source`, `order`, `sort`, `role`, `scope`, `mode`, or `provider`
- function names ending in `_v1`, `_v2`, `_v3`, or similar version suffixes
- public function names that do not start with an approved action verb
- request/input dataclasses used by only one public function
- public request dataclasses or public functions exposing `extra` payload escape hatches
- group-specific types that are not exported from `plextrac_api.types`
- polished groups still listed as generated in `scripts/generate_endpoints.py`

## Manual Review

For each polished group, review:

- Function names are pleasant, verb-first, and consistent within the group.
- Inputs are explicit and do not expose ambiguous `**kwargs`.
- Outputs are concrete dataclasses, lists, bytes, or dedicated result types.
- `OperationResult` is used only for genuinely generic operation responses.
- Unique response fields are preserved with specific names instead of collapsed into generic IDs.
- Documented finite values are enums, with readable enum member names.
- Raw strings remain only where values are truly open-ended or not exhaustively verified.
- Request dataclasses are reused across multiple functions; single-use request bodies use explicit
  parameters.
- Reused request dataclasses are passed as dataclasses only, without alternate keyword parameter
  paths.
- Public request types do not include `extra` or similar escape-hatch fields.
- Group-specific dataclasses live in `types.<group>` unless they are genuinely cross-cutting.
- Shared dataclasses live in `types.common` only when reused across groups.
- Public function signatures use multiline formatting.
- Docstrings are concise and useful.
- Generator overrides exist for intentional naming fixes.

## Test Coverage Review

Confirm each polished group has appropriate focused tests:

- at least one request-shape test
- at least one response parsing test
- enum serialization tests where the group defines enums
- naming regression tests for intentional generator/name overrides
- upload/download tests where the group handles files or bytes
- GraphQL variable-shape tests for polished GraphQL-backed groups such as `runbooks`

## Audit Output

Record findings in a separate audit result document or issue list with these sections:

- `Pass`
- `Needs Cleanup`
- `Intentional Exceptions`
- `Follow-up Candidates`

Prefer fixing findings in small, reviewable commits grouped by cleanup type or API group.
