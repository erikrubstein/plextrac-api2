from __future__ import annotations

from dataclasses import dataclass

from plextrac_api.types.assets import AssetCriticality
from plextrac_api.types.common import JsonDict, clean
from plextrac_api.types.findings import FindingSeverity, FindingStatus


@dataclass(slots=True)
class AnalyticsTags:
    clients: list[str] | None = None
    reports: list[str] | None = None
    findings: list[str] | None = None
    assets: list[str] | None = None
    client_tags_is_union: bool | None = None
    report_tags_is_union: bool | None = None
    finding_tags_is_union: bool | None = None
    asset_tags_is_union: bool | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "clients": self.clients,
                "reports": self.reports,
                "findings": self.findings,
                "assets": self.assets,
                "clientTagsIsUnion": self.client_tags_is_union,
                "reportTagsIsUnion": self.report_tags_is_union,
                "findingTagsIsUnion": self.finding_tags_is_union,
                "assetTagsIsUnion": self.asset_tags_is_union,
            }
        )


@dataclass(slots=True)
class AnalyticsFilter:
    clients: list[int] | None = None
    reports: list[int] | None = None
    assets: list[int | str] | None = None
    tags: AnalyticsTags | None = None
    severities: list[int] | None = None
    statuses: list[FindingStatus] | None = None
    substatuses: list[str] | None = None
    date_from: str | None = None
    date_to: str | None = None
    limit: int | None = None
    offset: int | None = None
    assignees: list[str] | None = None
    cve_ids: list[str] | None = None
    cwe_ids: list[str] | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "clients": self.clients,
                "reports": self.reports,
                "assets": self.assets,
                "tags": self.tags.to_api() if self.tags is not None else None,
                "severities": self.severities,
                "statuses": [status.value for status in self.statuses]
                if self.statuses is not None
                else None,
                "subStatuses": self.substatuses,
                "dateFrom": self.date_from,
                "dateTo": self.date_to,
                "limit": self.limit,
                "offset": self.offset,
                "assignees": self.assignees,
                "cveIDs": self.cve_ids,
                "cweIDs": self.cwe_ids,
            }
        )


@dataclass(slots=True)
class FindingAnalyticsBootstrapFilter:
    clients: list[int] | None = None
    client_tags: list[str] | None = None
    asset_tags: list[str] | None = None
    reports: list[int] | None = None
    report_tags: list[str] | None = None
    finding_tags: list[str] | None = None
    order: list[str] | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "clients": self.clients,
                "clientTags": self.client_tags,
                "assetTags": self.asset_tags,
                "reports": self.reports,
                "reportTags": self.report_tags,
                "findingTags": self.finding_tags,
                "order": self.order,
            }
        )


@dataclass(slots=True)
class AssetAnalyticsFilter:
    clients: list[int] | None = None
    criticality: list[AssetCriticality] | None = None
    finding_severities: list[FindingSeverity] | None = None
    type: list[str] | None = None
    asset_tags: list[str] | None = None
    limit: int | None = None
    offset: int | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "clients": self.clients,
                "criticality": [item.value for item in self.criticality]
                if self.criticality is not None
                else None,
                "findings": {"severity": [item.value for item in self.finding_severities]}
                if self.finding_severities is not None
                else None,
                "type": self.type,
                "tags": {"assets": self.asset_tags} if self.asset_tags is not None else None,
            }
        )


@dataclass(slots=True)
class AnalyticsTrendFilter:
    clients: list[int] | None = None
    reports: list[int] | None = None
    severity: list[FindingSeverity] | None = None
    finding_tags: list[str] | None = None
    report_tags: list[str] | None = None
    age: int | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "clients": self.clients,
                "reports": self.reports,
                "severity": [item.value for item in self.severity]
                if self.severity is not None
                else None,
                "tags": clean({"findings": self.finding_tags, "reports": self.report_tags})
                if self.finding_tags is not None or self.report_tags is not None
                else None,
                "age": self.age,
            }
        )


@dataclass(slots=True)
class SlaAnalyticsFilter:
    clients: list[int] | None = None
    date_from: str | None = None
    date_to: str | None = None
    reports: list[int] | None = None
    finding_severities: list[FindingSeverity] | None = None
    client_tags: list[str] | None = None
    report_tags: list[str] | None = None
    finding_tags: list[str] | None = None
    asset_criticality: list[AssetCriticality] | None = None
    asset_tags: list[str] | None = None
    finding_tags_is_union: bool | None = None
    asset_tags_is_union: bool | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "clients": self.clients,
                "dateFrom": self.date_from,
                "dateTo": self.date_to,
                "reports": self.reports,
                "findingSeverities": [item.value for item in self.finding_severities]
                if self.finding_severities is not None
                else None,
                "clientTags": self.client_tags,
                "reportTags": self.report_tags,
                "findingTags": self.finding_tags,
                "assetCriticality": [item.value for item in self.asset_criticality]
                if self.asset_criticality is not None
                else None,
                "assetTags": self.asset_tags,
                "findingTagsIsUnion": self.finding_tags_is_union,
                "assetTagsIsUnion": self.asset_tags_is_union,
            }
        )


@dataclass(slots=True)
class AnalyticsResult:
    status: str | None = None
    message: str | None = None
    data: JsonDict | list[JsonDict] | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict | list[JsonDict]) -> AnalyticsResult:
        if isinstance(data, dict):
            payload = data.get("data")
            return cls(
                status=data.get("status"),
                message=data.get("message"),
                data=payload if isinstance(payload, (dict, list)) else None,
                raw=dict(data),
            )
        return cls(data=data, raw={"data": data})
