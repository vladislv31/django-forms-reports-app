from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.http import HttpResponse, Http404

from django.views.generic.edit import FormView, CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView

from django.views import View

from django.templatetags.static import static

from .forms import MainLoginForm, MainRegisterForm, StartFormForm
from .models import UserOrganizationInfo, Questionnaire, Report

from .mixins import LoginRequiredMixin, StartFormRequiredMixin

from .utils import render_to_pdf

import json


class DoQuestionnaireView(LoginRequiredMixin, StartFormRequiredMixin, View):

    def get(self, request, type_slug):
        if not Questionnaire.objects.filter(type=type_slug).exists():
            return redirect('index')

        questionnaire = Questionnaire.objects.get(type=type_slug)

        template_path = 'main/do_questionnaire_determine.html' if questionnaire.type == 'determine'\
            else 'main/do_questionnaire.html'

        return render(request, template_path, {
            'questionnaire_type': questionnaire.get_type_display(),
            'questionnaire_fields': json.loads(questionnaire.fields)
        })

    def post(self, request, type_slug):
        if not Questionnaire.objects.filter(type=type_slug).exists():
            raise Http404()

        try:
            data = request.POST

            questionnaire = Questionnaire.objects.get(type=type_slug)

            if questionnaire.type != 'determine':
                fields = json.loads(questionnaire.fields)
                report_fields = {}

                for answer_key in filter(lambda x: x.endswith('_answer'), data):
                    field_id, question_id, _ = answer_key.split('_')
                    field_id, question_id = int(field_id) - 1, int(question_id) - 1

                    title = fields[field_id]['title']
                    if title not in report_fields.keys():
                        report_fields[title] = []

                    question = fields[field_id]['questions'][question_id]['question_text']
                    recommendation = fields[field_id]['questions'][question_id]['recommendation_text']
                    answer = data[answer_key]

                    report_fields[title].append({'is_provided': answer == 'provided', 'question': question,
                                                 'recommendation': recommendation})

                report = Report(questionnaire_title=questionnaire.get_type_display(), user=request.user, report=json.dumps(
                    report_fields))
                report.save()

                return HttpResponse(json.dumps({'status': 'ok', 'redirect': str(reverse_lazy('index'))}))
            else:
                determined_category = 'non'

                if len(list(filter(lambda x: x == 'first_cat_question', data.values()))) > 0:
                    determined_category = 'first'
                elif len(list(filter(lambda x: x == 'second_cat_question', data.values()))) > 0:
                    determined_category = 'second'
                elif len(list(filter(lambda x: x == 'third_cat_question', data.values()))) > 0:
                    determined_category = 'third'

                return HttpResponse(json.dumps({'status': 'ok', 'determined_category': determined_category}))
        except Exception as err:
            print(err)
            return HttpResponse(json.dumps({'status': 'error'}))


class QuestionnaireListView(LoginRequiredMixin, StartFormRequiredMixin, ListView):
    model = Questionnaire
    template_name = 'main/index.html'
    context_object_name = 'questionnaires'
    ordering = ['type']


class ReportListView(LoginRequiredMixin, StartFormRequiredMixin, ListView):
    model = Report
    template_name = 'main/report_list.html'
    context_object_name = 'reports'
    ordering = ['-done_date']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['reports'] = context['reports'].filter(user=self.request.user)

        return context


class ReportDownloadView(LoginRequiredMixin, StartFormRequiredMixin, View):

    def get(self, request, report_id):
        if not Report.objects.filter(id=report_id).exists():
            raise Http404()

        report = Report.objects.get(id=report_id)

        context = {'report': report, 'report_fields': json.loads(report.report),
                   'font_path': f'{request.build_absolute_uri(static("main/fonts/tahoma.ttf"))}',
                   'font_bold_path': f'{request.build_absolute_uri(static("main/fonts/tahoma_bold.ttf"))}'}

        for field_key in context['report_fields']:
            fields = context['report_fields'][field_key]
            context['report_fields'][field_key] = {
                'fields': fields,
                'not_provided_count': len(list(filter(lambda x: not x[
                    'is_provided'], context['report_fields'][field_key])))
            }

        pdf = render_to_pdf('main/report_pdf.html', context)

        filename = f'date.pdf'
        content = f'attachment; filename="{filename}"'

        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = content

        return response


class ReportDetailView(LoginRequiredMixin, StartFormRequiredMixin, DetailView):
    model = Report
    template_name = 'main/report_detail.html'
    context_object_name = 'report'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['report_fields'] = json.loads(context['report'].report)

        for field_key in context['report_fields']:
            fields = context['report_fields'][field_key]
            context['report_fields'][field_key] = {
                'fields': fields,
                'not_provided_count': len(list(filter(lambda x: not x[
                    'is_provided'], context['report_fields'][field_key])))
            }

        return context


class StartFormView(LoginRequiredMixin, CreateView):
    template_name = 'main/start_form.html'
    model = UserOrganizationInfo
    form_class = StartFormForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(StartFormView, self).form_valid(form)


class MainLoginView(LoginView):
    template_name = 'main/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    authentication_form = MainLoginForm

    def get_success_url(self):
        if self.request.user.is_superuser:
            return reverse_lazy('admin_panel:questionnaires')

        return reverse_lazy('index')


class MainRegisterView(FormView):
    template_name = 'main/register.html'
    form_class = MainRegisterForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super(MainRegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('login')

        return super(MainRegisterView, self).get(*args, **kwargs)
