from django import forms
from django.contrib.auth.forms import AuthenticationForm


class MainLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # fields

        self.fields['username'].widget = forms.widgets.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите логин',
        })
        self.fields['username'].label = 'Логин'

        self.fields['password'].widget = forms.widgets.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите пароль',
            'type': 'password'
        })
        self.fields['password'].label = 'Пароль'

        # error message

        self.error_messages['invalid_login'] = 'Пожалуйста введите корректный логин и пароль.'
        self.error_messages['inactive'] = 'Этот аккаунт не активен в данный момент.'
