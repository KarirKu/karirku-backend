# Generated by Django 4.2.8 on 2023-12-04 13:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Karier',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=100)),
                ('deskripsi_pekerjaan', models.TextField()),
                ('kompetensi', models.CharField(max_length=255)),
                ('tanggung_jawab', models.CharField(max_length=255)),
            ],
        ),
    ]
