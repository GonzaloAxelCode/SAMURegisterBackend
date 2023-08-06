from apps.paciente.views import ActivarPacienteView, ActualizarPacienteView, AgregarPacienteView, DesactivarPacienteView, PacienteView
from django.urls import path

urlpatterns = [
    path('get-pacientes', PacienteView.as_view(), name='get-pacientes'),
    path('add-paciente', AgregarPacienteView.as_view(), name='add-paciente'),
    path('update-paciente/<int:paciente_id>',
         ActualizarPacienteView.as_view(), name='update-paciente'),
    path('pacientes/<int:paciente_id>/activar/',
         ActivarPacienteView.as_view(), name='activar_paciente'),
    path('pacientes/<int:paciente_id>/desactivar/',
         DesactivarPacienteView.as_view(), name='desactivar_paciente'),
]
