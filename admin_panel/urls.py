from django.urls import path
from django.views.generic.base import RedirectView
from .views import QuestionnaireListView, QuestionnaireUpdateView, UserOrganizationInfoListView, \
    ParsedDocumentListView, ParseDocumentsView, AdminListView, AdminDeleteView, AdminCreateView, QuestionnaireCreateView, QuestionnaireDeleteView


app_name = 'admin_panel'

urlpatterns = [
    path('', RedirectView.as_view(url='questionnaires/'), name='index'),
    path('start-forms/', UserOrganizationInfoListView.as_view(), name='start-forms'),

    path('parsed-documents/', ParsedDocumentListView.as_view(), name='parsed-documents'),
    path('parse-documents/', ParseDocumentsView.as_view(), name='parse-documents'),

    path('questionnaires/', QuestionnaireListView.as_view(), name='questionnaires'),
    path('create-questionnaire', QuestionnaireCreateView.as_view(), name='create-questionnaire'),
    path('edit-questionnaire/<int:pk>', QuestionnaireUpdateView.as_view(), name='edit-questionnaire'),
    path('delete-questionnaire/<int:pk>', QuestionnaireDeleteView.as_view(), name='delete-questionnaire'),

    path('admins/', AdminListView.as_view(), name='admins'),
    path('create-admin/', AdminCreateView.as_view(), name='create-admin'),
    path('delete-admin/<int:pk>', AdminDeleteView.as_view(), name='delete-admin'),
]
