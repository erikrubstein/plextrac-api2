from __future__ import annotations

from dataclasses import dataclass

from plextrac_api.types.assets import AffectedAsset
from plextrac_api.types.common import JsonDict


@dataclass(slots=True)
class Identifier:
    name: str | None = None
    id: int | str | None = None
    year: int | None = None
    link: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict | None) -> Identifier | None:
        if not data:
            return None
        return cls(
            name=data.get("name"),
            id=data.get("id"),
            year=data.get("year"),
            link=data.get("link"),
            raw=dict(data),
        )


@dataclass(slots=True)
class CodeSample:
    id: str | None = None
    caption: str | None = None
    code: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict | None) -> CodeSample | None:
        if not data:
            return None
        return cls(
            id=data.get("id"),
            caption=data.get("caption"),
            code=data.get("code"),
            raw=dict(data),
        )


@dataclass(slots=True)
class Finding:
    id: int | str | None = None
    flaw_id: int | str | None = None
    client_id: int | str | None = None
    report_id: int | str | None = None
    title: str | None = None
    description: str | None = None
    severity: str | None = None
    status: str | None = None
    substatus: str | None = None
    substatus_cuid: str | None = None
    assigned_to: str | None = None
    source: str | None = None
    visibility: str | None = None
    selected_score: str | None = None
    tags: list[str] | None = None
    affected_assets: dict[str, AffectedAsset] | None = None
    cves: list[Identifier] | None = None
    cwes: list[Identifier] | None = None
    code_samples: list[CodeSample] | None = None
    created_at: int | None = None
    closed_at: int | None = None
    reopened_at: int | None = None
    last_update: int | None = None
    doc_type: str | None = None
    doc_version: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> Finding:
        common_identifiers = data.get("common_identifiers")
        affected_assets = data.get("affected_assets")
        cves = common_identifiers.get("CVE") if isinstance(common_identifiers, dict) else None
        cwes = common_identifiers.get("CWE") if isinstance(common_identifiers, dict) else None
        code_samples = (
            common_identifiers.get("code_samples") if isinstance(common_identifiers, dict) else None
        )
        return cls(
            id=data.get("id") or data.get("cuid"),
            flaw_id=data.get("flaw_id"),
            client_id=data.get("client_id"),
            report_id=data.get("report_id"),
            title=data.get("title"),
            description=data.get("description"),
            severity=data.get("severity"),
            status=data.get("status"),
            substatus=data.get("subStatus"),
            substatus_cuid=data.get("substatusCuid"),
            assigned_to=data.get("assignedTo"),
            source=data.get("source"),
            visibility=data.get("visibility"),
            selected_score=data.get("selectedScore"),
            tags=data.get("tags") if isinstance(data.get("tags"), list) else None,
            affected_assets={
                key: asset
                for key, asset in (
                    (key, AffectedAsset.from_api(value))
                    for key, value in affected_assets.items()
                    if isinstance(value, dict)
                )
                if asset is not None
            }
            if isinstance(affected_assets, dict)
            else None,
            cves=[item for item in (Identifier.from_api(value) for value in cves or []) if item]
            if isinstance(cves, list)
            else None,
            cwes=[item for item in (Identifier.from_api(value) for value in cwes or []) if item]
            if isinstance(cwes, list)
            else None,
            code_samples=[
                item
                for item in (CodeSample.from_api(value) for value in code_samples or [])
                if item
            ]
            if isinstance(code_samples, list)
            else None,
            created_at=data.get("createdAt"),
            closed_at=data.get("closedAt"),
            reopened_at=data.get("reopenedAt") or data.get("repoenedAt"),
            last_update=data.get("last_update"),
            doc_type=data.get("doc_type"),
            doc_version=data.get("doc_version"),
            raw=dict(data),
        )
