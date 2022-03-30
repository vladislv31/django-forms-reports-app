from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, FormView
from django.views import View

from django.shortcuts import render
from django.urls import reverse_lazy

from django.http import HttpResponse
from .models import ParsedDocument

from django.contrib.auth.models import User

from .forms import AdminCreateForm

from main.models import Questionnaire, UserOrganizationInfo

import json


class UserOrganizationInfoListView(ListView):
    model = UserOrganizationInfo
    template_name = 'admin_panel/start_forms_list.html'
    context_object_name = 'start_forms'


class QuestionnaireListView(ListView):
    model = Questionnaire
    template_name = 'admin_panel/questionnaires.html'
    context_object_name = 'questionnaires'
    ordering = ['type']


class QuestionnaireUpdateView(View):

    def get(self, request, type_slug):
        if not Questionnaire.objects.all().filter(type=type_slug).exists():
            return HttpResponse('404')

        questionnaire = Questionnaire.objects.get(type=type_slug)

        return render(request, 'admin_panel/questionnaire_edit.html', {
            'questionnaire_type': questionnaire.get_type_display(),
            'questionnaire_fields': json.loads(questionnaire.fields)
        })

    def post(self, request, type_slug):
        if not Questionnaire.objects.all().filter(type=type_slug).exists():
            return HttpResponse('404')

        try:
            data = request.POST
            fields = []

            for title_key in filter(lambda x: x.endswith('_title'), data):
                _id = title_key.replace('_title', '')

                title = data[title_key]

                designation_key = list(filter(lambda x: x == f'{_id}_designation', data))[0]
                designation = data[designation_key]

                questions = []
                for number_key in filter(lambda x: x.startswith(_id) and x.endswith('_number'), data):
                    inner_id = number_key.split('_')[1]

                    number = data[number_key]

                    question_text_key = list(filter(lambda x: x == f'{_id}_{inner_id}_question', data))[0]
                    question_text = data[question_text_key]

                    questions.append({
                        'number': number,
                        'question_text': question_text
                    })

                fields.append({
                    'title': title,
                    'designation': designation,
                    'questions': questions
                })

            questionnaire = Questionnaire.objects.get(type=type_slug)
            questionnaire.fields = json.dumps(fields)
            questionnaire.save()
        except Exception as err:
            return HttpResponse(json.dumps({'status': 'error'}))

        return HttpResponse(json.dumps({'status': 'ok'}))


class ParsedDocumentListView(ListView):
    model = ParsedDocument
    template_name = 'admin_panel/parsed_document_list.html'
    context_object_name = 'parsed_documents'


class AdminListView(ListView):
    model = User
    template_name = 'admin_panel/admin_list.html'
    context_object_name = 'admins'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['admins'] = context['admins'].filter(is_superuser=True)
        context['admins'] = [admin for admin in context['admins'] if admin.username != str(self.request.user)]

        return context


class AdminCreateView(FormView):
    form_class = AdminCreateForm
    template_name = 'admin_panel/admin_create.html'
    success_url = reverse_lazy('admin_panel:admins')

    def form_valid(self, form):
        admin = form.save()
        admin.is_superuser = True
        admin.save()

        return super(AdminCreateView, self).form_valid(form)


class AdminDeleteView(DeleteView):
    model = User
    template_name = 'admin_panel/admin_delete.html'
    context_object_name = 'admin'
    success_url = reverse_lazy('admin_panel:admins')
