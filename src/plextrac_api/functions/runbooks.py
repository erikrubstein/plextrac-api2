from __future__ import annotations

from pathlib import Path
from typing import BinaryIO, TypeVar, cast

from plextrac_api.functions.common import graphql_request, rest_request
from plextrac_api.generated.endpoints import GROUPS
from plextrac_api.types.auth import AuthSession
from plextrac_api.types.common import JsonDict
from plextrac_api.types.runbooks import (
    RunbookAsset,
    RunbookAssetInput,
    RunbookAttachment,
    RunbookEngagement,
    RunbookEngagementInput,
    RunbookEngagementProcedure,
    RunbookExecutionStepInput,
    RunbookImportResult,
    RunbookListArgs,
    RunbookMethodology,
    RunbookMutationResult,
    RunbookProcedure,
    RunbookProcedureLog,
    RunbookProcedureLogInput,
    RunbookRecord,
    RunbookRecordInput,
    RunbookRepository,
    RunbookTactic,
    RunbookTeam,
    RunbookTechnique,
    RunbookTestPlan,
    RunbookUploadResult,
    RunbookUser,
    RunbookUserInput,
)

RunbookRecordT = TypeVar("RunbookRecordT", bound=RunbookRecord)


def list_runbook_engagement_procedure_operators(
    session: AuthSession,
    procedure_id: int | str,
) -> list[RunbookUser]:
    """Execute the runbook engagement procedure operator list operation."""
    variables = {
        "procedureId": procedure_id,
    }
    data = _graphql_data(session, "list_runbook_engagement_procedure_operators", variables)
    return _user_list(data)


def update_runbook_engagement_procedure_operators(
    session: AuthSession,
    procedure_id: int | str,
    operators: list[RunbookUserInput],
) -> list[RunbookUser]:
    """Execute the runbook engagement procedure operators update operation."""
    variables = {
        "procedureId": procedure_id,
        "operators": [item.to_api() for item in operators],
    }
    data = _graphql_data(session, "update_runbook_engagement_procedure_operators", variables)
    return _user_list(data)


def list_runbook_engagement_procedure_assets(
    session: AuthSession,
    procedure_id: int | str,
) -> list[RunbookAsset]:
    """Execute the runbook engagement procedure asset list operation."""
    variables = {
        "procedureId": procedure_id,
    }
    data = _graphql_data(session, "list_runbook_engagement_procedure_assets", variables)
    return _asset_list(data)


def add_runbook_engagement_procedure_assets(
    session: AuthSession,
    procedure_id: int | str,
    client_asset_ids: list[int | str],
) -> list[RunbookAsset]:
    """Execute the runbook engagement procedure assets add operation."""
    variables = {
        "procedureId": procedure_id,
        "clientAssetIds": client_asset_ids,
    }
    data = _graphql_data(session, "add_runbook_engagement_procedure_assets", variables)
    return _asset_list(data)


def create_runbook_engagement_procedure_asset(
    session: AuthSession,
    procedure_id: int | str,
    asset: RunbookAssetInput,
    evidence_ids: list[int | str] | None = None,
) -> RunbookAsset:
    """Execute the runbook engagement procedure asset create operation."""
    variables = {
        "procedureId": procedure_id,
        "clientAsset": asset.to_api(),
        "evidences": [_id_input(item) for item in evidence_ids] if evidence_ids is not None else None,
    }
    data = _graphql_data(session, "create_runbook_engagement_procedure_asset", variables)
    return RunbookAsset.from_api(_record_object(data))


def delete_runbook_engagement_procedure_asset(
    session: AuthSession,
    asset_id: int | str,
    procedure_id: int | str,
) -> RunbookMutationResult:
    """Execute the runbook engagement procedure asset delete operation."""
    variables = {
        "id": asset_id,
        "procedureId": procedure_id,
    }
    data = _graphql_data(session, "delete_runbook_engagement_procedure_asset", variables)
    return RunbookMutationResult.from_api(data)


