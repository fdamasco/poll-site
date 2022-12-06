# Generated by Django 4.1.3 on 2022-12-05 00:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0003_question_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='author',
        ),
        migrations.AddField(
            model_name='question',
            name='authors_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Nome do autor'),
        ),
    ]
