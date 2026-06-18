"""Generate endpoint metadata from the PlexTrac Postman collection."""

from __future__ import annotations

import json
import keyword
import re
from collections import Counter, defaultdict
from pathlib import Path
from pprint import pformat
from urllib.parse import parse_qsl, urlparse

ROOT = Path(__file__).resolve().parents[1]
COLLECTION_PATH = Path("/tmp/plextrac_postman.json")
PACKAGE_DIR = ROOT / "src" / "plextrac_api"
OUT_DIR = PACKAGE_DIR / "generated"
FUNCTIONS_DIR = PACKAGE_DIR / "functions"
DOCS_DIR = ROOT / "docs"
GENERATED_FUNCTION_GROUPS = {
    "admin",
    "assessments",
    "content_library",
    "graph_ql_mutations",
    "graph_ql_queries",
    "runbooks",
    "users",
}
HAND_WRITTEN_FUNCTION_GROUPS = {
    "affected_assets",
    "analytics",
    "assets",
    "clients",
    "files",
    "findings",
    "integrations",
    "mailer",
    "parser_actions",
    "reports",
    "scheduler",
    "substatus",
    "templates",
    "tenant",
}
VERSION_SUFFIX_RE = re.compile(r"^(?P<base>.+)_v(?P<version>\d+)$")
METHOD_NAME_OVERRIDES = {
    ("Analytics", "retreive_analytics_findings_aging"): "retrieve_analytics_findings_aging",
    (
        "Affected Assets",
        "bulk_create_affected_asset_status",
    ): "bulk_create_affected_asset_status_updates",
    ("Affected Assets", "bulk_get_affected_assets_status"): "bulk_get_affected_asset_statuses",
    ("Affected Assets", "create_affected_asset_status"): "create_affected_asset_status_update",
    ("Affected Assets", "get_affected_asset_status_list"): "list_affected_asset_status_updates",
    ("Affected Assets", "remove_affected_asset_from_flaw"): "remove_affected_asset",
    ("Clients", "available_tenant_users"): "list_available_tenant_users",
    ("Clients", "assign_user_to_client"): "assign_users_to_client",
    ("Clients", "remove_user_from_client"): "remove_users_from_client",
    ("Files", "delete_an_artifact"): "delete_artifact",
    ("Files", "download_an_artifact"): "download_artifact",
    ("Files", "get_artifacts"): "list_artifacts",
    ("Files", "upload_an_artifact_file"): "upload_artifact",
    ("Files", "upload_image_to_tenant"): "upload_tenant_image",
    ("Integrations", "create_configurations"): "create_configuration",
    ("Integrations", "create_jira_ticket_from_findings"): "create_jira_tickets_from_findings",
    ("Integrations", "bulk_update_issue_type_mappings"): "bulk_update_jira_issue_type_mappings",
    ("Integrations", "get_configurations"): "list_configurations",
    ("Integrations", "get_issue_mapping_types"): "list_jira_issue_mappings",
    ("Integrations", "reset_issue_mapping_types"): "reset_jira_issue_mappings",
    ("Integrations", "tenable_io_get_tags"): "list_tenable_io_tags",
    ("Integrations", "tenable_io_sync_tags"): "sync_tenable_io_tags",
    ("Mailer", "get_mailer_templates"): "list_mailer_templates",
    ("Parser Actions", "enable_disable_parser_plugin_actions"): "set_parser_plugin_actions_enabled",
    ("Parser Actions", "get_tenant_parser_actions"): "list_tenant_parser_actions",
    ("Reports", "bulk_add_tags_to_report"): "bulk_add_tags_to_reports",
    ("Reports", "bulk_adjust_status_of_report"): "bulk_update_report_statuses",
    ("Reports", "bulk_assign_reviewers_to_report"): "bulk_assign_reviewers_to_reports",
    ("Reports", "get_exhibit"): "get_report_exhibit",
    ("Reports", "get_report_list"): "list_reports",
    ("Reports", "import_ptrac_report"): "import_report_from_ptrac",
    ("Reports", "search_replace_in_report_occurrences"): "count_report_search_occurrences",
    ("Reports", "search_replace_in_report_replace"): "replace_report_text",
    (
        "Scheduler",
        "create_engagement_schedule_event_artifact",
    ): "upload_engagement_schedule_event_artifact",
    ("Scheduler", "find_many_engagement_schedule_events"): "search_engagement_schedule_events",
    (
        "Scheduler",
        "get_engagement_schedule_event_artifacts",
    ): "list_engagement_schedule_event_artifacts",
    ("Scheduler", "get_engagement_schedule_event_by_id"): "get_engagement_schedule_event",
    ("Substatus", "list_substatus"): "list_substatuses",
    ("Templates", "get_export_template"): "download_export_template",
    ("Templates", "get_findings_template"): "get_finding_template",
    ("Templates", "list_findings_templates"): "list_finding_templates",
    ("Tenant", "add_tenant_logo"): "upload_tenant_logo",
    ("Tenant", "add_tenant_logo_dark"): "upload_tenant_dark_logo",
    ("Tenant", "delete_tenant_icon_dark"): "delete_tenant_dark_icon",
    ("Tenant", "delete_tenant_logo_dark"): "delete_tenant_dark_logo",
    ("Tenant", "root_request"): "get_root_info",
    ("Tenant", "tenant_analytics"): "get_tenant_analytics",
}


