from django.db import models

from django.utils import timezone
from apps.personal_medico.models import PersonalMedico

# Create your models here.


class InformanteAtencion(models.Model):
    id_llamada = models.AutoField(primary_key=True)
    tipo_llamada = models.CharField(max_length=50, null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)
    hora = models.TimeField(null=True, blank=True)
    turno = models.CharField(max_length=50, null=True, blank=True)
    telefono_infor = models.CharField(max_length=20, null=True, blank=True)
    nombres_infor = models.CharField(max_length=50, null=True, blank=True)
    apellidos_infor = models.CharField(max_length=50, null=True, blank=True)
    dni_infor = models.CharField(max_length=20, null=True, blank=True)
    gen_infor = models.CharField(max_length=20, null=True, blank=True)

    id_personal = models.ForeignKey(PersonalMedico, on_delete=models.CASCADE)

    activate = models.BooleanField(default=True, null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(null=True, default=None)
