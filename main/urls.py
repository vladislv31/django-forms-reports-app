from django.urls import path
from .views import QuestionnaireListView, MainLoginView, MainRegisterView, StartFormView, DoQuestionnaireView, \
    ReportListView, ReportDetailView, ReportDownloadView

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', QuestionnaireListView.as_view(), name='index'),
    path('questionnaire/<slug:type_slug>', DoQuestionnaireView.as_view(), name='do-questionnaire'),

    path('reports/', ReportListView.as_view(), name='reports'),
    path('report/<int:pk>', ReportDetailView.as_view(), name='report'),
    path('report-download/<int:report_id>', ReportDownloadView.as_view(), name='report-download'),

    # path('start-form/', StartFormView.as_view(), name='start-form'),

    path('login/', MainLoginView.as_view(), name='login'),
    path('register/', MainRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
]
