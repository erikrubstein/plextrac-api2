"""Generated PlexTrac endpoint functions.

Do not edit by hand. Run scripts/generate_endpoints.py to refresh.
"""

from __future__ import annotations

from typing import Any

from plextrac_api.functions.common import endpoint_request
from plextrac_api.types.auth import AuthSession


def list_all_sections(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/narratives/sections/all\n\nPlexTrac endpoint: List All Sections"""
    return endpoint_request(session, "content_library", "list_all_sections", **kwargs)


def list_narrative_repository_sections(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/narratives/{repositoryId}/sections\n\nPlexTrac endpoint: List Narrative Repository Sections"""
    return endpoint_request(session, "content_library", "list_narrative_repository_sections", **kwargs)


def get_narrative_repository_section(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/narratives/sections/{sectionId}\n\nPlexTrac endpoint: Get Narrative Repository Section"""
    return endpoint_request(session, "content_library", "get_narrative_repository_section", **kwargs)


def create_narratives_db_repository(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/narratives/createNarrativesRepository\n\nPlexTrac endpoint: Create NarrativesDB Repository"""
    return endpoint_request(session, "content_library", "create_narratives_db_repository", **kwargs)


def create_narratives_repository_section(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/narratives/sections\n\nPlexTrac endpoint: Create Narratives Repository Section"""
    return endpoint_request(session, "content_library", "create_narratives_repository_section", **kwargs)


def update_narrative_db_section(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v2/narratives/sections/{sectionId}\n\nPlexTrac endpoint: Update NarrativeDB Section"""
    return endpoint_request(session, "content_library", "update_narrative_db_section", **kwargs)


def delete_narrative_db_section(session: AuthSession, **kwargs: Any) -> Any:
    """DELETE /api/v2/narratives/{repositoryId}/sections/{sectionId}\n\nPlexTrac endpoint: Delete NarrativeDB Section"""
    return endpoint_request(session, "content_library", "delete_narrative_db_section", **kwargs)


def list_narrative_dbs(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/narratives/getAllNarrativesRepositories\n\nPlexTrac endpoint: List NarrativeDBs"""
    return endpoint_request(session, "content_library", "list_narrative_dbs", **kwargs)


def copy_section_to_narative_repository(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/narratives/sections/copy\n\nPlexTrac endpoint: Copy Section to Narative Repository"""
    return endpoint_request(session, "content_library", "copy_section_to_narative_repository", **kwargs)


def get_all_narrative_db_users(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/narratives/users/all\n\nPlexTrac endpoint: Get All NarrativeDB Users"""
    return endpoint_request(session, "content_library", "get_all_narrative_db_users", **kwargs)


def get_narrative_db_users_by_repository(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/narratives/{narrativeRepositoryId}/users\n\nPlexTrac endpoint: Get NarrativeDB Users by Repository"""
    return endpoint_request(session, "content_library", "get_narrative_db_users_by_repository", **kwargs)


def update_narrative_db_users_by_repository(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v2/narratives/{narrativeRepositoryId}/users\n\nPlexTrac endpoint: Update NarrativeDB Users by Repository"""
    return endpoint_request(session, "content_library", "update_narrative_db_users_by_repository", **kwargs)


def get_narrative_db(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/narratives/{narrativeRepositoryId}/getNarrativesRepository\n\nPlexTrac endpoint: Get NarrativeDB"""
    return endpoint_request(session, "content_library", "get_narrative_db", **kwargs)


def update_narrative_db(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v2/narratives/{narrativeRepositoryId}/updateNarrativesRepository\n\nPlexTrac endpoint: Update NarrativeDB"""
    return endpoint_request(session, "content_library", "update_narrative_db", **kwargs)


def delete_narrative_db(session: AuthSession, **kwargs: Any) -> Any:
    """DELETE /api/v2/narratives/{narrativeRepositoryId}/deleteNarrativesRepository\n\nPlexTrac endpoint: Delete NarrativeDB"""
    return endpoint_request(session, "content_library", "delete_narrative_db", **kwargs)


def list_writeups(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/template/list\n\nPlexTrac endpoint: List Writeups"""
    return endpoint_request(session, "content_library", "list_writeups", **kwargs)


def get_writeup(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/template/{writeupId}\n\nPlexTrac endpoint: Get Writeup"""
    return endpoint_request(session, "content_library", "get_writeup", **kwargs)


def create_writeups(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v1/template/create\n\nPlexTrac endpoint: Create Writeups"""
    return endpoint_request(session, "content_library", "create_writeups", **kwargs)


def update_writeups(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v1/template/{writeupId}\n\nPlexTrac endpoint: Update Writeups"""
    return endpoint_request(session, "content_library", "update_writeups", **kwargs)


def delete_writeups(session: AuthSession, **kwargs: Any) -> Any:
    """DELETE /api/v1/template/{writeupId}\n\nPlexTrac endpoint: Delete Writeups"""
    return endpoint_request(session, "content_library", "delete_writeups", **kwargs)


def add_writeup_to_report(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v1/copy/{writeupId}\n\nPlexTrac endpoint: Add Writeup to Report"""
    return endpoint_request(session, "content_library", "add_writeup_to_report", **kwargs)


def bulk_add_writeups_to_report(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/writeups/bulk/addToReport\n\nPlexTrac endpoint: Bulk Add Writeups to Report"""
    return endpoint_request(session, "content_library", "bulk_add_writeups_to_report", **kwargs)


def get_writeups_from_repository(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/repositories/{repositoryId}/getWriteups\n\nPlexTrac endpoint: Get Writeups from Repository"""
    return endpoint_request(session, "content_library", "get_writeups_from_repository", **kwargs)


def add_writeups_to_repository(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/repositories/{repositoryId}/addWriteups\n\nPlexTrac endpoint: Add Writeups to Repository"""
    return endpoint_request(session, "content_library", "add_writeups_to_repository", **kwargs)


def copy_finding_to_writeups_repository(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/repositories/copyFlawToWriteupsRepository\n\nPlexTrac endpoint: Copy Finding to Writeups Repository"""
    return endpoint_request(session, "content_library", "copy_finding_to_writeups_repository", **kwargs)


def import_writeups_to_repository(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/writeups/import/{source}\n\nPlexTrac endpoint: Import Writeups to Repository"""
    return endpoint_request(session, "content_library", "import_writeups_to_repository", **kwargs)


def remove_writeups_from_repository(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/repositories/{repositoryId}/removeWriteup\n\nPlexTrac endpoint: Remove Writeups from Repository"""
    return endpoint_request(session, "content_library", "remove_writeups_from_repository", **kwargs)


def bulk_copy_writeups(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/writeups/bulk/copy\n\nPlexTrac endpoint: Bulk Copy Writeups"""
    return endpoint_request(session, "content_library", "bulk_copy_writeups", **kwargs)


def bulk_move_writeups(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/writeups/bulk/move\n\nPlexTrac endpoint: Bulk Move Writeups"""
    return endpoint_request(session, "content_library", "bulk_move_writeups", **kwargs)


def bulk_add_tags_to_writeups(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/writeups/bulk/tags\n\nPlexTrac endpoint: Bulk Add Tags to Writeups"""
    return endpoint_request(session, "content_library", "bulk_add_tags_to_writeups", **kwargs)


def bulk_delete_writeups(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/writeups/bulk/delete\n\nPlexTrac endpoint: Bulk Delete Writeups"""
    return endpoint_request(session, "content_library", "bulk_delete_writeups", **kwargs)


def list_all_writeup_repositories(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/repositories/getAllWriteupsRepositories\n\nPlexTrac endpoint: List All Writeup Repositories"""
    return endpoint_request(session, "content_library", "list_all_writeup_repositories", **kwargs)


def get_writeups_repository_users_can_edit(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/repositories/listUserCanEdit\n\nPlexTrac endpoint: Get Writeups Repository Users Can Edit"""
    return endpoint_request(session, "content_library", "get_writeups_repository_users_can_edit", **kwargs)


def get_writeup_repository(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/repositories/{repositoryId}\n\nPlexTrac endpoint: Get Writeup Repository"""
    return endpoint_request(session, "content_library", "get_writeup_repository", **kwargs)


def create_writeup_repository(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/repositories/add\n\nPlexTrac endpoint: Create Writeup Repository"""
    return endpoint_request(session, "content_library", "create_writeup_repository", **kwargs)


def update_writeup_repository(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/repositories/{repositoryId}/update\n\nPlexTrac endpoint: Update Writeup Repository"""
    return endpoint_request(session, "content_library", "update_writeup_repository", **kwargs)


def delete_writeup_repository(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/repositories/delete\n\nPlexTrac endpoint: Delete Writeup Repository"""
    return endpoint_request(session, "content_library", "delete_writeup_repository", **kwargs)


def get_writeups_repository_users(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/repositories/{repositoryId}/users\n\nPlexTrac endpoint: Get Writeups Repository Users"""
    return endpoint_request(session, "content_library", "get_writeups_repository_users", **kwargs)


def add_writeups_repository_users(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/repositories/{repositoryId}/users\n\nPlexTrac endpoint: Add Writeups Repository Users"""
    return endpoint_request(session, "content_library", "add_writeups_repository_users", **kwargs)


def update_writeups_repository_users(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v2/repositories/{repositoryId}/users\n\nPlexTrac endpoint: Update Writeups Repository Users"""
    return endpoint_request(session, "content_library", "update_writeups_repository_users", **kwargs)


def get_all_writeups_repository_users(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/repositories/users\n\nPlexTrac endpoint: Get All Writeups Repository Users"""
    return endpoint_request(session, "content_library", "get_all_writeups_repository_users", **kwargs)

