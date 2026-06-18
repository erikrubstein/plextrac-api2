from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from plextrac_api.types.common import JsonDict, clean
from plextrac_api.types.findings import CommonIdentifiers, FindingField, FindingSeverity


class WriteupImportSource(str, Enum):
    CSV = "csv"


@dataclass(slots=True)
class ContentLibraryUserInput:
    user_id: int | str
    permission_level: str | None = None

    def to_api(self) -> JsonDict:
        return clean({"userId": self.user_id, "permissionLevel": self.permission_level})


@dataclass(slots=True)
class ContentLibraryUser:
    user_id: int | str | None = None
    email: str | None = None
    username: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    full_name: str | None = None
    permission_level: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> ContentLibraryUser:
        return cls(
            user_id=data.get("userId") or data.get("user_id") or data.get("id"),
            email=data.get("email"),
            username=data.get("username"),
            first_name=data.get("firstName") or data.get("first_name"),
            last_name=data.get("lastName") or data.get("last_name"),
            full_name=data.get("fullName") or data.get("full_name") or data.get("name"),
            permission_level=(
                data.get("permissionLevel") or data.get("permission_level") or data.get("role")
            ),
            raw=dict(data),
        )


@dataclass(slots=True)
class NarrativeSectionInput:
    title: str
    repository_id: int | str
    text: str | None = None
    parent_id: int | str | None = None
    order: int | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "title": self.title,
                "repositoryId": self.repository_id,
                "text": self.text,
                "parentId": self.parent_id,
                "order": self.order,
            }
        )


@dataclass(slots=True)
class NarrativeSection:
    section_id: int | str | None = None
    repository_id: int | str | None = None
    title: str | None = None
    text: str | None = None
    parent_id: int | str | None = None
    order: int | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> NarrativeSection:
        return cls(
            section_id=data.get("sectionId") or data.get("section_id") or data.get("id"),
            repository_id=data.get("repositoryId") or data.get("repository_id"),
            title=data.get("title") or data.get("name"),
            text=data.get("text") or data.get("body") or data.get("content"),
            parent_id=data.get("parentId") or data.get("parent_id"),
            order=data.get("order"),
            raw=dict(data),
        )


@dataclass(slots=True)
class NarrativeRepositoryInput:
    name: str
    description: str | None = None
    permission_level: str | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "name": self.name,
                "description": self.description,
                "permissionsLevel": self.permission_level,
            }
        )


@dataclass(slots=True)
class NarrativeRepository:
    repository_id: int | str | None = None
    name: str | None = None
    description: str | None = None
    permission_level: str | None = None
    sections: list[NarrativeSection] | None = None
    users: list[ContentLibraryUser] | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> NarrativeRepository:
        sections = data.get("sections")
        users = data.get("users") or data.get("repositoryUsers")
        return cls(
            repository_id=data.get("repositoryId") or data.get("repository_id") or data.get("id"),
            name=data.get("name") or data.get("title"),
            description=data.get("description"),
            permission_level=data.get("permissionsLevel") or data.get("permissionLevel"),
            sections=[
                NarrativeSection.from_api(item) for item in sections if isinstance(item, dict)
            ]
            if isinstance(sections, list)
            else None,
            users=[ContentLibraryUser.from_api(item) for item in users if isinstance(item, dict)]
            if isinstance(users, list)
            else None,
            raw=dict(data),
        )


@dataclass(slots=True)
class WriteupInput:
    title: str
    repository_id: int | str
    severity: FindingSeverity
    description: str | None = None
    recommendations: str | None = None
    references: str | None = None
    fields: list[FindingField] | None = None
    tags: list[str] | None = None
    risk_score: float | None = None
    calculated_severity: bool | None = None
    common_identifiers: CommonIdentifiers | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "title": self.title,
                "repositoryID": self.repository_id,
                "severity": self.severity.value,
                "description": self.description,
                "recommendations": self.recommendations,
                "references": self.references,
                "fields": [field.to_api() for field in self.fields]
                if self.fields is not None
                else None,
                "tags": self.tags,
                "risk_score": self.risk_score,
                "calculated_severity": self.calculated_severity,
                "common_identifiers": self.common_identifiers.to_api()
                if self.common_identifiers is not None
                else None,
            }
        )


