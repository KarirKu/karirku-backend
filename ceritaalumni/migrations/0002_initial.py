# Generated by Django 4.2.8 on 2023-12-04 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ceritaalumni', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ceritaalumni',
            name='alumni',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
