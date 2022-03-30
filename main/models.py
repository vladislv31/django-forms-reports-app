from django.db import models
from django.contrib.auth.models import User

from .validators import validate_questionnaire_fields


class Questionnaire(models.Model):
    TYPE_CHOICES = (
        ('first', 'Анкета первой категории значимости'),
        ('second', 'Анкета второй категории значимости'),
        ('third', 'Анкета третей категории значимости'),
        ('without', 'Анкета без категории значимости'),
    )
    type = models.CharField(max_length=200, choices=TYPE_CHOICES, unique=True)

    fields = models.TextField(validators=[validate_questionnaire_fields])

    def __str__(self):
        return f'{self.get_type_display()}'


class Report(models.Model):
    questionnaire_title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report = models.TextField()
    done_date = models.DateTimeField(auto_now_add=True)


class UserOrganizationInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    industry = models.CharField(max_length=100)
    type_used_systems = models.CharField(max_length=100)

    def __str__(self):
        return f'{str(self.user).capitalize()}s organization info'
