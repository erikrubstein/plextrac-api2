from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing import Self

from plextrac_api.types.common import JsonDict, clean


class RunbookTeam(StrEnum):
    RED = "RED"
    BLUE = "BLUE"
    PURPLE = "PURPLE"


@dataclass(slots=True)
class RunbookListArgs:
    limit: int = 25
    offset: int = 0
    search: str | None = None

    def to_api(self) -> JsonDict:
        return clean({"limit": self.limit, "offset": self.offset, "search": self.search})


@dataclass(slots=True)
class RunbookTag:
    tag_id: int | str | None = None
    tag: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> RunbookTag:
        return cls(tag_id=data.get("id"), tag=data.get("tag") or data.get("name"), raw=dict(data))


@dataclass(slots=True)
class RunbookUser:
    user_id: int | str | None = None
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    full_name: str | None = None
    role: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> RunbookUser:
        return cls(
            user_id=data.get("id") or data.get("userId"),
            email=data.get("email"),
            first_name=data.get("firstName") or data.get("first_name"),
            last_name=data.get("lastName") or data.get("last_name"),
            full_name=data.get("fullName") or data.get("name"),
            role=data.get("role") or data.get("permission"),
            raw=dict(data),
        )


@dataclass(slots=True)
class RunbookUserInput:
    user_id: int | str
    role: str | None = None

    def to_api(self) -> JsonDict:
        return clean({"userId": self.user_id, "role": self.role})


@dataclass(slots=True)
class RunbookRecord:
    record_id: int | str | None = None
    name: str | None = None
    short_name: str | None = None
    title: str | None = None
    description: str | None = None
    type: str | None = None
    status: str | None = None
    repository_id: int | str | None = None
    client_id: int | str | None = None
    is_editable: bool | None = None
    updated_at: str | None = None
    deleted_at: str | None = None
    tags: list[RunbookTag] | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> Self:
        tags = data.get("tags")
        client = data.get("client")
        return cls(
            record_id=data.get("id"),
            name=data.get("name"),
            short_name=data.get("shortName") or data.get("short_name"),
            title=data.get("title"),
            description=data.get("description"),
            type=data.get("type"),
            status=data.get("status"),
            repository_id=data.get("repositoryId") or data.get("repository_id"),
            client_id=_id_from(client) or data.get("clientId") or data.get("client_id"),
            is_editable=data.get("isEditable") or data.get("is_editable"),
            updated_at=data.get("updatedAt") or data.get("updated_at"),
            deleted_at=data.get("deletedAt") or data.get("deleted_at"),
            tags=[RunbookTag.from_api(item) for item in tags if isinstance(item, dict)]
            if isinstance(tags, list)
            else None,
            raw=dict(data),
        )


class RunbookRepository(RunbookRecord):
    pass


class RunbookMethodology(RunbookRecord):
    pass


class RunbookTactic(RunbookRecord):
    pass


class RunbookTechnique(RunbookRecord):
    pass


class RunbookProcedure(RunbookRecord):
    pass


class RunbookEngagement(RunbookRecord):
    pass


class RunbookEngagementProcedure(RunbookRecord):
    pass


class RunbookTestPlan(RunbookRecord):
    pass


@dataclass(slots=True)
class RunbookRecordInput:
    name: str
    short_name: str | None = None
    description: str | None = None
    repository_id: int | str | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "name": self.name,
                "shortName": self.short_name,
                "description": self.description,
                "repositoryId": self.repository_id,
            }
        )


@dataclass(slots=True)
class RunbookEngagementInput:
    title: str
    description: str | None = None
    client_id: int | str | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "title": self.title,
                "description": self.description,
                "clientId": self.client_id,
            }
        )


@dataclass(slots=True)
class RunbookExecutionStepInput:
    description: str
    success_criteria: str | None = None
    sort_order: int | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "description": self.description,
                "successCriteria": self.success_criteria,
                "sortOrder": self.sort_order,
            }
        )


@dataclass(slots=True)
class RunbookProcedureLog:
    log_id: int | str | None = None
    engagement_procedure_id: int | str | None = None
    text: str | None = None
    start_date: str | None = None
    end_date: str | None = None
    team: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> RunbookProcedureLog:
        return cls(
            log_id=data.get("id"),
            engagement_procedure_id=data.get("engagementProcedureId"),
            text=data.get("text"),
            start_date=data.get("startDate"),
            end_date=data.get("endDate"),
            team=data.get("team"),
            raw=dict(data),
        )


@dataclass(slots=True)
class RunbookProcedureLogInput:
    text: str
    start_date: str | None = None
    end_date: str | None = None
    team: RunbookTeam | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "text": self.text,
                "startDate": self.start_date,
                "endDate": self.end_date,
                "team": self.team.value if self.team is not None else None,
            }
        )


@dataclass(slots=True)
class RunbookAsset:
    asset_id: int | str | None = None
    name: str | None = None
    hostname: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> RunbookAsset:
        return cls(
            asset_id=data.get("id") or data.get("assetId"),
            name=data.get("name") or data.get("asset"),
            hostname=data.get("hostname"),
            raw=dict(data),
        )


@dataclass(slots=True)
class RunbookAssetInput:
    name: str | None = None
    hostname: str | None = None
    client_asset_id: int | str | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "name": self.name,
                "hostname": self.hostname,
                "clientAssetId": self.client_asset_id,
            }
        )


@dataclass(slots=True)
class RunbookAttachment:
    attachment_id: int | str | None = None
    filename: str | None = None
    content_type: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> RunbookAttachment:
        return cls(
            attachment_id=data.get("id") or data.get("attachmentId"),
            filename=data.get("filename") or data.get("name"),
            content_type=data.get("contentType") or data.get("content_type"),
            raw=dict(data),
        )


@dataclass(slots=True)
class RunbookUploadResult:
    attachment_id: int | str | None = None
    filename: str | None = None
    status: str | None = None
    raw: JsonDict | None = None

    @property
    def ok(self) -> bool:
        return self.attachment_id is not None or self.status == "success"

    @classmethod
    def from_api(cls, data: JsonDict) -> RunbookUploadResult:
        return cls(
            attachment_id=data.get("id") or data.get("attachmentId"),
            filename=data.get("filename") or data.get("name"),
            status=data.get("status"),
            raw=dict(data),
        )


@dataclass(slots=True)
class RunbookImportResult:
    runbook_id: int | str | None = None
    status: str | None = None
    raw: JsonDict | None = None

    @property
    def ok(self) -> bool:
        return self.runbook_id is not None or self.status == "success"

    @classmethod
    def from_api(cls, data: JsonDict) -> RunbookImportResult:
        return cls(
            runbook_id=data.get("runbookId") or data.get("id"),
            status=data.get("status"),
            raw=dict(data),
        )


@dataclass(slots=True)
class RunbookMutationResult:
    result_id: int | str | None = None
    ok: bool = False
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: object) -> RunbookMutationResult:
        if isinstance(data, dict):
            return cls(result_id=data.get("id"), ok=bool(data.get("ok", True)), raw=dict(data))
        return cls(ok=bool(data), raw={"data": data})


def _id_from(value: object) -> int | str | None:
    return value.get("id") if isinstance(value, dict) else None
