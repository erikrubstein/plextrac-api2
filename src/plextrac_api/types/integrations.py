from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from plextrac_api.types.common import JsonDict, clean


class JiraSyncFrequency(StrEnum):
    HALF_HOUR = "Half_Hour"
    HOURLY = "Hourly"
    DAILY = "Daily"


class JiraProjectMappingType(StrEnum):
    DEFAULT = "Default"
    CUSTOM = "Custom"


class IntegrationConfigurationType(StrEnum):
    COBALT = "Colbalt"
    HACKER_ONE = "HackerOne"
    MSV = "MSV"
    SNYK = "Snyk"


@dataclass(slots=True)
class IntegrationSettings:
    product: str
    enabled: bool | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, product: str, data: JsonDict) -> IntegrationSettings:
        return cls(product=product, enabled=data.get("enabled"), raw=dict(data))


@dataclass(slots=True)
class TenableTag:
    id: int | str | None = None
    name: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> TenableTag:
        return cls(id=data.get("id") or data.get("uuid"), name=data.get("name"), raw=dict(data))


@dataclass(slots=True)
class JiraConnectionInput:
    url: str | None = None
    username: str | None = None
    api_token: str | None = None
    sync_frequency: JiraSyncFrequency | None = None
    name: str | None = None

    def to_api(self) -> JsonDict:
        sync_frequency = self.sync_frequency.value if self.sync_frequency is not None else None
        return clean(
            {
                "url": self.url,
                "username": self.username,
                "apiToken": self.api_token,
                "syncFrequency": sync_frequency,
                "name": self.name,
            }
        )


@dataclass(slots=True)
class JiraConnection:
    integration_id: int | str | None = None
    name: str | None = None
    url: str | None = None
    sync_frequency: JiraSyncFrequency | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> JiraConnection:
        return cls(
            integration_id=data.get("integrationId") or data.get("id"),
            name=data.get("name"),
            url=data.get("url"),
            sync_frequency=_sync_frequency(data.get("syncFrequency")),
            raw=dict(data),
        )


@dataclass(slots=True)
class JiraProject:
    project_id: int | str | None = None
    key: str | None = None
    name: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> JiraProject:
        return cls(
            project_id=data.get("id") or data.get("projectId"),
            key=data.get("key"),
            name=data.get("name"),
            raw=dict(data),
        )

    def to_api(self) -> JsonDict:
        return clean({"id": self.project_id, "key": self.key, "name": self.name})


@dataclass(slots=True)
class JiraIssueMappingInput:
    source: str
    destination: str
    direction: str | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "source": self.source,
                "destination": self.destination,
                "direction": self.direction,
            }
        )


@dataclass(slots=True)
class JiraIssueTypeMappingInput:
    jira_project_id: int | str
    jira_issue_type_id: int | str
    mappings: list[JiraIssueMappingInput]

    def to_api(self) -> JsonDict:
        return {
            "jiraProjectId": self.jira_project_id,
            "jiraIssueTypeId": self.jira_issue_type_id,
            "mappings": [mapping.to_api() for mapping in self.mappings],
        }


@dataclass(slots=True)
class JiraIssueMapping:
    source: str | None = None
    destination: str | None = None
    direction: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> JiraIssueMapping:
        return cls(
            source=data.get("source"),
            destination=data.get("destination"),
            direction=data.get("direction"),
            raw=dict(data),
        )


@dataclass(slots=True)
class JiraTicketCreateResult:
    status: str | None = None
    message: str | None = None
    ticket_ids: list[str] | None = None
    raw: JsonDict | None = None

    @property
    def ok(self) -> bool:
        return self.status == "success" or bool(self.ticket_ids)

    @classmethod
    def from_api(cls, data: JsonDict) -> JiraTicketCreateResult:
        tickets = data.get("ticketIds") or data.get("tickets")
        return cls(
            status=data.get("status"),
            message=data.get("message"),
            ticket_ids=[str(ticket) for ticket in tickets] if isinstance(tickets, list) else None,
            raw=dict(data),
        )


@dataclass(slots=True)
class IntegrationConfigurationInput:
    integration_type: IntegrationConfigurationType
    api_key: str
    api_username: str | None = None
    org_id: str | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "integrationType": self.integration_type.value,
                "apiKey": self.api_key,
                "apiUserName": self.api_username,
                "orgId": self.org_id,
            }
        )


@dataclass(slots=True)
class IntegrationConfiguration:
    config_id: int | str | None = None
    integration_type: IntegrationConfigurationType | None = None
    api_username: str | None = None
    org_id: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> IntegrationConfiguration:
        return cls(
            config_id=data.get("configId") or data.get("id"),
            integration_type=_configuration_type(data.get("integrationType")),
            api_username=data.get("apiUserName"),
            org_id=data.get("orgId"),
            raw=dict(data),
        )


def _sync_frequency(value: object) -> JiraSyncFrequency | None:
    if isinstance(value, JiraSyncFrequency):
        return value
    if isinstance(value, str):
        try:
            return JiraSyncFrequency(value)
        except ValueError:
            return None
    return None


def _configuration_type(value: object) -> IntegrationConfigurationType | None:
    if isinstance(value, IntegrationConfigurationType):
        return value
    if isinstance(value, str):
        try:
            return IntegrationConfigurationType(value)
        except ValueError:
            return None
    return None