@dataclass(slots=True)
class Writeup:
    writeup_id: int | str | None = None
    doc_id: int | str | None = None
    doc_type: str | None = None
    repository_id: int | str | None = None
    tenant_id: int | str | None = None
    title: str | None = None
    severity: FindingSeverity | None = None
    description: str | None = None
    recommendations: str | None = None
    references: str | None = None
    source: str | None = None
    fields: list[FindingField] | None = None
    tags: list[str] | None = None
    risk_score: float | None = None
    calculated_severity: bool | None = None
    common_identifiers: CommonIdentifiers | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> Writeup:
        fields = data.get("fields")
        tags = data.get("tags")
        risk_score = data.get("risk_score")
        return cls(
            writeup_id=data.get("id"),
            doc_id=data.get("doc_id") or data.get("docId"),
            doc_type=data.get("doc_type") or data.get("docType"),
            repository_id=data.get("repositoryId") or data.get("repositoryID"),
            tenant_id=data.get("tenantId") or data.get("tenant_id"),
            title=data.get("title"),
            severity=_severity(data.get("severity")),
            description=data.get("description"),
            recommendations=data.get("recommendations"),
            references=data.get("references"),
            source=data.get("source"),
            fields=[
                field for field in (FindingField.from_api(item) for item in fields or []) if field
            ]
            if isinstance(fields, list)
            else None,
            tags=[str(item) for item in tags] if isinstance(tags, list) else None,
            risk_score=float(risk_score) if isinstance(risk_score, (int, float)) else None,
            calculated_severity=data.get("calculated_severity"),
            common_identifiers=CommonIdentifiers.from_api(data.get("common_identifiers")),
            raw=dict(data),
        )


@dataclass(slots=True)
class WriteupRepositoryInput:
    name: str
    description: str | None = None

    def to_api(self) -> JsonDict:
        return clean({"name": self.name, "description": self.description})


@dataclass(slots=True)
class WriteupRepository:
    repository_id: int | str | None = None
    name: str | None = None
    description: str | None = None
    writeups: list[Writeup] | None = None
    users: list[ContentLibraryUser] | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> WriteupRepository:
        writeups = data.get("writeups")
        users = data.get("users") or data.get("repositoryUsers")
        return cls(
            repository_id=data.get("repositoryId") or data.get("repository_id") or data.get("id"),
            name=data.get("name") or data.get("title"),
            description=data.get("description"),
            writeups=[Writeup.from_api(item) for item in writeups if isinstance(item, dict)]
            if isinstance(writeups, list)
            else None,
            users=[ContentLibraryUser.from_api(item) for item in users if isinstance(item, dict)]
            if isinstance(users, list)
            else None,
            raw=dict(data),
        )


@dataclass(slots=True)
class WriteupTransfer:
    writeup_ids: list[int | str]
    destination_repository_id: int | str
    source_repository_id: int | str | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "writeups": self.writeup_ids,
                "destinationRepositoryId": self.destination_repository_id,
                "sourceRepositoryId": self.source_repository_id,
            }
        )


@dataclass(slots=True)
class WriteupDeleteResult:
    message: str | None = None
    doc_id: int | str | None = None
    raw: JsonDict | None = None

    @property
    def ok(self) -> bool:
        return self.message == "success" or self.doc_id is not None

    @classmethod
    def from_api(cls, data: JsonDict) -> WriteupDeleteResult:
        return cls(
            message=data.get("message"),
            doc_id=data.get("doc_id") or data.get("docId"),
            raw=dict(data),
        )


@dataclass(slots=True)
class ContentLibraryImportResult:
    status: str | None = None
    message: str | None = None
    import_id: int | str | None = None
    raw: JsonDict | None = None

    @property
    def ok(self) -> bool:
        return self.status == "success" or self.import_id is not None

    @classmethod
    def from_api(cls, data: JsonDict) -> ContentLibraryImportResult:
        return cls(
            status=data.get("status"),
            message=data.get("message"),
            import_id=data.get("import_id") or data.get("importId") or data.get("id"),
            raw=dict(data),
        )


def _severity(value: object) -> FindingSeverity | None:
    if isinstance(value, FindingSeverity):
        return value
    if isinstance(value, str):
        try:
            return FindingSeverity(value)
        except ValueError:
            return None
    return None
