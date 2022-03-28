from django.shortcuts import redirect
from django.views.generic.list import ListView

from main.models import Questionnaire


class QuestionnaireListView(ListView):
    model = Questionnaire
    template_name = 'admin_panel/questionnaires.html'
    context_object_name = 'questionnaire'
