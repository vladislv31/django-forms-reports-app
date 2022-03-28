from django.urls import path
from .views import QuestionnaireListView, MainLoginView, MainRegisterView, StartFormView, do_questionnaire_view

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', QuestionnaireListView.as_view(), name='index'),
    path('questionnaire/<slug:type_slug>', do_questionnaire_view, name='do-questionnaire'),
    path('start-form/', StartFormView.as_view(), name='start-form'),
    path('login/', MainLoginView.as_view(), name='login'),
    path('register/', MainRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
]
