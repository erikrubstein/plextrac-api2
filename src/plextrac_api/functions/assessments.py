"""Generated PlexTrac endpoint functions.

Do not edit by hand. Run scripts/generate_endpoints.py to refresh.
"""

from __future__ import annotations

from typing import Any

from plextrac_api.functions.common import endpoint_request
from plextrac_api.types.auth import AuthSession


def list_questions(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/assessments/questionnaires/{questionnaireId}/questions\n\nPlexTrac endpoint: List Questions"""
    return endpoint_request(session, "assessments", "list_questions", **kwargs)


def get_question(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/assessments/questionnaires/{questionnaireId}/questions/{questionId}\n\nPlexTrac endpoint: Get Question"""
    return endpoint_request(session, "assessments", "get_question", **kwargs)


def create_question(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/assessments/questionnaires/{questionnaireId}/questions\n\nPlexTrac endpoint: Create Question"""
    return endpoint_request(session, "assessments", "create_question", **kwargs)


def update_question(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v2/assessments/questionnaires/{questionnaireId}/questions/{questionId}\n\nPlexTrac endpoint: Update Question"""
    return endpoint_request(session, "assessments", "update_question", **kwargs)


def change_question_order(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v2/assessments/questionnaires/{questionnaireId}/questions/{questionId}/order\n\nPlexTrac endpoint: Change Question Order"""
    return endpoint_request(session, "assessments", "change_question_order", **kwargs)


def delete_question(session: AuthSession, **kwargs: Any) -> Any:
    """DELETE /api/v2/assessments/questionnaires/{questionnaireId}/questions/{questionId}\n\nPlexTrac endpoint: Delete Question"""
    return endpoint_request(session, "assessments", "delete_question", **kwargs)


def list_answer_types(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/tenant/{tenantId}/client/{clientId}/answertypes\n\nPlexTrac endpoint: List Answer Types"""
    return endpoint_request(session, "assessments", "list_answer_types", **kwargs)


def get_answer_type(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/tenant/{tenantId}/client/{clientId}/answertypes/{answerTypeId}\n\nPlexTrac endpoint: Get Answer Type"""
    return endpoint_request(session, "assessments", "get_answer_type", **kwargs)


def update_answer_type(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v2/tenant/{tenantId}/client/{clientId}/answertypes/{answerTypeId}\n\nPlexTrac endpoint: Update Answer Type"""
    return endpoint_request(session, "assessments", "update_answer_type", **kwargs)


def create_answer_type(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/tenant/{tenantId}/client/{clientId}/answertypes/create\n\nPlexTrac endpoint: Create Answer Type"""
    return endpoint_request(session, "assessments", "create_answer_type", **kwargs)


def delete_answer_type(session: AuthSession, **kwargs: Any) -> Any:
    """DELETE /api/v2/tenant/{tenantId}/client/{clientId}/answertypes/{answerTypeId}\n\nPlexTrac endpoint: Delete Answer Type"""
    return endpoint_request(session, "assessments", "delete_answer_type", **kwargs)


def list_questionnaires(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/tenant/{tenantId}/assessments\n\nPlexTrac endpoint: List Questionnaires"""
    return endpoint_request(session, "assessments", "list_questionnaires", **kwargs)


def get_questionnaire(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/assessments/questionnaires/{questionnaireId}\n\nPlexTrac endpoint: Get Questionnaire"""
    return endpoint_request(session, "assessments", "get_questionnaire", **kwargs)


def create_questionnaire(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/assessments/questionnaires\n\nPlexTrac endpoint: Create Questionnaire"""
    return endpoint_request(session, "assessments", "create_questionnaire", **kwargs)


def update_questionnaire(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v2/assessments/questionnaires/{questionnaireId}\n\nPlexTrac endpoint: Update Questionnaire"""
    return endpoint_request(session, "assessments", "update_questionnaire", **kwargs)


def delete_questionnaire(session: AuthSession, **kwargs: Any) -> Any:
    """DELETE /api/v1/tenant/{tenantId}/assessment/{questionnaireId}\n\nPlexTrac endpoint: Delete Questionnaire"""
    return endpoint_request(session, "assessments", "delete_questionnaire", **kwargs)


def export_questionnaire(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/assessments/questionnaires/{questionnaireId}/export\n\nPlexTrac endpoint: Export Questionnaire"""
    return endpoint_request(session, "assessments", "export_questionnaire", **kwargs)


def import_questionnaire(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/import/questionnaire\n\nPlexTrac endpoint: Import Questionnaire"""
    return endpoint_request(session, "assessments", "import_questionnaire", **kwargs)


def list_tenant_assessments(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/tenants/{tenantId}/assessments\n\nPlexTrac endpoint: List Tenant Assessments"""
    return endpoint_request(session, "assessments", "list_tenant_assessments", **kwargs)


def list_client_assessments(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/tenant/{tenantId}/client/{clientId}/assessments\n\nPlexTrac endpoint: List Client Assessments"""
    return endpoint_request(session, "assessments", "list_client_assessments", **kwargs)


def list_client_assessments_filtered(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/tenants/{tenantId}/clients/{clientId}/assessments\n\nPlexTrac endpoint: List Client Assessments (Filtered)"""
    return endpoint_request(session, "assessments", "list_client_assessments_filtered", **kwargs)


def get_client_assessment_with_questions_and_answers(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/tenant/{tenantId}/client/{clientId}/assessment/{assessmentId}\n\nPlexTrac endpoint: Get Client Assessment (with questions and answers)"""
    return endpoint_request(session, "assessments", "get_client_assessment_with_questions_and_answers", **kwargs)


def get_client_assessment(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/tenants/{tenantId}/clients/{clientId}/assessments/{assessmentId}\n\nPlexTrac endpoint: Get Client Assessment"""
    return endpoint_request(session, "assessments", "get_client_assessment", **kwargs)


def get_assessment_by_cuid(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/assessments/{assessmentCuid}\n\nPlexTrac endpoint: Get Assessment by CUID"""
    return endpoint_request(session, "assessments", "get_assessment_by_cuid", **kwargs)


def get_assessment_questions(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/tenants/{tenantId}/clients/{clientId}/assessments/{assessmentId}/questions\n\nPlexTrac endpoint: Get Assessment Questions"""
    return endpoint_request(session, "assessments", "get_assessment_questions", **kwargs)


def get_assessment_answers(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/tenants/{tenantId}/clients/{clientId}/assessments/{assessmentId}/answers\n\nPlexTrac endpoint: Get Assessment Answers"""
    return endpoint_request(session, "assessments", "get_assessment_answers", **kwargs)


def update_assessment_answers(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v2/tenants/{tenantId}/clients/{clientId}/assessments/{assessmentId}/answers\n\nPlexTrac endpoint: Update Assessment Answers"""
    return endpoint_request(session, "assessments", "update_assessment_answers", **kwargs)


def get_assessment_reviewers(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/tenants/{tenantId}/clients/{clientId}/assessments/{assessmentId}/reviewers\n\nPlexTrac endpoint: Get Assessment Reviewers"""
    return endpoint_request(session, "assessments", "get_assessment_reviewers", **kwargs)


def create_client_assessment(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v1/tenant/{tenantId}/client/{clientId}/assessment\n\nPlexTrac endpoint: Create Client Assessment"""
    return endpoint_request(session, "assessments", "create_client_assessment", **kwargs)


def update_client_assessment(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v1/tenant/{tenantId}/client/{clientId}/assessment/{assessmentId}\n\nPlexTrac endpoint: Update Client Assessment"""
    return endpoint_request(session, "assessments", "update_client_assessment", **kwargs)


def delete_client_assessment(session: AuthSession, **kwargs: Any) -> Any:
    """DELETE /api/v1/tenant/{tenantId}/client/{clientId}/assessment/{assessmentId}\n\nPlexTrac endpoint: Delete Client Assessment"""
    return endpoint_request(session, "assessments", "delete_client_assessment", **kwargs)


def create_report_from_assessment_questionnaire(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v1/tenant/{tenantId}/client/{clientId}/assessment/{assessmentId}/report\n\nPlexTrac endpoint: Create Report From Assessment Questionnaire"""
    return endpoint_request(session, "assessments", "create_report_from_assessment_questionnaire", **kwargs)


def copy_asessment_questionnaire(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/tenants/{tenantId}/clients/{clientId}/assessments/{assessmentId}/copy\n\nPlexTrac endpoint: Copy Asessment Questionnaire"""
    return endpoint_request(session, "assessments", "copy_asessment_questionnaire", **kwargs)

