from __future__ import annotations

from pathlib import Path
from typing import BinaryIO, cast

from plextrac_api.functions.common import rest_request
from plextrac_api.types.auth import AuthSession
from plextrac_api.types.common import JsonDict, OperationResult, clean
from plextrac_api.types.content_library import (
    ContentLibraryImportResult,
    ContentLibraryUser,
    ContentLibraryUserInput,
    NarrativeRepository,
    NarrativeRepositoryInput,
    NarrativeSection,
    NarrativeSectionInput,
    Writeup,
    WriteupDeleteResult,
    WriteupImportSource,
    WriteupInput,
    WriteupRepository,
    WriteupRepositoryInput,
    WriteupTransfer,
)


def list_all_sections(
    session: AuthSession,
    *,
    permission_level: str | None = None,
) -> list[NarrativeSection]:
    """List all NarrativesDB sections available to the caller."""
    data = rest_request(
        session,
        "POST",
        "/api/v2/narratives/sections/all",
        json=clean({"permissionsLevel": permission_level}),
    )
    return [NarrativeSection.from_api(item) for item in _items(data, "sections")]


def list_narrative_repository_sections(
    session: AuthSession,
    repository_id: int | str,
    *,
    permission_level: str | None = None,
) -> list[NarrativeSection]:
    """List sections for one NarrativesDB repository."""
    data = rest_request(
        session,
        "POST",
        f"/api/v2/narratives/{repository_id}/sections",
        json=clean({"permissionsLevel": permission_level}),
    )
    return [NarrativeSection.from_api(item) for item in _items(data, "sections")]


def get_narrative_repository_section(
    session: AuthSession,
    section_id: int | str,
) -> NarrativeSection:
    """Get one NarrativesDB section."""
    data = rest_request(session, "GET", f"/api/v2/narratives/sections/{section_id}")
    return NarrativeSection.from_api(_object(data, "narrative section"))


def create_narrative_repository(
    session: AuthSession,
    repository: NarrativeRepositoryInput,
) -> NarrativeRepository:
    """Create a NarrativesDB repository."""
    data = rest_request(
        session,
        "POST",
        "/api/v2/narratives/createNarrativesRepository",
        json=repository.to_api(),
    )
    return NarrativeRepository.from_api(_object(data, "narrative repository"))


def create_narrative_repository_section(
    session: AuthSession,
    section: NarrativeSectionInput,
) -> NarrativeSection:
    """Create a section in a NarrativesDB repository."""
    data = rest_request(
        session,
        "POST",
        "/api/v2/narratives/sections",
        json=section.to_api(),
    )
    return NarrativeSection.from_api(_object(data, "narrative section"))


def update_narrative_repository_section(
    session: AuthSession,
    section_id: int | str,
    section: NarrativeSectionInput,
) -> NarrativeSection:
    """Update one NarrativesDB section."""
    data = rest_request(
        session,
        "PUT",
        f"/api/v2/narratives/sections/{section_id}",
        json=section.to_api(),
    )
    return NarrativeSection.from_api(_object(data, "narrative section"))


