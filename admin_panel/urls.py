from django.urls import path
from django.views.generic.base import RedirectView
from .views import QuestionnaireListView, UserOrganizationInfoListView, ParsedDocumentListView


app_name = 'admin_panel'

urlpatterns = [
    path('', RedirectView.as_view(url='questionnaires/'), name='index'),
    path('start-forms/', UserOrganizationInfoListView.as_view(), name='start-forms'),
    path('parsed-documents/', ParsedDocumentListView.as_view(), name='parsed-documents'),
    path('questionnaires/', QuestionnaireListView.as_view(), name='questionnaires'),
]
