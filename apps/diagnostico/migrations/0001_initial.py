# Generated by Django 3.1.7 on 2023-07-03 03:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id_diagnostico', models.AutoField(primary_key=True, serialize=False)),
                ('condicion_antes', models.CharField(blank=True, max_length=200, null=True)),
                ('observaciones', models.CharField(blank=True, max_length=200, null=True)),
                ('condicion_despues', models.CharField(blank=True, max_length=200, null=True)),
                ('derivado_EESS', models.CharField(blank=True, max_length=100, null=True)),
                ('derivado_medico', models.CharField(blank=True, max_length=100, null=True)),
                ('activate', models.BooleanField(blank=True, default=True, null=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(default=None, null=True)),
            ],
        ),
    ]