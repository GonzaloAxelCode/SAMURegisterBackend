from django.db import models

from django.utils import timezone

# Create your models here.


class Diagnostico(models.Model):
    id_diagnostico = models.AutoField(primary_key=True)
    codigo = models.CharField(
        max_length=200, null=True, blank=True, unique=True)
    condicion_antes = models.CharField(max_length=200, null=True, blank=True)
    observaciones = models.CharField(max_length=200, null=True, blank=True)
    condicion_despues = models.CharField(max_length=200, null=True, blank=True)
    derivado_EESS = models.CharField(max_length=100, null=True, blank=True)
    derivado_medico = models.CharField(max_length=100, null=True, blank=True)

    activate = models.BooleanField(default=True, null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(null=True, default=None)
