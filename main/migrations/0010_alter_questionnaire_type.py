# Generated by Django 4.0.3 on 2022-03-28 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_questionnaire_fields_alter_questionnaire_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='type',
            field=models.CharField(choices=[('first', 'Анкета первой категории значимости'), ('second', 'Анкета второй категории значимости'), ('third', 'Анкета третей категории значимости'), ('without', 'Анкета без категории значимости')], max_length=200, unique=True),
        ),
    ]