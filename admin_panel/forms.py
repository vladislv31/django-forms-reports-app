from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.core.exceptions import ValidationError

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

        # error message

        self.error_messages['password_mismatch'] = 'Пароли не совпадают.'

        print(self.error_messages.keys())
        print(self.Meta.model)

    def clean(self):
        cleaned_data = super().clean()

        if User.objects.filter(username=cleaned_data.get('username')).exists():
            raise ValidationError('Пользователь с таким логином уже зарегистрирован!')

        if len(cleaned_data.get('password1')) < 8:
            raise ValidationError('Пароль должен содержать хотя бы 8 символов!')

        if cleaned_data.get('password1').isdigit():
            raise ValidationError('Пароль содержит только цифры!')

