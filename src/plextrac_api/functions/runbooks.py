"""Generated PlexTrac endpoint functions.

Do not edit by hand. Run scripts/generate_endpoints.py to refresh.
"""

from __future__ import annotations

from typing import Any

from plextrac_api.functions.common import endpoint_request
from plextrac_api.types.auth import AuthSession


def runbook_engagement_procedure_operator_list(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookEngagementProcedureOperatorListV2"""
    return endpoint_request(session, "runbooks", "runbook_engagement_procedure_operator_list", **kwargs)


def runbook_engagement_procedure_operators_update(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookEngagementProcedureOperatorsUpdateV2"""
    return endpoint_request(session, "runbooks", "runbook_engagement_procedure_operators_update", **kwargs)


def runbook_engagement_procedure_asset_list(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookEngagementProcedureAssetListV2"""
    return endpoint_request(session, "runbooks", "runbook_engagement_procedure_asset_list", **kwargs)


def runbook_engagement_procedure_assets_add(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookEngagementProcedureAssetsAddV2"""
    return endpoint_request(session, "runbooks", "runbook_engagement_procedure_assets_add", **kwargs)


def runbook_engagement_procedure_asset_create(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookEngagementProcedureAssetCreateV2"""
    return endpoint_request(session, "runbooks", "runbook_engagement_procedure_asset_create", **kwargs)


def runbook_engagement_procedure_asset_delete(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookEngagementProcedureAssetDeleteV2"""
    return endpoint_request(session, "runbooks", "runbook_engagement_procedure_asset_delete", **kwargs)


def runbook_engagement_procedure_asset_update(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookEngagementProcedureAssetUpdateV2"""
    return endpoint_request(session, "runbooks", "runbook_engagement_procedure_asset_update", **kwargs)


def runbook_engagement_procedure_logs(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookEngagementProcedureLogsV2"""
    return endpoint_request(session, "runbooks", "runbook_engagement_procedure_logs", **kwargs)


def runbook_engagement_procedure_log_create(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookEngagementProcedureLogCreateV2"""
    return endpoint_request(session, "runbooks", "runbook_engagement_procedure_log_create", **kwargs)


def runbook_engagement_procedure_log_update(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookEngagementProcedureLogUpdateV2"""
    return endpoint_request(session, "runbooks", "runbook_engagement_procedure_log_update", **kwargs)


def runbook_engagement_procedure_log_delete(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookEngagementProcedureLogDeleteV2"""
    return endpoint_request(session, "runbooks", "runbook_engagement_procedure_log_delete", **kwargs)


def runbook_engagement_procedure_attachment_list(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookEngagementProcedureAttachmentListV2"""
    return endpoint_request(session, "runbooks", "runbook_engagement_procedure_attachment_list", **kwargs)


def upload_attachment_to_engagement_procedure(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/runbooks/engagement-procedures/{engagementProcedureId}/attachments/upload\n\nPlexTrac endpoint: Upload Attachment to Engagement Procedure"""
    return endpoint_request(session, "runbooks", "upload_attachment_to_engagement_procedure", **kwargs)


def runbook_engagement_procedure_attachments_update(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookEngagementProcedureAttachmentsUpdateV2"""
    return endpoint_request(session, "runbooks", "runbook_engagement_procedure_attachments_update", **kwargs)


def runbook_engagement_procedure_attachment_delete(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookEngagementProcedureAttachmentDeleteV2"""
    return endpoint_request(session, "runbooks", "runbook_engagement_procedure_attachment_delete", **kwargs)


def runbook_engagement_procedure_ids(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookEngagementProcedureIdsV2"""
    return endpoint_request(session, "runbooks", "runbook_engagement_procedure_ids", **kwargs)


def runbook_engagement_procedure_list(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookEngagementProcedureListV2"""
    return endpoint_request(session, "runbooks", "runbook_engagement_procedure_list", **kwargs)


def runbook_engagement_procedure_detail(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookEngagementProcedureDetailV2"""
    return endpoint_request(session, "runbooks", "runbook_engagement_procedure_detail", **kwargs)


def runbook_engagement_procedure_update(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookEngagementProcedureUpdateV2"""
    return endpoint_request(session, "runbooks", "runbook_engagement_procedure_update", **kwargs)


def runbook_engagement_procedure_delete(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookEngagementProcedureDeleteV2"""
    return endpoint_request(session, "runbooks", "runbook_engagement_procedure_delete", **kwargs)


def runbook_engagement_list(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookEngagementListV2"""
    return endpoint_request(session, "runbooks", "runbook_engagement_list", **kwargs)


def runbook_engagement_detail(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookEngagementDetailV2"""
    return endpoint_request(session, "runbooks", "runbook_engagement_detail", **kwargs)


def runbook_engagement_create(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookEngagementCreateV2"""
    return endpoint_request(session, "runbooks", "runbook_engagement_create", **kwargs)


def runbook_engagement_update(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookEngagementUpdateV2"""
    return endpoint_request(session, "runbooks", "runbook_engagement_update", **kwargs)


def runbook_engagement_delete(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookEngagementDeleteV2"""
    return endpoint_request(session, "runbooks", "runbook_engagement_delete", **kwargs)


def runbook_engagement_finish(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookEngagementFinishV2"""
    return endpoint_request(session, "runbooks", "runbook_engagement_finish", **kwargs)


def runbook_test_plan_list(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookTestPlanListV2"""
    return endpoint_request(session, "runbooks", "runbook_test_plan_list", **kwargs)


def runbook_test_plan_detail(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookTestPlanDetailV2"""
    return endpoint_request(session, "runbooks", "runbook_test_plan_detail", **kwargs)


def runbook_test_plan_create(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookTestPlanCreateV2"""
    return endpoint_request(session, "runbooks", "runbook_test_plan_create", **kwargs)


def runbook_test_plan_update(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookTestPlanUpdateV2"""
    return endpoint_request(session, "runbooks", "runbook_test_plan_update", **kwargs)


def runbook_test_plan_delete(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookTestPlanDeleteV2"""
    return endpoint_request(session, "runbooks", "runbook_test_plan_delete", **kwargs)


def runbook_repository_available_user_list(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookRepositoryAvailableUserListV2"""
    return endpoint_request(session, "runbooks", "runbook_repository_available_user_list", **kwargs)


def runbook_repository_users(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookRepositoryUsersV2"""
    return endpoint_request(session, "runbooks", "runbook_repository_users", **kwargs)


def runbook_repository_users_add(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookRepositoryUsersAddV2"""
    return endpoint_request(session, "runbooks", "runbook_repository_users_add", **kwargs)


def runbook_repository_user_update(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookRepositoryUserUpdateV2"""
    return endpoint_request(session, "runbooks", "runbook_repository_user_update", **kwargs)


def runbook_repository_user_remove(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookRepositoryUserRemoveV2"""
    return endpoint_request(session, "runbooks", "runbook_repository_user_remove", **kwargs)


def runbook_repository_list(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookRepositoryListV2"""
    return endpoint_request(session, "runbooks", "runbook_repository_list", **kwargs)


def runbook_repository_detail(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookRepositoryDetailV2"""
    return endpoint_request(session, "runbooks", "runbook_repository_detail", **kwargs)


def runbook_repository_create(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookRepositoryCreateV2"""
    return endpoint_request(session, "runbooks", "runbook_repository_create", **kwargs)


def runbook_repository_update(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookRepositoryUpdateV2"""
    return endpoint_request(session, "runbooks", "runbook_repository_update", **kwargs)


def runbook_repository_delete(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookRepositoryDeleteV2"""
    return endpoint_request(session, "runbooks", "runbook_repository_delete", **kwargs)


def runbook_methodology_list(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookMethodologyListV2"""
    return endpoint_request(session, "runbooks", "runbook_methodology_list", **kwargs)


def runbook_methodology_detail(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookMethodologyDetailV2"""
    return endpoint_request(session, "runbooks", "runbook_methodology_detail", **kwargs)


def runbook_methodology_create(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookMethodologyCreateV2"""
    return endpoint_request(session, "runbooks", "runbook_methodology_create", **kwargs)


def runbook_methodology_update(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookMethodologyUpdateV2"""
    return endpoint_request(session, "runbooks", "runbook_methodology_update", **kwargs)


def runbook_methodology_delete(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookMethodologyDeleteV2"""
    return endpoint_request(session, "runbooks", "runbook_methodology_delete", **kwargs)


def runbook_tactic_list(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookTacticListV2"""
    return endpoint_request(session, "runbooks", "runbook_tactic_list", **kwargs)


def runbook_tactic_detail(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookTacticDetailV2"""
    return endpoint_request(session, "runbooks", "runbook_tactic_detail", **kwargs)


def runbook_tactic_create(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookTacticCreateV2"""
    return endpoint_request(session, "runbooks", "runbook_tactic_create", **kwargs)


def runbook_tactic_update(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookTacticUpdateV2"""
    return endpoint_request(session, "runbooks", "runbook_tactic_update", **kwargs)


def runbook_tactic_delete(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookTacticDeleteV2"""
    return endpoint_request(session, "runbooks", "runbook_tactic_delete", **kwargs)


def runbook_technique_list(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookTechniqueListV2"""
    return endpoint_request(session, "runbooks", "runbook_technique_list", **kwargs)


def runbook_technique_detail(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookTechniqueDetailV2"""
    return endpoint_request(session, "runbooks", "runbook_technique_detail", **kwargs)


def runbook_technique_create(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookTechniqueCreateV2"""
    return endpoint_request(session, "runbooks", "runbook_technique_create", **kwargs)


def runbook_technique_update(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookTechniqueUpdateV2"""
    return endpoint_request(session, "runbooks", "runbook_technique_update", **kwargs)


def runbook_technique_delete(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookTechniqueDeleteV2"""
    return endpoint_request(session, "runbooks", "runbook_technique_delete", **kwargs)


def runbook_procedure_list(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookProcedureListV2"""
    return endpoint_request(session, "runbooks", "runbook_procedure_list", **kwargs)


def runbook_procedure_detail(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookProcedureDetailV2"""
    return endpoint_request(session, "runbooks", "runbook_procedure_detail", **kwargs)


def runbook_procedure_create(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookProcedureCreateV2"""
    return endpoint_request(session, "runbooks", "runbook_procedure_create", **kwargs)


def runbook_procedure_update(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookProcedureUpdateV2"""
    return endpoint_request(session, "runbooks", "runbook_procedure_update", **kwargs)


def runbook_procedure_delete(session: AuthSession, **kwargs: Any) -> Any:
    """POST /graphql\n\nPlexTrac endpoint: RunbookProcedureDeleteV2"""
    return endpoint_request(session, "runbooks", "runbook_procedure_delete", **kwargs)


def export_runbook(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/export/runbook/{runbookId}\n\nPlexTrac endpoint: Export Runbook"""
    return endpoint_request(session, "runbooks", "export_runbook", **kwargs)


def export(session: AuthSession, **kwargs: Any) -> Any:
    """Alias for `export_runbook`."""
    return export_runbook(session, **kwargs)


def import_runbook(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v1/import/runbook\n\nPlexTrac endpoint: Import Runbook"""
    return endpoint_request(session, "runbooks", "import_runbook", **kwargs)

