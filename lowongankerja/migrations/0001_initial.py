# Generated by Django 4.2.7 on 2023-12-04 13:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('informasikarier', '0001_initial'),
        ('user', '0006_alter_user_is_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='LowonganKerja',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('posisi', models.CharField(max_length=64)),
                ('nama_instansi', models.CharField(max_length=64)),
                ('deskripsi', models.TextField()),
                ('eligibilitas', models.TextField()),
                ('tanggal_buka', models.DateTimeField()),
                ('tanggal_tutup', models.DateTimeField()),
                ('link', models.URLField()),
                ('alumni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.alumni')),
                ('karier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informasikarier.karier')),
            ],
        ),
    ]
