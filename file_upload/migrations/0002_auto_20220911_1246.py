# Generated by Django 3.2 on 2022-09-11 12:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('file_upload', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadeddata',
            name='user_id',
        ),
        migrations.AddField(
            model_name='uploadeddata',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='userId'),
            preserve_default=False,
        ),
    ]
