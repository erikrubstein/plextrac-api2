from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from plextrac_api.types.common import JsonDict, clean


class ArtifactRelationModel(StrEnum):
    CLIENT = "client"
    REPORT = "report"
    ASSESSMENT_QUESTION = "assessment_question"


@dataclass(slots=True)
class ArtifactRelation:
    model: ArtifactRelationModel
    id: int | str
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> ArtifactRelation | None:
        model = _artifact_relation_model(data.get("model"))
        relation_id = data.get("id")
        if model is None or relation_id is None:
            return None
        return cls(model=model, id=relation_id, raw=dict(data))

    def to_api(self) -> JsonDict:
        return {"model": self.model.value, "id": self.id}


@dataclass(slots=True)
class Artifact:
    artifact_id: str | None = None
    filename: str | None = None
    content_type: str | None = None
    description: str | None = None
    size: int | None = None
    created_at: int | None = None
    components: list[str] | None = None
    relations: list[ArtifactRelation] | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> Artifact:
        relations = data.get("relations")
        return cls(
            artifact_id=data.get("id") or data.get("artifactId"),
            filename=data.get("filename") or data.get("name"),
            content_type=data.get("content_type") or data.get("contentType"),
            description=data.get("description"),
            size=data.get("size") if isinstance(data.get("size"), int) else None,
            created_at=data.get("createdAt"),
            components=data.get("components") if isinstance(data.get("components"), list) else None,
            relations=[
                relation
                for relation in (
                    ArtifactRelation.from_api(item) for item in relations if isinstance(item, dict)
                )
                if relation is not None
            ]
            if isinstance(relations, list)
            else None,
            raw=dict(data),
        )


@dataclass(slots=True)
class ArtifactUploadResult:
    artifact_id: str | None = None
    status: str | None = None
    raw: JsonDict | None = None

    @property
    def ok(self) -> bool:
        return self.status == "ok" or self.artifact_id is not None

    @classmethod
    def from_api(cls, data: JsonDict) -> ArtifactUploadResult:
        nested = data.get("data")
        return cls(
            artifact_id=_artifact_id(nested) or _artifact_id(data),
            status=data.get("status"),
            raw=dict(data),
        )


@dataclass(slots=True)
class TenantImageUploadResult:
    file_url: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> TenantImageUploadResult:
        return cls(file_url=data.get("fileUrl") or data.get("file_url"), raw=dict(data))


def artifact_filter_payload(
    *,
    components: list[str] | None = None,
    relations: list[ArtifactRelation] | None = None,
) -> JsonDict:
    return clean(
        {
            "components": components,
            "relations": [relation.to_api() for relation in relations]
            if relations is not None
            else None,
        }
    )


def _artifact_relation_model(value: object) -> ArtifactRelationModel | None:
    if isinstance(value, ArtifactRelationModel):
        return value
    if isinstance(value, str):
        try:
            return ArtifactRelationModel(value)
        except ValueError:
            return None
    return None


def _artifact_id(data: object) -> str | None:
    if not isinstance(data, dict):
        return None
    value = data.get("id") or data.get("artifactId")
    return str(value) if value is not None else None