def update_runbook_engagement_procedure_asset(
    session: AuthSession,
    asset_id: int | str,
    procedure_id: int | str,
    asset: RunbookAssetInput | None = None,
    evidence_ids: list[int | str] | None = None,
    input: RunbookAssetInput | None = None,
) -> RunbookAsset:
    """Execute the runbook engagement procedure asset update operation."""
    variables = {
        "id": asset_id,
        "procedureId": procedure_id,
        "clientAsset": asset.to_api() if asset is not None else None,
        "evidences": [_id_input(item) for item in evidence_ids] if evidence_ids is not None else None,
        "input": input.to_api() if input is not None else None,
    }
    data = _graphql_data(session, "update_runbook_engagement_procedure_asset", variables)
    return RunbookAsset.from_api(_record_object(data))


def list_runbook_engagement_procedure_logs(
    session: AuthSession,
    engagement_procedure_id: int | str,
) -> list[RunbookProcedureLog]:
    """Execute the runbook engagement procedure logs operation."""
    variables = {
        "engagementProcedureId": engagement_procedure_id,
    }
    data = _graphql_data(session, "list_runbook_engagement_procedure_logs", variables)
    return _log_list(data)


def create_runbook_engagement_procedure_log(
    session: AuthSession,
    engagement_procedure_id: int | str,
    log: RunbookProcedureLogInput,
) -> RunbookProcedureLog:
    """Execute the runbook engagement procedure log create operation."""
    variables = {
        "engagementProcedureId": engagement_procedure_id,
        "input": log.to_api(),
    }
    data = _graphql_data(session, "create_runbook_engagement_procedure_log", variables)
    return RunbookProcedureLog.from_api(_record_object(data))


def update_runbook_engagement_procedure_log(
    session: AuthSession,
    log_id: int | str,
    log: RunbookProcedureLogInput,
) -> RunbookProcedureLog:
    """Execute the runbook engagement procedure log update operation."""
    variables = {
        "id": log_id,
        "input": log.to_api(),
    }
    data = _graphql_data(session, "update_runbook_engagement_procedure_log", variables)
    return RunbookProcedureLog.from_api(_record_object(data))


def delete_runbook_engagement_procedure_log(
    session: AuthSession,
    log_id: int | str,
) -> RunbookMutationResult:
    """Execute the runbook engagement procedure log delete operation."""
    variables = {
        "id": log_id,
    }
    data = _graphql_data(session, "delete_runbook_engagement_procedure_log", variables)
    return RunbookMutationResult.from_api(data)


def list_runbook_engagement_procedure_attachments(
    session: AuthSession,
    procedure_id: int | str,
    team: RunbookTeam,
) -> list[RunbookAttachment]:
    """Execute the runbook engagement procedure attachment list operation."""
    variables = {
        "procedureId": procedure_id,
        "team": team.value,
    }
    data = _graphql_data(session, "list_runbook_engagement_procedure_attachments", variables)
    return _attachment_list(data)


def update_runbook_engagement_procedure_attachments(
    session: AuthSession,
    procedure_id: int | str,
    attachment_ids: list[int | str],
) -> list[RunbookAttachment]:
    """Execute the runbook engagement procedure attachments update operation."""
    variables = {
        "procedureId": procedure_id,
        "attachments": [_id_input(item) for item in attachment_ids],
    }
    data = _graphql_data(session, "update_runbook_engagement_procedure_attachments", variables)
    return _attachment_list(data)


def delete_runbook_engagement_procedure_attachment(
    session: AuthSession,
    procedure_id: int | str,
    attachment_id: int | str,
) -> RunbookMutationResult:
    """Execute the runbook engagement procedure attachment delete operation."""
    variables = {
        "procedureId": procedure_id,
        "id": attachment_id,
    }
    data = _graphql_data(session, "delete_runbook_engagement_procedure_attachment", variables)
    return RunbookMutationResult.from_api(data)


def list_runbook_engagement_procedure_ids(
    session: AuthSession,
    engagement_id: int | str,
) -> list[str]:
    """Execute the runbook engagement procedure ids operation."""
    variables = {
        "engagementId": engagement_id,
    }
    data = _graphql_data(session, "list_runbook_engagement_procedure_ids", variables)
    return _ids(data)


