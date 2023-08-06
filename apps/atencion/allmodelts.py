
'''

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


class Diagnostico(models.Model):
    id_diagnostico = models.AutoField(primary_key=True)
    condicion_antes = models.CharField(max_length=200, null=True, blank=True)
    observaciones = models.CharField(max_length=200, null=True, blank=True)
    condicion_despues = models.CharField(max_length=200, null=True, blank=True)
    derivado_EESS = models.CharField(max_length=100, null=True, blank=True)
    derivado_medico = models.CharField(max_length=100, null=True, blank=True)

    activate = models.BooleanField(default=True, null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(null=True, default=None)


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
'''
