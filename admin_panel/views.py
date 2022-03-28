from django.shortcuts import redirect
from django.views.generic.list import ListView

from main.models import Questionnaire, UserOrganizationInfo


class UserOrganizationInfoListView(ListView):
    model = UserOrganizationInfo
    template_name = 'admin_panel/start_forms_list.html'
    context_object_name = 'start_forms'


class QuestionnaireListView(ListView):
    model = Questionnaire
    template_name = 'admin_panel/questionnaires.html'
    context_object_name = 'questionnaire'
