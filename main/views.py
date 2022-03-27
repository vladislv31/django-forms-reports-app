from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic.edit import FormView

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm

from .forms import MainLoginForm


def index_view(request):
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
    form_class = UserCreationForm
    success_url = reverse_lazy('index')

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')

        return super(MainRegisterView, self).get(*args, **kwargs)
