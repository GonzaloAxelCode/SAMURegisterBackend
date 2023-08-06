from django.db import models
from django.utils import timezone

# Create your models here.


class Medico(models.Model):
    id_medico = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100, null=True)
    apellidos = models.CharField(max_length=100, null=True)
    n_colegiatura = models.CharField(max_length=50, null=True)
    dni = models.CharField(max_length=20, null=True)
    telefono = models.CharField(max_length=20, null=True)
    activate = models.BooleanField(default=True, null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(null=True, default=None)
