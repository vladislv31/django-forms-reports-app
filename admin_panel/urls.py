from django.urls import path
from django.views.generic.base import RedirectView
from .views import QuestionnaireListView


app_name = 'admin_panel'

urlpatterns = [
    path('', RedirectView.as_view(url='questionnaires/'), name='index'),
    path('questionnaires/', QuestionnaireListView.as_view(), name='questionnaires'),
]