def list_runbook_engagement_procedures(
    session: AuthSession,
    engagement_id: int | str,
    args: RunbookListArgs | None = None,
) -> list[RunbookEngagementProcedure]:
    """Execute the runbook engagement procedure list operation."""
    variables = {
        "engagementId": engagement_id,
        "args": (args or RunbookListArgs()).to_api(),
    }
    data = _graphql_data(session, "list_runbook_engagement_procedures", variables)
    return _record_list(data, RunbookEngagementProcedure)


def get_runbook_engagement_procedure(
    session: AuthSession,
    procedure_id: int | str,
) -> RunbookEngagementProcedure:
    """Execute the runbook engagement procedure detail operation."""
    variables = {
        "procedureId": procedure_id,
    }
    data = _graphql_data(session, "get_runbook_engagement_procedure", variables)
    return RunbookEngagementProcedure.from_api(_record_object(data))


def update_runbook_engagement_procedure(
    session: AuthSession,
    procedure_id: int | str,
    procedure: RunbookRecordInput,
    execution_steps: list[RunbookExecutionStepInput] | None = None,
    assets: list[RunbookAssetInput] | None = None,
) -> RunbookEngagementProcedure:
    """Execute the runbook engagement procedure update operation."""
    variables = {
        "id": procedure_id,
        "data": procedure.to_api(),
        "executionSteps": (
            [item.to_api() for item in execution_steps]
            if execution_steps is not None
            else None
        ),
        "assets": [item.to_api() for item in assets] if assets is not None else None,
    }
    data = _graphql_data(session, "update_runbook_engagement_procedure", variables)
    return RunbookEngagementProcedure.from_api(_record_object(data))


def delete_runbook_engagement_procedure(
    session: AuthSession,
    procedure_id: int | str,
) -> RunbookMutationResult:
    """Execute the runbook engagement procedure delete operation."""
    variables = {
        "id": procedure_id,
    }
    data = _graphql_data(session, "delete_runbook_engagement_procedure", variables)
    return RunbookMutationResult.from_api(data)


def list_runbook_engagements(
    session: AuthSession,
    args: RunbookListArgs | None = None,
) -> list[RunbookEngagement]:
    """Execute the runbook engagement list operation."""
    variables = {
        "args": (args or RunbookListArgs()).to_api(),
    }
    data = _graphql_data(session, "list_runbook_engagements", variables)
    return _record_list(data, RunbookEngagement)


def get_runbook_engagement(
    session: AuthSession,
    engagement_id: int | str,
) -> RunbookEngagement:
    """Execute the runbook engagement detail operation."""
    variables = {
        "engagementId": engagement_id,
    }
    data = _graphql_data(session, "get_runbook_engagement", variables)
    return RunbookEngagement.from_api(_record_object(data))


def create_runbook_engagement(
    session: AuthSession,
    engagement: RunbookEngagementInput,
    procedure_ids: list[int | str] | None = None,
    tags: list[str] | None = None,
) -> RunbookEngagement:
    """Execute the runbook engagement create operation."""
    variables = {
        "data": engagement.to_api(),
        "procedureIds": procedure_ids,
        "tags": tags,
    }
    data = _graphql_data(session, "create_runbook_engagement", variables)
    return RunbookEngagement.from_api(_record_object(data))


def update_runbook_engagement(
    session: AuthSession,
    engagement_id: int | str,
    engagement: RunbookEngagementInput,
    procedure_ids: list[int | str] | None = None,
    tags: list[str] | None = None,
) -> RunbookEngagement:
    """Execute the runbook engagement update operation."""
    variables = {
        "id": engagement_id,
        "data": engagement.to_api(),
        "procedureIds": procedure_ids,
        "tags": tags,
    }
    data = _graphql_data(session, "update_runbook_engagement", variables)
    return RunbookEngagement.from_api(_record_object(data))


def delete_runbook_engagement(
    session: AuthSession,
    engagement_id: int | str,
) -> RunbookMutationResult:
    """Execute the runbook engagement delete operation."""
    variables = {
        "id": engagement_id,
    }
    data = _graphql_data(session, "delete_runbook_engagement", variables)
    return RunbookMutationResult.from_api(data)