def main() -> None:
    collection = json.loads(COLLECTION_PATH.read_text())
    groups = {}
    coverage_rows = []

    for top in collection["item"]:
        display_name = top["name"]
        attr_name = slug(display_name)
        endpoints = list(walk(top, [display_name]))
        generated = generate_group(display_name, endpoints)
        groups[attr_name] = {
            "display_name": display_name,
            "endpoints": generated,
        }
        coverage_rows.append((display_name, attr_name, len(generated)))

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "__init__.py").write_text('"""Generated PlexTrac endpoint metadata."""\n')
    (OUT_DIR / "endpoints.py").write_text(render_python(groups))

    FUNCTIONS_DIR.mkdir(parents=True, exist_ok=True)
    for attr_name, group_data in groups.items():
        if attr_name in GENERATED_FUNCTION_GROUPS:
            (FUNCTIONS_DIR / f"{attr_name}.py").write_text(render_functions(attr_name, group_data))

    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    (DOCS_DIR / "endpoint-coverage.md").write_text(render_coverage(coverage_rows, groups))


def walk(node: dict, path: list[str]):
    if "request" in node:
        yield endpoint_from_item(node, path[:-1])
        return
    for child in node.get("item", []):
        yield from walk(child, path + [child["name"]])


def endpoint_from_item(item: dict, folder_path: list[str]) -> dict:
    request = item["request"]
    path, params = parse_url(request.get("url"))
    body = request.get("body") or {}
    graphql_query = None
    if body.get("mode") == "graphql":
        graphql = body.get("graphql") or {}
        graphql_query = graphql.get("query")

    return {
        "name": item["name"],
        "method": request.get("method", "GET").upper(),
        "path": path,
        "folder_path": folder_path,
        "default_params": params,
        "body_mode": body.get("mode", "none"),
        "description": description_text(request.get("description")),
        "graphql_query": graphql_query,
    }


def parse_url(url: object) -> tuple[str, list[tuple[str, str]]]:
    raw = ""
    params: list[tuple[str, str]] = []

    if isinstance(url, str):
        raw = url
    elif isinstance(url, dict):
        raw = url.get("raw") or ""
        for query in url.get("query") or []:
            key = query.get("key")
            if key:
                params.append((key, str(query.get("value", ""))))
    else:
        return "", []

    if raw:
        try:
            parsed = urlparse(raw)
        except ValueError:
            return normalize_placeholders(raw), params
        if parsed.scheme and parsed.netloc:
            path = parsed.path or "/"
            params = parse_qsl(parsed.query, keep_blank_values=True) or params
        else:
            path, _, query = raw.partition("?")
            params = parse_qsl(query, keep_blank_values=True) or params
    elif isinstance(url, dict):
        path_parts = url.get("path") or []
        path = "/" + "/".join(str(part) for part in path_parts)
    else:
        path = ""

    return normalize_placeholders(path), [
        (key, normalize_placeholders(value)) for key, value in params
    ]


def generate_group(display_name: str, endpoints: list[dict]) -> list[dict]:
    used = Counter()
    group_tokens = token_set(display_name)
    generated = []

    for endpoint in endpoints:
        base = slug(endpoint["name"])
        if not base:
            base = slug(f"{endpoint['method']} {endpoint['path']}")
        base = method_name_override(display_name, base)
        if keyword.iskeyword(base):
            base = f"{base}_"
        used[base] += 1
        method_name = base if used[base] == 1 else f"{base}_{used[base]}"
        versioned_parts = versioned_method_parts(base)
        operation_base = (
            method_name_override(display_name, versioned_parts[0])
            if versioned_parts
            else base
        )

        aliases = aliases_for(method_name, group_tokens)
        endpoint = dict(endpoint)
        endpoint["method_name"] = method_name
        endpoint["operation_base"] = operation_base
        endpoint["aliases"] = aliases
        generated.append(endpoint)

    generated = keep_latest_versions(generated, group_tokens)
    generated = remove_alias_collisions(generated)
    return generated


