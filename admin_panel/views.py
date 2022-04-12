from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, FormView
from django.views import View

from django.shortcuts import render
from django.urls import reverse_lazy

from django.http import HttpResponse, Http404
from .models import ParsedDocument

from django.contrib.auth.models import User

from .forms import AdminCreateForm

from .mixins import GeneralAdminRequired

from main.models import Questionnaire, UserOrganizationInfo

import json

from parser import Parser


class UserOrganizationInfoListView(ListView):
    model = UserOrganizationInfo
    template_name = 'admin_panel/start_forms_list.html'
    context_object_name = 'start_forms'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['industries'] = list(set([sf.industry for sf in context['start_forms']]))
        context['types_used_systems'] = list(set([sf.type_used_systems for sf in context['start_forms']]))

        return context




class QuestionnaireListView(ListView):
    model = Questionnaire
    template_name = 'admin_panel/questionnaires.html'
    context_object_name = 'questionnaires'
    ordering = ['mode']


class QuestionnaireUpdateView(View):

    def get(self, request, pk):
        if not Questionnaire.objects.all().filter(id=pk).exists():
            return Http404()

        questionnaire = Questionnaire.objects.get(id=pk)
        template_path = 'admin_panel/questionnaire_edit.html' if questionnaire.mode != 'determine' else \
            'admin_panel/questionnaire_determine_edit.html'

        return render(request, template_path, {
            'questionnaire_type': questionnaire.type,
            'questionnaire_fields': json.loads(questionnaire.fields)
        })

    def post(self, request, pk):
        if not Questionnaire.objects.all().filter(id=pk).exists():
            raise Http404()

        try:
            data = request.POST
            fields = []

            questionnaire = Questionnaire.objects.get(id=pk)
            questionnaire_type = questionnaire.type

            if questionnaire.type != 'determine':
                questionnaire_type = data['type']

                for title_key in filter(lambda x: x.endswith('_title'), data):
                    _id = title_key.replace('_title', '')

                    title = data[title_key]

                    designation_key = list(filter(lambda x: x == f'{_id}_designation', data))[0]
                    designation = data[designation_key]

                    questions = []
                    for number_key in filter(lambda x: x.startswith(f'{_id}_') and x.endswith('_number'), data):
                        inner_id = number_key.split('_')[1]

                        number = data[number_key]

                        question_text_key = list(filter(lambda x: x == f'{_id}_{inner_id}_question', data))[0]
                        question_text = data[question_text_key]

                        recommendation_text_key = list(filter(lambda x: x == f'{_id}_{inner_id}_recommendation', data))[0]
                        recommendation_text = data[recommendation_text_key]

                        questions.append({
                            'number': number,
                            'question_text': question_text,
                            'recommendation_text': recommendation_text
                        })

                    fields.append({
                        'title': title,
                        'designation': designation,
                        'questions': questions
                    })
            else:
                for significance_key in filter(lambda x: x.endswith('_significance'), data):
                    _id = significance_key.replace('_significance', '')

                    significance = data[significance_key]

                    questions = []
                    for indicator_key in filter(lambda x: x.startswith(f'{_id}_') and x.endswith('_indicator'), data):
                        inner_id = indicator_key.split('_')[1]

                        indicator = data[indicator_key]

                        variants = []
                        for title_key in filter(lambda x: x.startswith(f'{_id}_{inner_id}_') and x.endswith('_title'),
                                                data):
                            variant_id = title_key.split('_')[2]

                            title = data[title_key]

                            first_cat_question = data[f'{_id}_{inner_id}_{variant_id}_first_cat_question']
                            second_cat_question = data[f'{_id}_{inner_id}_{variant_id}_second_cat_question']
                            third_cat_question = data[f'{_id}_{inner_id}_{variant_id}_third_cat_question']
                            no_cat_question = data[f'{_id}_{inner_id}_{variant_id}_no_cat_question']

                            variants.append({
                                'title': title,
                                'first_cat_question': first_cat_question,
                                'second_cat_question': second_cat_question,
                                'third_cat_question': third_cat_question,
                                'no_cat_question': no_cat_question,
                            })

                        questions.append({
                            'indicator': indicator,
                            'variants': variants,
                        })

                    fields.append({
                        'significance': significance,
                        'questions': questions,
                    })

            questionnaire.type = questionnaire_type
            questionnaire.fields = json.dumps(fields)
            questionnaire.full_clean()

            questionnaire.save()
        except Exception as err:
            print(err)
            return HttpResponse(json.dumps({'status': 'error'}))

        return HttpResponse(json.dumps({'status': 'ok'}))


class ParsedDocumentListView(ListView):
    model = ParsedDocument
    template_name = 'admin_panel/parsed_document_list.html'
    context_object_name = 'parsed_documents'


class ParseDocumentsView(View):

    def get(self, request):
        try:
            parser = Parser()
            docs = parser.parse()

            ParsedDocument.objects.all().delete()

            for doc in docs:
                parsed_document = ParsedDocument(title=doc[0], link=doc[1])
                parsed_document.save()
        except Exception as err:
            print(err)
            return HttpResponse(json.dumps({'status': 'error'}))

        return HttpResponse(json.dumps({'status': 'ok'}))


class AdminListView(GeneralAdminRequired, ListView):
    model = User
    template_name = 'admin_panel/admin_list.html'
    context_object_name = 'admins'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['admins'] = context['admins'].filter(is_superuser=True)
        context['admins'] = [admin for admin in context['admins'] if admin.username != str(self.request.user)]

        return context


class AdminCreateView(GeneralAdminRequired, FormView):
    form_class = AdminCreateForm
    template_name = 'admin_panel/admin_create.html'
    success_url = reverse_lazy('admin_panel:admins')

    def form_valid(self, form):
        admin = form.save()
        admin.is_superuser = True
        admin.save()

        return super(AdminCreateView, self).form_valid(form)


class AdminDeleteView(GeneralAdminRequired, DeleteView):
    model = User
    template_name = 'admin_panel/admin_delete.html'
    context_object_name = 'admin'
    success_url = reverse_lazy('admin_panel:admins')