def finish_runbook_engagement(
    session: AuthSession,
    engagement_id: int | str,
) -> RunbookMutationResult:
    """Execute the runbook engagement finish operation."""
    variables = {
        "id": engagement_id,
    }
    data = _graphql_data(session, "finish_runbook_engagement", variables)
    return RunbookMutationResult.from_api(data)


def list_runbook_test_plans(
    session: AuthSession,
    args: RunbookListArgs | None = None,
) -> list[RunbookTestPlan]:
    """Execute the runbook test plan list operation."""
    variables = {
        "args": (args or RunbookListArgs()).to_api(),
    }
    data = _graphql_data(session, "list_runbook_test_plans", variables)
    return _record_list(data, RunbookTestPlan)


def get_runbook_test_plan(
    session: AuthSession,
    test_plan_id: int | str,
) -> RunbookTestPlan:
    """Execute the runbook test plan detail operation."""
    variables = {
        "testPlanId": test_plan_id,
    }
    data = _graphql_data(session, "get_runbook_test_plan", variables)
    return RunbookTestPlan.from_api(_record_object(data))


def create_runbook_test_plan(
    session: AuthSession,
    test_plan: RunbookEngagementInput,
    procedure_ids: list[int | str] | None = None,
    tags: list[str] | None = None,
) -> RunbookTestPlan:
    """Execute the runbook test plan create operation."""
    variables = {
        "data": test_plan.to_api(),
        "procedureIds": procedure_ids,
        "tags": tags,
    }
    data = _graphql_data(session, "create_runbook_test_plan", variables)
    return RunbookTestPlan.from_api(_record_object(data))


def update_runbook_test_plan(
    session: AuthSession,
    test_plan_id: int | str,
    test_plan: RunbookEngagementInput,
    procedure_ids: list[int | str] | None = None,
    tags: list[str] | None = None,
) -> RunbookTestPlan:
    """Execute the runbook test plan update operation."""
    variables = {
        "id": test_plan_id,
        "data": test_plan.to_api(),
        "procedureIds": procedure_ids,
        "tags": tags,
    }
    data = _graphql_data(session, "update_runbook_test_plan", variables)
    return RunbookTestPlan.from_api(_record_object(data))


def delete_runbook_test_plan(
    session: AuthSession,
    test_plan_id: int | str,
) -> RunbookMutationResult:
    """Execute the runbook test plan delete operation."""
    variables = {
        "id": test_plan_id,
    }
    data = _graphql_data(session, "delete_runbook_test_plan", variables)
    return RunbookMutationResult.from_api(data)


def list_available_runbook_repository_users(
    session: AuthSession,
    args: RunbookListArgs | None = None,
) -> list[RunbookUser]:
    """Execute the runbook repository available user list operation."""
    variables = {
        "args": (args or RunbookListArgs()).to_api(),
    }
    data = _graphql_data(session, "list_available_runbook_repository_users", variables)
    return _user_list(data)


def list_runbook_repository_users(
    session: AuthSession,
    repository_id: int | str,
) -> list[RunbookUser]:
    """Execute the runbook repository users operation."""
    variables = {
        "repositoryId": repository_id,
    }
    data = _graphql_data(session, "list_runbook_repository_users", variables)
    return _user_list(data)


def add_runbook_repository_users(
    session: AuthSession,
    repository_id: int | str,
    users: list[RunbookUserInput],
) -> list[RunbookUser]:
    """Execute the runbook repository users add operation."""
    variables = {
        "repositoryId": repository_id,
        "users": [item.to_api() for item in users],
    }
    data = _graphql_data(session, "add_runbook_repository_users", variables)
    return _user_list(data)


def update_runbook_repository_user(
    session: AuthSession,
    repository_id: int | str,
    user_id: int | str,
    user: RunbookUserInput,
) -> RunbookUser:
    """Execute the runbook repository user update operation."""
    variables = {
        "repositoryId": repository_id,
        "userId": user_id,
        "data": user,
    }
    data = _graphql_data(session, "update_runbook_repository_user", variables)
    return RunbookUser.from_api(_record_object(data))


