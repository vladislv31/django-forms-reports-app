# Generated by Django 4.0.3 on 2022-04-12 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_questionnaire_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='mode',
            field=models.CharField(choices=[('determine', ''), ('simple', '')], default='simple', max_length=200),
        ),
    ]
