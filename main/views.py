from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic.edit import FormView

from django.contrib.auth.views import LoginView
from django.contrib.auth import login

from .forms import MainLoginForm, MainRegisterForm


def index_view(request):

    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'main/index.html')


class MainLoginView(LoginView):
    template_name = 'main/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    authentication_form = MainLoginForm

    def get_success_url(self):
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