def remove_runbook_repository_user(
    session: AuthSession,
    repository_id: int | str,
    user_id: int | str,
) -> RunbookMutationResult:
    """Execute the runbook repository user remove operation."""
    variables = {
        "repositoryId": repository_id,
        "userId": user_id,
    }
    data = _graphql_data(session, "remove_runbook_repository_user", variables)
    return RunbookMutationResult.from_api(data)


def list_runbook_repositories(
    session: AuthSession,
    args: RunbookListArgs | None = None,
) -> list[RunbookRepository]:
    """Execute the runbook repository list operation."""
    variables = {
        "args": (args or RunbookListArgs()).to_api(),
    }
    data = _graphql_data(session, "list_runbook_repositories", variables)
    return _record_list(data, RunbookRepository)


def get_runbook_repository(
    session: AuthSession,
    repository_id: int | str,
    procedure_list_args: RunbookListArgs | None = None,
) -> RunbookRepository:
    """Execute the runbook repository detail operation."""
    variables = {
        "repositoryId": repository_id,
        "procedureListArgs": (procedure_list_args or RunbookListArgs()).to_api(),
    }
    data = _graphql_data(session, "get_runbook_repository", variables)
    return RunbookRepository.from_api(_record_object(data))


def create_runbook_repository(
    session: AuthSession,
    repository: RunbookRecordInput,
) -> RunbookRepository:
    """Execute the runbook repository create operation."""
    variables = {
        "data": repository.to_api(),
    }
    data = _graphql_data(session, "create_runbook_repository", variables)
    return RunbookRepository.from_api(_record_object(data))


def update_runbook_repository(
    session: AuthSession,
    repository: RunbookRecordInput,
    repository_id: int | str,
) -> RunbookRepository:
    """Execute the runbook repository update operation."""
    variables = {
        "data": repository.to_api(),
        "repositoryId": repository_id,
    }
    data = _graphql_data(session, "update_runbook_repository", variables)
    return RunbookRepository.from_api(_record_object(data))


def delete_runbook_repository(
    session: AuthSession,
    repository_id: int | str,
) -> RunbookMutationResult:
    """Execute the runbook repository delete operation."""
    variables = {
        "id": repository_id,
    }
    data = _graphql_data(session, "delete_runbook_repository", variables)
    return RunbookMutationResult.from_api(data)


def list_runbook_methodologies(
    session: AuthSession,
    args: RunbookListArgs | None = None,
) -> list[RunbookMethodology]:
    """Execute the runbook methodology list operation."""
    variables = {
        "args": (args or RunbookListArgs()).to_api(),
    }
    data = _graphql_data(session, "list_runbook_methodologies", variables)
    return _record_list(data, RunbookMethodology)


def get_runbook_methodology(
    session: AuthSession,
    methodology_id: int | str,
) -> RunbookMethodology:
    """Execute the runbook methodology detail operation."""
    variables = {
        "methodologyId": methodology_id,
    }
    data = _graphql_data(session, "get_runbook_methodology", variables)
    return RunbookMethodology.from_api(_record_object(data))


def create_runbook_methodology(
    session: AuthSession,
    methodology: RunbookRecordInput,
    tactic_ids: list[int | str] | None = None,
    tags: list[str] | None = None,
) -> RunbookMethodology:
    """Execute the runbook methodology create operation."""
    variables = {
        "data": methodology.to_api(),
        "tacticIds": tactic_ids,
        "tags": tags,
    }
    data = _graphql_data(session, "create_runbook_methodology", variables)
    return RunbookMethodology.from_api(_record_object(data))


def update_runbook_methodology(
    session: AuthSession,
    methodology_id: int | str,
    methodology: RunbookRecordInput,
    tactic_ids: list[int | str] | None = None,
    tags: list[str] | None = None,
) -> RunbookMethodology:
    """Execute the runbook methodology update operation."""
    variables = {
        "id": methodology_id,
        "data": methodology.to_api(),
        "tacticIds": tactic_ids,
        "tags": tags,
    }
    data = _graphql_data(session, "update_runbook_methodology", variables)
    return RunbookMethodology.from_api(_record_object(data))


