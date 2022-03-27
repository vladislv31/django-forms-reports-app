from django.db import models
from django.contrib.postgres.fields import ArrayField

from .validators import validate_questionnaire_fields


class Questionnaire(models.Model):
    designation = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    security = models.CharField(max_length=200)

    title = models.CharField(max_length=200)

    TYPE_CHOICES = (
        ('start', 'Старторая анкета'),
        ('first', 'Анкета первой категории значимости'),
        ('second', 'Анкета второй категории значимости'),
        ('third', 'Анкета третей категории значимости'),
        ('without', 'Анкета без категории значимости'),
        ('determine', 'Анкета определения категории значимости'),
    )
    type = models.CharField(max_length=200, choices=TYPE_CHOICES, blank=True, null=True)

    fields = ArrayField(ArrayField(models.TextField()), blank=True, null=True, validators=[validate_questionnaire_fields])

    def __str__(self):
        return f'{self.title} - {self.get_type_display()}'