def keep_latest_versions(endpoints: list[dict], group_tokens: set[str]) -> list[dict]:
    grouped: dict[str, list[tuple[int, dict]]] = defaultdict(list)
    for index, endpoint in enumerate(endpoints):
        key = endpoint.get("operation_base") or endpoint["method_name"]
        grouped[key].append((index, endpoint))

    selected_indexes: set[int] = set()
    canonical_names: dict[int, str] = {}
    for key, candidates in grouped.items():
        winner_index, winner = max(candidates, key=lambda item: version_score(item[1], item[0]))
        selected_indexes.add(winner_index)
        if len(candidates) > 1 or versioned_method_parts(winner["method_name"]):
            canonical_names[winner_index] = key

    kept = []
    used = Counter()
    for index, endpoint in enumerate(endpoints):
        if index not in selected_indexes:
            continue
        endpoint = dict(endpoint)
        method_name = canonical_names.get(index, endpoint["method_name"])
        used[method_name] += 1
        if used[method_name] > 1:
            method_name = f"{method_name}_{used[method_name]}"
        endpoint["method_name"] = method_name
        endpoint["aliases"] = aliases_for(method_name, group_tokens)
        endpoint.pop("operation_base", None)
        kept.append(endpoint)
    return kept


def method_name_override(display_name: str, method_name: str) -> str:
    return METHOD_NAME_OVERRIDES.get((display_name, method_name), method_name)


def versioned_method_parts(method_name: str) -> tuple[str, int] | None:
    match = VERSION_SUFFIX_RE.match(method_name)
    if not match:
        return None
    return match.group("base"), int(match.group("version"))


def version_score(endpoint: dict, index: int) -> tuple[int, int, int, int]:
    parts = versioned_method_parts(endpoint["method_name"])
    declared_version = parts[1] if parts else 0
    path_version, method_preference = endpoint_score(endpoint)
    return declared_version, path_version, method_preference, -index


def aliases_for(method_name: str, group_tokens: set[str]) -> list[str]:
    aliases = []
    for verb in ("list", "get", "create", "update", "delete", "search", "import", "export"):
        prefix = f"{verb}_"
        if not method_name.startswith(prefix):
            continue
        remainder = method_name.removeprefix(prefix)
        remainder_tokens = {
            token
            for token in token_set(remainder)
            if not token.isdigit() and not re.fullmatch(r"v\d+", token)
        }
        if remainder_tokens and remainder_tokens <= group_tokens:
            aliases.append(verb)
    return aliases


def remove_alias_collisions(endpoints: list[dict]) -> list[dict]:
    alias_winners: dict[str, dict] = {}
    grouped: dict[str, list[dict]] = defaultdict(list)
    for endpoint in endpoints:
        for alias in endpoint["aliases"]:
            grouped[alias].append(endpoint)

    for alias, candidates in grouped.items():
        alias_winners[alias] = max(candidates, key=endpoint_score)

    method_names = {endpoint["method_name"] for endpoint in endpoints}
    for endpoint in endpoints:
        endpoint["aliases"] = [
            alias
            for alias in endpoint["aliases"]
            if alias_winners.get(alias) is endpoint
            and alias not in method_names
            and not keyword.iskeyword(alias)
        ]
    return endpoints


def endpoint_score(endpoint: dict) -> tuple[int, int]:
    version = 0
    match = re.search(r"/api/v(\d+)", endpoint["path"])
    if match:
        version = int(match.group(1))
    method_preference = {"GET": 4, "POST": 3, "PUT": 2, "PATCH": 1, "DELETE": 0}
    return version, method_preference.get(endpoint["method"], 0)


def token_set(value: str) -> set[str]:
    tokens = set(slug(value).split("_"))
    expanded = set(tokens)
    for token in tokens:
        if token.endswith("ies"):
            expanded.add(f"{token[:-3]}y")
        if token.endswith("s") and len(token) > 3:
            expanded.add(token[:-1])
    return expanded


def slug(value: str) -> str:
    value = value.replace("Graph QL", "GraphQL").replace("Graph QL", "GraphQL")
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value)
    value = re.sub(r"[^A-Za-z0-9]+", "_", value)
    value = re.sub(r"_+", "_", value).strip("_").lower()
    if value and value[0].isdigit():
        value = f"endpoint_{value}"
    return value


