# Generated by Django 4.0.3 on 2022-03-28 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_questionnaire_fields_alter_questionnaire_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionnaire',
            name='designation',
        ),
        migrations.RemoveField(
            model_name='questionnaire',
            name='number',
        ),
        migrations.RemoveField(
            model_name='questionnaire',
            name='security',
        ),
        migrations.RemoveField(
            model_name='questionnaire',
            name='title',
        ),
    ]
