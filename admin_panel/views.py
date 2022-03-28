from django.views.generic.list import ListView

from main.models import Questionnaire, UserOrganizationInfo
from .models import ParsedDocument


class UserOrganizationInfoListView(ListView):
    model = UserOrganizationInfo
    template_name = 'admin_panel/start_forms_list.html'
    context_object_name = 'start_forms'


class QuestionnaireListView(ListView):
    model = Questionnaire
    template_name = 'admin_panel/questionnaires.html'
    context_object_name = 'questionnaire'


class ParsedDocumentListView(ListView):
    model = ParsedDocument
    template_name = 'admin_panel/parsed_document_list.html'
    context_object_name = 'parsed_documents'
