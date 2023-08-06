from django.db import models

from django.utils import timezone
# Create your models here.


class PersonalMedico(models.Model):
    id_personal = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100, null=True, blank=True)
    apellidos = models.CharField(max_length=100, null=True, blank=True)
    turno = models.CharField(max_length=50, null=True, blank=True)
    dni = models.CharField(max_length=20, null=True, blank=True)
    salida_cantidad = models.IntegerField(null=True, blank=True)

    activate = models.BooleanField(default=True, null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(null=True, default=None)