def delete_narrative_repository_section(
    session: AuthSession,
    repository_id: int | str,
    section_id: int | str,
) -> OperationResult:
    """Delete one section from a NarrativesDB repository."""
    data = rest_request(
        session,
        "DELETE",
        f"/api/v2/narratives/{repository_id}/sections/{section_id}",
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def list_narrative_repositories(
    session: AuthSession,
    *,
    permission_level: str | None = None,
) -> list[NarrativeRepository]:
    """List NarrativesDB repositories available to the caller."""
    data = rest_request(
        session,
        "POST",
        "/api/v2/narratives/getAllNarrativesRepositories",
        json=clean({"permissionsLevel": permission_level}),
    )
    return [NarrativeRepository.from_api(item) for item in _items(data, "repositories")]


def copy_section_to_narrative_repository(
    session: AuthSession,
    section_id: int | str,
    destination_repository_id: int | str,
) -> NarrativeSection:
    """Copy a NarrativesDB section to another repository."""
    data = rest_request(
        session,
        "POST",
        "/api/v2/narratives/sections/copy",
        json={
            "sectionId": section_id,
            "destinationRepositoryId": destination_repository_id,
        },
    )
    return NarrativeSection.from_api(_object(data, "copied narrative section"))


def list_all_narrative_repository_users(
    session: AuthSession,
    *,
    filter_text: str | None = None,
) -> list[ContentLibraryUser]:
    """List users assigned to NarrativesDB repositories."""
    data = rest_request(
        session,
        "POST",
        "/api/v2/narratives/users/all",
        json=clean({"filterText": filter_text}),
    )
    return [ContentLibraryUser.from_api(item) for item in _items(data, "users")]


def list_narrative_repository_users(
    session: AuthSession,
    narrative_repository_id: int | str,
    *,
    filter_text: str | None = None,
) -> list[ContentLibraryUser]:
    """List users assigned to one NarrativesDB repository."""
    data = rest_request(
        session,
        "POST",
        f"/api/v2/narratives/{narrative_repository_id}/users",
        json=clean({"filterText": filter_text}),
    )
    return [ContentLibraryUser.from_api(item) for item in _items(data, "users")]


def update_narrative_repository_users(
    session: AuthSession,
    narrative_repository_id: int | str,
    users: list[ContentLibraryUserInput],
    *,
    replace: bool = False,
) -> list[ContentLibraryUser]:
    """Add, update, or replace users for one NarrativesDB repository."""
    data = rest_request(
        session,
        "PUT",
        f"/api/v2/narratives/{narrative_repository_id}/users",
        json={
            "replace": replace,
            "repositoryUsers": [user.to_api() for user in users],
        },
    )
    return [ContentLibraryUser.from_api(item) for item in _items(data, "users")]


def get_narrative_repository(
    session: AuthSession,
    narrative_repository_id: int | str,
) -> NarrativeRepository:
    """Get one NarrativesDB repository."""
    data = rest_request(
        session,
        "GET",
        f"/api/v2/narratives/{narrative_repository_id}/getNarrativesRepository",
    )
    return NarrativeRepository.from_api(_object(data, "narrative repository"))


def update_narrative_repository(
    session: AuthSession,
    narrative_repository_id: int | str,
    repository: NarrativeRepositoryInput,
) -> NarrativeRepository:
    """Update one NarrativesDB repository."""
    data = rest_request(
        session,
        "PUT",
        f"/api/v2/narratives/{narrative_repository_id}/updateNarrativesRepository",
        json=repository.to_api(),
    )
    return NarrativeRepository.from_api(_object(data, "narrative repository"))


def delete_narrative_repository(
    session: AuthSession,
    narrative_repository_id: int | str,
) -> OperationResult:
    """Delete one NarrativesDB repository."""
    data = rest_request(
        session,
        "DELETE",
        f"/api/v2/narratives/{narrative_repository_id}/deleteNarrativesRepository",
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def list_writeups(
    session: AuthSession,
) -> list[Writeup]:
    """List WriteupsDB entries."""
    data = rest_request(session, "GET", "/api/v1/template/list")
    return [Writeup.from_api(item) for item in _items(data, "templates")]


def get_writeup(
    session: AuthSession,
    writeup_id: int | str,
) -> Writeup:
    """Get one WriteupsDB entry."""
    data = rest_request(session, "GET", f"/api/v1/template/{writeup_id}")
    return Writeup.from_api(_object(data, "writeup"))


def create_writeup(
    session: AuthSession,
    writeup: WriteupInput,
) -> Writeup:
    """Create a WriteupsDB entry."""
    data = rest_request(
        session,
        "POST",
        "/api/v1/template/create",
        json=writeup.to_api(),
    )
    return Writeup.from_api(_object(data, "writeup"))


def update_writeup(
    session: AuthSession,
    writeup_id: int | str,
    writeup: WriteupInput,
) -> Writeup:
    """Update one WriteupsDB entry."""
    data = rest_request(
        session,
        "PUT",
        f"/api/v1/template/{writeup_id}",
        json=writeup.to_api(),
    )
    return Writeup.from_api(_object(data, "writeup"))


def delete_writeup(
    session: AuthSession,
    writeup_id: int | str,
) -> WriteupDeleteResult:
    """Delete one WriteupsDB entry."""
    data = rest_request(session, "DELETE", f"/api/v1/template/{writeup_id}")
    return WriteupDeleteResult.from_api(data if isinstance(data, dict) else {"data": data})


def bulk_add_writeups_to_report(
    session: AuthSession,
    report_id: int | str,
    writeups: list[Writeup],
) -> OperationResult:
    """Add one or more writeups to a report using the latest bulk endpoint."""
    data = rest_request(
        session,
        "POST",
        "/api/v2/writeups/bulk/addToReport",
        json={
            "reportId": report_id,
            "writeups": [writeup.raw or _writeup_reference(writeup) for writeup in writeups],
        },
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def list_writeups_from_repository(
    session: AuthSession,
    repository_id: int | str,
    *,
    filter_text: str | None = None,
) -> list[Writeup]:
    """List writeups from one WriteupsDB repository."""
    data = rest_request(
        session,
        "POST",
        f"/api/v2/repositories/{repository_id}/getWriteups",
        json=clean({"filterText": filter_text}),
    )
    return [Writeup.from_api(item) for item in _items(data, "writeups")]


def add_writeups_to_repository(
    session: AuthSession,
    repository_id: int | str,
    writeup_ids: list[int | str],
) -> OperationResult:
    """Move writeups into a WriteupsDB repository."""
    data = rest_request(
        session,
        "POST",
        f"/api/v2/repositories/{repository_id}/addWriteups",
        json={"writeups": writeup_ids},
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def import_writeups_to_repository(
    session: AuthSession,
    file: str | Path | BinaryIO,
    *,
    source: WriteupImportSource = WriteupImportSource.CSV,
    filename: str | None = None,
    content_type: str | None = None,
) -> ContentLibraryImportResult:
    """Import WriteupsDB entries from a documented source file."""
    data = _upload_file(
        session,
        f"/api/v2/writeups/import/{source.value}",
        file,
        filename=filename,
        content_type=content_type,
        fallback_name="writeups.csv",
    )
    return ContentLibraryImportResult.from_api(data if isinstance(data, dict) else {"data": data})


def remove_writeups_from_repository(
    session: AuthSession,
    repository_id: int | str,
    writeup_ids: list[int | str],
) -> OperationResult:
    """Remove writeups from one WriteupsDB repository."""
    data = rest_request(
        session,
        "POST",
        f"/api/v2/repositories/{repository_id}/removeWriteup",
        json={"writeups": writeup_ids},
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def bulk_copy_writeups(
    session: AuthSession,
    transfer: WriteupTransfer,
) -> OperationResult:
    """Copy writeups between WriteupsDB repositories."""
    data = rest_request(
        session,
        "POST",
        "/api/v2/writeups/bulk/copy",
        json=transfer.to_api(),
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def bulk_move_writeups(
    session: AuthSession,
    transfer: WriteupTransfer,
) -> OperationResult:
    """Move writeups between WriteupsDB repositories."""
    data = rest_request(
        session,
        "POST",
        "/api/v2/writeups/bulk/move",
        json=transfer.to_api(),
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def bulk_add_tags_to_writeups(
    session: AuthSession,
    writeup_ids: list[int | str],
    tags: list[str],
) -> OperationResult:
    """Add tags to WriteupsDB entries in bulk."""
    data = rest_request(
        session,
        "POST",
        "/api/v2/writeups/bulk/tags",
        json={"writeups": writeup_ids, "tags": tags},
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def bulk_delete_writeups(
    session: AuthSession,
    writeup_doc_ids: list[int | str],
) -> OperationResult:
    """Delete WriteupsDB entries in bulk using documented doc IDs."""
    data = rest_request(
        session,
        "POST",
        "/api/v2/writeups/bulk/delete",
        json={"doc_ids": writeup_doc_ids},
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def list_writeup_repositories(
    session: AuthSession,
) -> list[WriteupRepository]:
    """List WriteupsDB repositories."""
    data = rest_request(
        session,
        "POST",
        "/api/v2/repositories/getAllWriteupsRepositories",
        json={},
    )
    return [WriteupRepository.from_api(item) for item in _items(data, "repositories")]


def list_editable_writeup_repositories(
    session: AuthSession,
) -> list[WriteupRepository]:
    """List WriteupsDB repositories the caller can edit."""
    data = rest_request(session, "GET", "/api/v2/repositories/listUserCanEdit")
    return [WriteupRepository.from_api(item) for item in _items(data, "repositories")]


def get_writeup_repository(
    session: AuthSession,
    repository_id: int | str,
) -> WriteupRepository:
    """Get one WriteupsDB repository."""
    data = rest_request(session, "POST", f"/api/v2/repositories/{repository_id}", json={})
    return WriteupRepository.from_api(_object(data, "writeup repository"))


def create_writeup_repository(
    session: AuthSession,
    repository: WriteupRepositoryInput,
) -> WriteupRepository:
    """Create a WriteupsDB repository."""
    data = rest_request(
        session,
        "POST",
        "/api/v2/repositories/add",
        json=repository.to_api(),
    )
    return WriteupRepository.from_api(_object(data, "writeup repository"))


def update_writeup_repository(
    session: AuthSession,
    repository_id: int | str,
    repository: WriteupRepositoryInput,
) -> WriteupRepository:
    """Update one WriteupsDB repository."""
    data = rest_request(
        session,
        "POST",
        f"/api/v2/repositories/{repository_id}/update",
        json=repository.to_api(),
    )
    return WriteupRepository.from_api(_object(data, "writeup repository"))


def delete_writeup_repository(
    session: AuthSession,
    repository_id: int | str,
) -> OperationResult:
    """Delete one WriteupsDB repository."""
    data = rest_request(
        session,
        "POST",
        "/api/v2/repositories/delete",
        json={"repositoryId": repository_id},
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def list_writeup_repository_users(
    session: AuthSession,
    repository_id: int | str,
) -> list[ContentLibraryUser]:
    """List users assigned to one WriteupsDB repository."""
    data = rest_request(session, "GET", f"/api/v2/repositories/{repository_id}/users")
    return [ContentLibraryUser.from_api(item) for item in _items(data, "users")]


def add_writeup_repository_users(
    session: AuthSession,
    repository_id: int | str,
    users: list[ContentLibraryUserInput],
) -> list[ContentLibraryUser]:
    """Add users to one WriteupsDB repository."""
    data = rest_request(
        session,
        "POST",
        f"/api/v2/repositories/{repository_id}/users",
        json={"users": [user.to_api() for user in users]},
    )
    return [ContentLibraryUser.from_api(item) for item in _items(data, "users")]


def update_writeup_repository_users(
    session: AuthSession,
    repository_id: int | str,
    users: list[ContentLibraryUserInput],
) -> list[ContentLibraryUser]:
    """Replace users assigned to one WriteupsDB repository."""
    data = rest_request(
        session,
        "PUT",
        f"/api/v2/repositories/{repository_id}/users",
        json={"users": [user.to_api() for user in users]},
    )
    return [ContentLibraryUser.from_api(item) for item in _items(data, "users")]


def search_writeup_repository_users(
    session: AuthSession,
    *,
    filter_text: str | None = None,
) -> list[ContentLibraryUser]:
    """Search users eligible for WriteupsDB repository access."""
    data = rest_request(
        session,
        "POST",
        "/api/v2/repositories/users",
        json=clean({"filterText": filter_text}),
    )
    return [ContentLibraryUser.from_api(item) for item in _items(data, "users")]


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


def _items(data: object, key: str) -> list[JsonDict]:
    if isinstance(data, list):
        return [item for item in data if isinstance(item, dict)]
    if isinstance(data, dict):
        nested = data.get(key) or data.get("data") or data.get("items") or data.get("results")
        if isinstance(nested, list):
            return [item for item in nested if isinstance(item, dict)]
        if isinstance(nested, dict):
            return [nested]
    return []


def _object(data: object, label: str) -> JsonDict:
    if isinstance(data, dict):
        nested = data.get("data")
        if isinstance(nested, dict):
            return cast(JsonDict, nested)
        return data
    raise ValueError(f"PlexTrac {label} response was not a JSON object.")


def _writeup_reference(writeup: Writeup) -> JsonDict:
    return clean(
        {
            "id": writeup.writeup_id,
            "doc_id": writeup.doc_id,
            "title": writeup.title,
            "repositoryId": writeup.repository_id,
        }
    )
