from django.db import models


class Questionnaire(models.Model):
    designation = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    security = models.CharField(max_length=200)

    title = models.CharField(max_length=200)

    type = (
        ('start', 'Старторая анкета'),
        ('first', 'Анкета первой категории значимости'),
        ('second', 'Анкета второй категории значимости'),
        ('third', 'Анкета третей категории значимости'),
        ('without', 'Анкета без категории значимости'),
        ('determine', 'Анкета определения категории значимости'),
    )

    fields = models.TextField()
