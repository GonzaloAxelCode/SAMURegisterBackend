from django.db import models

from django.utils import timezone
from apps.diagnostico.models import Diagnostico
from apps.informante_atencion.models import InformanteAtencion
from apps.medico.models import Medico
from apps.paciente.models import Paciente

from apps.personal_medico.models import PersonalMedico


class Atencion(models.Model):
    id_atencion = models.AutoField(primary_key=True)
    tipo_emergencia = models.CharField(max_length=50, null=True, blank=True)
    tipo_atencion = models.CharField(max_length=50, null=True, blank=True)
    traslado = models.BooleanField(default=False)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    referencia = models.CharField(max_length=100, null=True, blank=True)
    sector = models.CharField(max_length=50, null=True, blank=True)
    sub_sector = models.CharField(max_length=50, null=True, blank=True)
    distrito = models.CharField(max_length=50, null=True, blank=True)
    provincia = models.CharField(max_length=50, null=True, blank=True)
    region = models.CharField(max_length=50, null=True, blank=True)
    hora_salida_ambulancia = models.DateTimeField(null=True, blank=True)
    hora_llegada = models.DateTimeField(null=True, blank=True)
    hora_salida = models.DateTimeField(null=True, blank=True)
    hora_llegada_EESS = models.DateTimeField(null=True, blank=True)

    id_personal = models.ForeignKey(PersonalMedico, on_delete=models.CASCADE)
    id_medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    id_diagnostico = models.ForeignKey(Diagnostico, on_delete=models.CASCADE)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    id_informante_atencion = models.ForeignKey(
        InformanteAtencion, on_delete=models.CASCADE)

    activate = models.BooleanField(default=True, null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(null=True, default=None)
    user_updated = models.CharField(max_length=50, null=True, default=None)
