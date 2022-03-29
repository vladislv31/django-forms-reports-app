from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import UserOrganizationInfo


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


class MainRegisterForm(UserCreationForm):

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
            'placeholder': 'Введите пароль повторно',
            'type': 'password'
        })
        self.fields['password2'].label = 'Повторите пароль'


class StartFormForm(forms.ModelForm):

    class Meta:
        model = UserOrganizationInfo
        fields = ['industry', 'type_used_systems']

        widgets = {
            'industry': forms.TextInput(attrs={'class': 'form-control'}),
            'type_used_systems': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'industry': 'Отрасль предприятия',
            'type_used_systems': 'Тип используемых систем',
        }