def delete_runbook_methodology(
    session: AuthSession,
    methodology_id: int | str,
) -> RunbookMutationResult:
    """Execute the runbook methodology delete operation."""
    variables = {
        "id": methodology_id,
    }
    data = _graphql_data(session, "delete_runbook_methodology", variables)
    return RunbookMutationResult.from_api(data)


def list_runbook_tactics(
    session: AuthSession,
    args: RunbookListArgs | None = None,
) -> list[RunbookTactic]:
    """Execute the runbook tactic list operation."""
    variables = {
        "args": (args or RunbookListArgs()).to_api(),
    }
    data = _graphql_data(session, "list_runbook_tactics", variables)
    return _record_list(data, RunbookTactic)


def get_runbook_tactic(
    session: AuthSession,
    tactic_id: int | str,
) -> RunbookTactic:
    """Execute the runbook tactic detail operation."""
    variables = {
        "tacticId": tactic_id,
    }
    data = _graphql_data(session, "get_runbook_tactic", variables)
    return RunbookTactic.from_api(_record_object(data))


def create_runbook_tactic(
    session: AuthSession,
    tactic: RunbookRecordInput,
    methodology_ids: list[int | str] | None = None,
    technique_ids: list[int | str] | None = None,
    tags: list[str] | None = None,
) -> RunbookTactic:
    """Execute the runbook tactic create operation."""
    variables = {
        "data": tactic.to_api(),
        "methodologyIds": methodology_ids,
        "techniqueIds": technique_ids,
        "tags": tags,
    }
    data = _graphql_data(session, "create_runbook_tactic", variables)
    return RunbookTactic.from_api(_record_object(data))


def update_runbook_tactic(
    session: AuthSession,
    tactic_id: int | str,
    tactic: RunbookRecordInput,
    methodology_ids: list[int | str] | None = None,
    technique_ids: list[int | str] | None = None,
    tags: list[str] | None = None,
) -> RunbookTactic:
    """Execute the runbook tactic update operation."""
    variables = {
        "id": tactic_id,
        "data": tactic.to_api(),
        "methodologyIds": methodology_ids,
        "techniqueIds": technique_ids,
        "tags": tags,
    }
    data = _graphql_data(session, "update_runbook_tactic", variables)
    return RunbookTactic.from_api(_record_object(data))


def delete_runbook_tactic(
    session: AuthSession,
    tactic_id: int | str,
) -> RunbookMutationResult:
    """Execute the runbook tactic delete operation."""
    variables = {
        "id": tactic_id,
    }
    data = _graphql_data(session, "delete_runbook_tactic", variables)
    return RunbookMutationResult.from_api(data)


def list_runbook_techniques(
    session: AuthSession,
    args: RunbookListArgs | None = None,
) -> list[RunbookTechnique]:
    """Execute the runbook technique list operation."""
    variables = {
        "args": (args or RunbookListArgs()).to_api(),
    }
    data = _graphql_data(session, "list_runbook_techniques", variables)
    return _record_list(data, RunbookTechnique)


def get_runbook_technique(
    session: AuthSession,
    technique_id: int | str,
) -> RunbookTechnique:
    """Execute the runbook technique detail operation."""
    variables = {
        "techniqueId": technique_id,
    }
    data = _graphql_data(session, "get_runbook_technique", variables)
    return RunbookTechnique.from_api(_record_object(data))


def create_runbook_technique(
    session: AuthSession,
    technique: RunbookRecordInput,
    tactic_ids: list[int | str] | None = None,
    procedure_ids: list[int | str] | None = None,
    tags: list[str] | None = None,
) -> RunbookTechnique:
    """Execute the runbook technique create operation."""
    variables = {
        "data": technique.to_api(),
        "tacticIds": tactic_ids,
        "procedureIds": procedure_ids,
        "tags": tags,
    }
    data = _graphql_data(session, "create_runbook_technique", variables)
    return RunbookTechnique.from_api(_record_object(data))


def update_runbook_technique(
    session: AuthSession,
    technique: RunbookRecordInput,
    technique_id: int | str,
    tactic_ids: list[int | str] | None = None,
    procedure_ids: list[int | str] | None = None,
    tags: list[str] | None = None,
) -> RunbookTechnique:
    """Execute the runbook technique update operation."""
    variables = {
        "data": technique.to_api(),
        "id": technique_id,
        "tacticIds": tactic_ids,
        "procedureIds": procedure_ids,
        "tags": tags,
    }
    data = _graphql_data(session, "update_runbook_technique", variables)
    return RunbookTechnique.from_api(_record_object(data))


