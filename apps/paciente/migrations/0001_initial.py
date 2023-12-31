# Generated by Django 3.1.7 on 2023-07-03 03:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('paciente_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=20)),
                ('dni', models.CharField(max_length=15)),
                ('tipo_seguro', models.CharField(blank=True, max_length=50, null=True)),
                ('empresa_aseguradora', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('edad', models.IntegerField()),
                ('prioridad_emergencia', models.CharField(blank=True, max_length=20, null=True)),
                ('accidente', models.CharField(blank=True, max_length=20, null=True)),
                ('condicion_antes', models.TextField(blank=True, null=True)),
                ('condicion_despues', models.TextField(blank=True, null=True)),
                ('tipo_edad', models.CharField(blank=True, max_length=20, null=True)),
                ('telefono_paciente', models.CharField(blank=True, max_length=20, null=True)),
                ('activate', models.BooleanField(blank=True, default=True, null=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(default=None, null=True)),
            ],
        ),
    ]
