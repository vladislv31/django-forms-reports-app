# Generated by Django 4.0.3 on 2022-04-13 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_questionnaire_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
