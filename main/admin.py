from django.contrib import admin
from .models import Questionnaire
from django import forms
from django_admin_hstore_widget.forms import HStoreFormField


class SectionAdminForm(forms.ModelForm):

    fields = HStoreFormField()

    class Meta:
        model = Questionnaire
        exclude = ()


@admin.register(Questionnaire)
class SectionAdmin(admin.ModelAdmin):
    form = SectionAdminForm
