# Generated by Django 4.0.3 on 2022-03-28 06:17

import django.contrib.postgres.fields
from django.db import migrations, models
import main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_questionnaire_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='fields',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None), blank=True, null=True, size=None, validators=[main.validators.validate_questionnaire_fields]),
        ),
    ]
