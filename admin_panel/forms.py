from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User


class AdminCreateForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # fields

        self.fields['username'].widget = forms.widgets.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите логин',
        })
        self.fields['username'].label = 'Логин'

        self.fields['password1'].widget = forms.widgets.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите пароль',
            'type': 'password'
        })
        self.fields['password1'].label = 'Пароль'

        self.fields['password2'].widget = forms.widgets.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Повторите пароль',
            'type': 'password'
        })
        self.fields['password2'].label = 'Повторите пароль'
