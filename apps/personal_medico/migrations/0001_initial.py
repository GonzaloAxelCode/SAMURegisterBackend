# Generated by Django 3.1.7 on 2023-07-03 03:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalMedico',
            fields=[
                ('id_personal', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(blank=True, max_length=100, null=True)),
                ('apellidos', models.CharField(blank=True, max_length=100, null=True)),
                ('turno', models.CharField(blank=True, max_length=50, null=True)),
                ('dni', models.CharField(blank=True, max_length=20, null=True)),
                ('salida_cantidad', models.IntegerField(blank=True, null=True)),
                ('activate', models.BooleanField(blank=True, default=True, null=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(default=None, null=True)),
            ],
        ),
    ]
