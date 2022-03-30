from django.urls import path
from django.views.generic.base import RedirectView
from .views import QuestionnaireListView, QuestionnaireUpdateView, UserOrganizationInfoListView, \
    ParsedDocumentListView, AdminListView, AdminDeleteView, AdminCreateView


app_name = 'admin_panel'

urlpatterns = [
    path('', RedirectView.as_view(url='questionnaires/'), name='index'),
    path('start-forms/', UserOrganizationInfoListView.as_view(), name='start-forms'),
    path('parsed-documents/', ParsedDocumentListView.as_view(), name='parsed-documents'),

    path('questionnaires/', QuestionnaireListView.as_view(), name='questionnaires'),
    path('edit-questionnaire/<slug:type_slug>', QuestionnaireUpdateView.as_view(), name='edit-questionnaire'),

    path('admins/', AdminListView.as_view(), name='admins'),
    path('create-admin/', AdminCreateView.as_view(), name='create-admin'),
    path('delete-admin/<int:pk>', AdminDeleteView.as_view(), name='delete-admin'),
]
