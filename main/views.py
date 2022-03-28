from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic.edit import FormView, CreateView
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView

from .forms import MainLoginForm, MainRegisterForm, StartFormForm
from .models import UserOrganizationInfo, Questionnaire

from .mixins import LoginRequiredMixin, StartFormRequired


def do_questionnaire_view(request, type_slug):
    return render(request, template_name='main/do_questionnaire.html')


class QuestionnaireListView(LoginRequiredMixin, StartFormRequired, ListView):
    model = Questionnaire
    template_name = 'main/index.html'
    context_object_name = 'questionnaires'
    ordering = ['type']


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