def delete_runbook_technique(
    session: AuthSession,
    technique_id: int | str,
) -> RunbookMutationResult:
    """Execute the runbook technique delete operation."""
    variables = {
        "id": technique_id,
    }
    data = _graphql_data(session, "delete_runbook_technique", variables)
    return RunbookMutationResult.from_api(data)


def list_runbook_procedures(
    session: AuthSession,
    args: RunbookListArgs | None = None,
) -> list[RunbookProcedure]:
    """Execute the runbook procedure list operation."""
    variables = {
        "args": (args or RunbookListArgs()).to_api(),
    }
    data = _graphql_data(session, "list_runbook_procedures", variables)
    return _record_list(data, RunbookProcedure)


def get_runbook_procedure(
    session: AuthSession,
    procedure_id: int | str,
) -> RunbookProcedure:
    """Execute the runbook procedure detail operation."""
    variables = {
        "id": procedure_id,
    }
    data = _graphql_data(session, "get_runbook_procedure", variables)
    return RunbookProcedure.from_api(_record_object(data))


def create_runbook_procedure(
    session: AuthSession,
    procedure: RunbookRecordInput,
    execution_steps: list[RunbookExecutionStepInput],
    technique_ids: list[int | str] | None = None,
    tags: list[str] | None = None,
) -> RunbookProcedure:
    """Execute the runbook procedure create operation."""
    variables = {
        "data": procedure.to_api(),
        "executionSteps": (
            [item.to_api() for item in execution_steps]
            if execution_steps is not None
            else None
        ),
        "techniqueIds": technique_ids,
        "tags": tags,
    }
    data = _graphql_data(session, "create_runbook_procedure", variables)
    return RunbookProcedure.from_api(_record_object(data))


def update_runbook_procedure(
    session: AuthSession,
    procedure_id: int | str,
    procedure: RunbookRecordInput,
    execution_steps: list[RunbookExecutionStepInput],
    technique_ids: list[int | str] | None = None,
    tags: list[str] | None = None,
) -> RunbookProcedure:
    """Execute the runbook procedure update operation."""
    variables = {
        "id": procedure_id,
        "data": procedure.to_api(),
        "executionSteps": (
            [item.to_api() for item in execution_steps]
            if execution_steps is not None
            else None
        ),
        "techniqueIds": technique_ids,
        "tags": tags,
    }
    data = _graphql_data(session, "update_runbook_procedure", variables)
    return RunbookProcedure.from_api(_record_object(data))


def delete_runbook_procedure(
    session: AuthSession,
    procedure_id: int | str,
) -> RunbookMutationResult:
    """Execute the runbook procedure delete operation."""
    variables = {
        "id": procedure_id,
    }
    data = _graphql_data(session, "delete_runbook_procedure", variables)
    return RunbookMutationResult.from_api(data)


def upload_runbook_engagement_procedure_attachment(
    session: AuthSession,
    engagement_procedure_id: int | str,
    file: str | Path | BinaryIO,
    *,
    filename: str | None = None,
    content_type: str | None = None,
) -> RunbookUploadResult:
    """Upload an attachment to an engagement procedure."""
    data = _upload_file(
        session,
        f"/api/v2/runbooks/engagement-procedures/{engagement_procedure_id}/attachments/upload",
        file,
        filename=filename,
        content_type=content_type,
        fallback_name="runbook-attachment",
    )
    return RunbookUploadResult.from_api(data if isinstance(data, dict) else {"data": data})


def export_runbook(
    session: AuthSession,
    runbook_id: int | str,
) -> bytes:
    """Export a runbook file."""
    data = rest_request(session, "GET", f"/api/v1/export/runbook/{runbook_id}")
    if isinstance(data, bytes):
        return data
    raise ValueError("PlexTrac runbook export response was not bytes.")


