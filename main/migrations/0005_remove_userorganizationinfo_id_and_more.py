# Generated by Django 4.0.3 on 2022-03-28 09:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_userorganizationinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userorganizationinfo',
            name='id',
        ),
        migrations.AlterField(
            model_name='userorganizationinfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