def normalize_placeholders(value: str) -> str:
    return re.sub(r"\{\{([A-Za-z0-9_]+)\}\}", r"{\1}", value)


def description_text(value: object) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        content = value.get("content")
        if isinstance(content, str):
            return content
    return ""


def render_python(groups: dict) -> str:
    body = pformat(groups, sort_dicts=True, width=100)
    return (
        '"""Generated from the public PlexTrac Postman collection.\n\n'
        "Do not edit by hand. Run scripts/generate_endpoints.py to refresh.\n"
        '"""\n\n'
        f"GROUPS = {body}\n"
    )


def render_functions(attr_name: str, group_data: dict) -> str:
    lines = [
        '"""Generated PlexTrac endpoint functions.',
        "",
        "Do not edit by hand. Run scripts/generate_endpoints.py to refresh.",
        '"""',
        "",
        "from __future__ import annotations",
        "",
        "from typing import Any",
        "",
        "from plextrac_api.functions.common import endpoint_request",
        "from plextrac_api.types.auth import AuthSession",
        "",
        "",
    ]
    for endpoint in group_data["endpoints"]:
        method_name = endpoint["method_name"]
        doc = (
            f"{endpoint['method']} {endpoint['path']}\\n\\n"
            f"PlexTrac endpoint: {endpoint['name']}"
        )
        lines.extend(
            [
                f"def {method_name}(session: AuthSession, **kwargs: Any) -> Any:",
                f'    """{doc}"""',
                f'    return endpoint_request(session, "{attr_name}", "{method_name}", **kwargs)',
                "",
                "",
            ]
        )
        for alias in endpoint.get("aliases") or []:
            lines.extend(
                [
                    f"def {alias}(session: AuthSession, **kwargs: Any) -> Any:",
                    f'    """Alias for `{method_name}`."""',
                    f"    return {method_name}(session, **kwargs)",
                    "",
                    "",
                ]
            )
    return "\n".join(lines)


def render_coverage(rows: list[tuple[str, str, int]], groups: dict) -> str:
    total = sum(count for _, _, count in rows)
    lines = [
        "# Endpoint Coverage",
        "",
        "Generated from the public PlexTrac Postman collection snapshot.",
        "",
        "When multiple documented versions expose the same operation, this SDK keeps only the "
        "latest supported version.",
        "",
        f"Total supported endpoint functions in snapshot: **{total}**",
        "",
        "| API group | Function module | Endpoint functions |",
        "|---|---|---:|",
    ]
    for display_name, attr_name, count in rows:
        module_label = coverage_module_label(attr_name)
        count_label = coverage_count_label(attr_name, count)
        lines.append(
            f"| {display_name} | {module_label} | {count_label} |"
        )

    lines.extend(["", "## Method Inventory", ""])
    for attr_name, data in groups.items():
        lines.extend([f"### `{attr_name}`", "", f"Display name: {data['display_name']}", ""])
        lines.append("| Method | HTTP | Path | Aliases |")
        lines.append("|---|---|---|---|")
        for endpoint in data["endpoints"]:
            aliases = ", ".join(f"`{alias}`" for alias in endpoint["aliases"]) or ""
            lines.append(
                f"| `{endpoint['method_name']}` | {endpoint['method']} | "
                f"`{endpoint['path']}` | {aliases} |"
            )
        lines.append("")
    return "\n".join(lines)


def coverage_module_label(attr_name: str) -> str:
    if attr_name in GENERATED_FUNCTION_GROUPS:
        return f"`plextrac_api.functions.{attr_name}`"
    if attr_name in HAND_WRITTEN_FUNCTION_GROUPS:
        return f"`plextrac_api.functions.{attr_name}`"
    if attr_name == "authentication":
        return "`plextrac_api.functions.auth`"
    if attr_name == "webhooks":
        return "`plextrac_api.functions.webhooks`"
    return "_not generated_"


def coverage_count_label(attr_name: str, count: int) -> str:
    if attr_name in GENERATED_FUNCTION_GROUPS:
        return str(count)
    if attr_name in HAND_WRITTEN_FUNCTION_GROUPS:
        return f"{count} explicit functions"
    if attr_name == "authentication":
        return "manual auth helpers"
    if attr_name == "webhooks":
        return "manual receiver helper"
    return str(count)


if __name__ == "__main__":
    main()
