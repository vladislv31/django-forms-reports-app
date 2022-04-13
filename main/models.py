from django.db import models
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError
from django.utils import timezone

import json


class Questionnaire(models.Model):
    TYPE_CHOICES = (
        ('first', 'Анкета первой категории значимости'),
        ('second', 'Анкета второй категории значимости'),
        ('third', 'Анкета третей категории значимости'),
        ('without', 'Анкета без категории значимости'),
        ('determine', 'Анкета определения категории значимости'),
    )
    type = models.CharField(max_length=200, unique=True)
    mode = models.CharField(max_length=200, choices=(('determine', 'Анкета определения категории'), ('simple', 'Обычная анкета')), default='simple')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    fields = models.TextField()

    def __str__(self):
        return f'{self.type}'

    def clean(self):
        try:
            fields = json.loads(self.fields)

            if self.mode != 'determine':
                for field in fields:
                    field_keys = field.keys()

                    for x in ['title', 'designation', 'questions']:
                        if x not in field_keys:
                            raise ValidationError('Not valid fields')

                    if not isinstance(field['questions'], list):
                        raise ValidationError('Not valid fields')

                    for x in field['questions']:
                        if not isinstance(x, dict):
                            raise ValidationError('Not valid fields')

                        question_keys = x.keys()
                        for y in ['number', 'question_text', 'recommendation_text', 'criterion_text']:
                            if y not in question_keys:
                                raise ValidationError('Not valid fields')
            else:
                for field in fields:
                    field_keys = field.keys()

                    for key in ['significance', 'questions']:
                        if key not in field_keys:
                            raise ValidationError('Not valid fields')

                    for question in field['questions']:
                        if not isinstance(question, dict):
                            raise ValidationError('Not valid fields')

                        question_keys = question.keys()
                        for key in ['indicator', 'variants']:
                            if key not in question_keys:
                                raise ValidationError('Not valid fields')

                        for variant in question['variants']:
                            if not isinstance(variant, dict):
                                raise ValidationError('Not valid fields')

                            variant_keys = variant.keys()
                            for key in ['title', 'third_cat_question', 'second_cat_question', 'first_cat_question',
                                        'no_cat_question']:
                                if key not in variant_keys:
                                    raise ValidationError('Not valid fields')
        except ValueError as err:
            raise ValidationError('Not valid JSON')
        except Exception as err:
            raise ValidationError('Not valid JSON')


class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    questionnaire_title = models.CharField(max_length=100)
    report = models.TextField()

    industry = models.CharField(max_length=100)
    type_used_systems = models.CharField(max_length=100)

    done_date = models.DateTimeField(auto_now_add=True)


    def get_done_date(self):
        tz = timezone.get_default_timezone()
        return self.done_date.astimezone(tz).strftime('%d.%m.%Y %H:%M')


class UserOrganizationInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    industry = models.CharField(max_length=100)
    type_used_systems = models.CharField(max_length=100)

    questionnaire_title = models.CharField(max_length=100)
    done_date = models.DateTimeField(auto_now_add=True)

    def get_done_date(self):
        tz = timezone.get_default_timezone()
        return self.done_date.astimezone(tz).strftime('%d.%m.%Y %H:%M')

    def __str__(self):
        return f'{str(self.user).capitalize()}s organization info'

