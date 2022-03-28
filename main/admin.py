from django.contrib import admin
from .models import Questionnaire, UserOrganizationInfo


admin.site.register(Questionnaire)
admin.site.register(UserOrganizationInfo)
