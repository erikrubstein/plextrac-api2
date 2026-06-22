from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing import Self

from plextrac_api.types.common import JsonDict, clean


class RunbookTeam(StrEnum):
    RED = "RED"
    BLUE = "BLUE"
    PURPLE = "PURPLE"


class RunbookRepositoryType(StrEnum):
    CURATED = "curated"
    OPEN = "open"


@dataclass(slots=True)
class RunbookListArgs:
    limit: int = 25
    offset: int = 0

    def to_api(self) -> JsonDict:
        return {"pagination": {"limit": self.limit, "offset": self.offset}}


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
            user_id=data.get("userId") or data.get("id"),
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
class RunbookOperatorInput:
    user_id: int | str
    team: RunbookTeam

    def to_api(self) -> JsonDict:
        return {"userId": str(self.user_id), "team": self.team.value}


@dataclass(slots=True)
class RunbookRecord:
    record_id: int | str | None = None
    name: str | None = None
    short_name: str | None = None
    title: str | None = None
    description: str | None = None
    record_type: str | None = None
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
            record_id=data.get("id") or data.get("recordId"),
            name=data.get("name"),
            short_name=data.get("shortName") or data.get("short_name"),
            title=data.get("title"),
            description=data.get("description"),
            record_type=data.get("type") or data.get("recordType"),
            status=data.get("status"),
            repository_id=data.get("repositoryId") or data.get("repository_id"),
            client_id=_id_from(client) or data.get("clientId") or data.get("client_id"),
            is_editable=_first_present(data, ("isEditable", "is_editable")),
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
    record_type: RunbookRepositoryType | str | None = None
    repository_id: int | str | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "name": self.name,
                "shortName": self.short_name,
                "description": self.description,
                "type": self.record_type.value
                if isinstance(self.record_type, RunbookRepositoryType)
                else self.record_type,
                "repositoryId": self.repository_id,
            }
        )


@dataclass(slots=True)
class RunbookEngagementInput:
    title: str
    description: str | None = None
    client_id: int | str | None = None

    def to_api(self, *, include_client_id: bool = True) -> JsonDict:
        payload = {
            "title": self.title,
            "description": self.description,
            "clientId": str(self.client_id) if self.client_id is not None else None,
        }
        if not include_client_id:
            payload["clientId"] = None
        return clean(payload)


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
    start_date: str
    end_date: str | None = None
    team: RunbookTeam | None = None

    def to_api(self, *, include_team: bool = True) -> JsonDict:
        payload = {
            "text": self.text,
            "startDate": self.start_date,
            "endDate": self.end_date,
            "team": self.team.value if self.team is not None else None,
        }
        if not include_team:
            payload["team"] = None
        return clean(payload)


@dataclass(slots=True)
class RunbookAsset:
    procedure_asset_id: int | str | None = None
    client_asset_id: int | str | None = None
    name: str | None = None
    asset_type: str | None = None
    parent_asset_id: int | str | None = None
    criticality: str | None = None
    known_ips: list[str] | None = None
    tags: list[str] | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> RunbookAsset:
        client_asset = data.get("clientAsset")
        source = client_asset if isinstance(client_asset, dict) else data
        return cls(
            procedure_asset_id=data.get("id") or data.get("procedureAssetId"),
            client_asset_id=source.get("id") or data.get("assetId"),
            name=source.get("name") or source.get("asset"),
            asset_type=source.get("type"),
            parent_asset_id=source.get("parentAssetId") or source.get("parent_asset_id"),
            criticality=source.get("criticality"),
            known_ips=source.get("knownIps") if isinstance(source.get("knownIps"), list) else None,
            tags=source.get("tags") if isinstance(source.get("tags"), list) else None,
            raw=dict(data),
        )


@dataclass(slots=True)
class RunbookAssetInput:
    name: str | None = None
    asset_type: str | None = None
    parent_asset_id: int | str | None = None
    criticality: str | None = None
    known_ips: list[str] | None = None
    tags: list[str] | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "name": self.name,
                "type": self.asset_type,
                "parentAssetId": self.parent_asset_id,
                "criticality": self.criticality,
                "knownIps": self.known_ips,
                "tags": self.tags,
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
        return self.attachment_id is not None or self.status in {"ok", "success"}

    @classmethod
    def from_api(cls, data: JsonDict) -> RunbookUploadResult:
        nested = data.get("data") if isinstance(data.get("data"), dict) else {}
        return cls(
            attachment_id=data.get("id") or data.get("attachmentId") or nested.get("id"),
            filename=data.get("filename")
            or data.get("name")
            or nested.get("filename")
            or nested.get("name"),
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
            return cls(
                result_id=data.get("id") or data.get("recordId"),
                ok=bool(data.get("ok", True)),
                raw=dict(data),
            )
        return cls(ok=bool(data), raw={"data": data})


def _id_from(value: object) -> int | str | None:
    return value.get("id") if isinstance(value, dict) else None


def _first_present(data: JsonDict, keys: tuple[str, ...]) -> object:
    for key in keys:
        if key in data:
            return data[key]
    return None
