from apps.diagnostico.views import ActivarDiagnosticoView, ActualizarDiagnosticoView, AgregarDiagnosticoView, DesactivarDiagnosticoView, DiagnosticoView
from django.urls import path

urlpatterns = [
    path('get-diagnosticos', DiagnosticoView.as_view(), name='get-diagnosticos'),
    path('add-diagnostico', AgregarDiagnosticoView.as_view(), name='add-diagnostico'),
    path('update-diagnostico/<int:diagnostico_id>',
         ActualizarDiagnosticoView.as_view(), name='update-diagnostico'),
    path('diagnosticos/<int:diagnostico_id>/activar/',
         ActivarDiagnosticoView.as_view(), name='activar_diagnostico'),
    path('diagnosticos/<int:diagnostico_id>/desactivar/',
         DesactivarDiagnosticoView.as_view(), name='desactivar_diagnostico'),
]
