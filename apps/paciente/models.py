from django.db import models

from django.utils import timezone


class Paciente(models.Model):
    paciente_id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    genero = models.CharField(max_length=20)
    dni = models.CharField(max_length=15)
    tipo_seguro = models.CharField(max_length=50, blank=True, null=True)
    empresa_aseguradora = models.CharField(
        max_length=50, blank=True, null=True, default=None)
    edad = models.IntegerField()
    tipo_edad = models.CharField(max_length=20, blank=True, null=True)
    prioridad_emergencia = models.CharField(
        max_length=20, blank=True, null=True)
    accidente = models.CharField(max_length=20, blank=True, null=True)
    condicion_antes = models.TextField(blank=True, null=True)
    condicion_despues = models.TextField(blank=True, null=True)
    tipo_edad = models.CharField(max_length=20, blank=True, null=True)
    telefono_paciente = models.CharField(max_length=20, blank=True, null=True)

    activate = models.BooleanField(default=True, null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(null=True, default=None)

    def __str__(self):
        return self.nombres