def import_runbook(
    session: AuthSession,
    file: str | Path | BinaryIO,
    *,
    filename: str | None = None,
    content_type: str | None = None,
) -> RunbookImportResult:
    """Import a runbook file."""
    data = _upload_file(
        session,
        "/api/v1/import/runbook",
        file,
        filename=filename,
        content_type=content_type,
        fallback_name="runbook",
    )
    return RunbookImportResult.from_api(data if isinstance(data, dict) else {"data": data})


def _graphql_data(
    session: AuthSession,
    method_name: str,
    variables: JsonDict,
) -> object:
    endpoint = _endpoint(method_name)
    query = endpoint.get("graphql_query")
    if not isinstance(query, str):
        raise ValueError(f"Runbook endpoint {method_name} does not define a GraphQL query.")
    data = graphql_request(session, _operation_name(query), query, _clean(variables))
    field = _root_field(query)
    return data.get(field) if field else data


def _endpoint(method_name: str) -> JsonDict:
    for endpoint in GROUPS["runbooks"]["endpoints"]:
        if endpoint["method_name"] == method_name:
            return cast(JsonDict, endpoint)
    raise KeyError(method_name)


def _operation_name(query: str) -> str | None:
    match = __import__("re").search(r"^(?:query|mutation)\s+(\w+)", query.strip())
    return match.group(1) if match else None


def _root_field(query: str) -> str | None:
    match = __import__("re").search(r"{\s*(\w+)\s*(?:\(|{)", query, flags=__import__("re").S)
    return match.group(1) if match else None


def _record_list(data: object, record_type: type[RunbookRecordT]) -> list[RunbookRecordT]:
    return [record_type.from_api(item) for item in _items(data)]


def _user_list(data: object) -> list[RunbookUser]:
    return [RunbookUser.from_api(item) for item in _items(data)]


def _asset_list(data: object) -> list[RunbookAsset]:
    return [RunbookAsset.from_api(item) for item in _items(data)]


def _attachment_list(data: object) -> list[RunbookAttachment]:
    return [RunbookAttachment.from_api(item) for item in _items(data)]


def _log_list(data: object) -> list[RunbookProcedureLog]:
    return [RunbookProcedureLog.from_api(item) for item in _items(data)]


def _record_object(data: object) -> JsonDict:
    if isinstance(data, dict):
        nested = data.get("data")
        if isinstance(nested, dict):
            return cast(JsonDict, nested)
        return data
    items = _items(data)
    if items:
        return items[0]
    raise ValueError("PlexTrac runbook response was not a JSON object.")


def _items(data: object) -> list[JsonDict]:
    if isinstance(data, list):
        return [item for item in data if isinstance(item, dict)]
    if isinstance(data, dict):
        for key in ("nodes", "items", "data", "results", "edges"):
            value = data.get(key)
            if isinstance(value, list):
                if key == "edges":
                    return [edge["node"] for edge in value if isinstance(edge, dict) and isinstance(edge.get("node"), dict)]
                return [item for item in value if isinstance(item, dict)]
        return [data]
    return []


def _ids(data: object) -> list[str]:
    if isinstance(data, dict):
        for key in ("procedureIds", "ids", "data"):
            value = data.get(key)
            if isinstance(value, list):
                return [str(item) for item in value]
    if isinstance(data, list):
        return [str(item) for item in data]
    return []


def _clean(data: JsonDict) -> JsonDict:
    return {key: value for key, value in data.items() if value is not None}


def _id_input(value: int | str) -> JsonDict:
    return {"id": value}


def _upload_file(
    session: AuthSession,
    path: str,
    file: str | Path | BinaryIO,
    *,
    filename: str | None,
    content_type: str | None,
    fallback_name: str,
) -> object:
    close_after = None
    if isinstance(file, (str, Path)):
        file_path = Path(file)
        close_after = file_path.open("rb")
        file_obj: BinaryIO = close_after
        upload_name = filename or file_path.name
    else:
        file_obj = file
        upload_name = filename or Path(getattr(file, "name", fallback_name)).name

    files = {"file": (upload_name, file_obj, content_type) if content_type else (upload_name, file_obj)}
    try:
        return rest_request(session, "POST", path, files=files)
    finally:
        if close_after is not None:
            close_after.close()
