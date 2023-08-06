
from django.urls import path

from apps.atencion.views import ActivarAtencionView, ActualizarAtencionView, AgregarAtencionView, AtencionConsolidadoView, AtencionView, DesactivarAtencionView

urlpatterns = [
    path('get-atenciones', AtencionView.as_view(), name='get-atenciones'),
    path('add-atencion', AgregarAtencionView.as_view(), name='add-atencion'),
    path('update-atencion/<int:atencion_id>',
         ActualizarAtencionView.as_view(), name='update-atencion'),
    path('atenciones/<int:atencion_id>/activar/',
         ActivarAtencionView.as_view(), name='activar_atencion'),
    path('atenciones/<int:atencion_id>/desactivar/',
         DesactivarAtencionView.as_view(), name='desactivar_atencion'),
    path('atencion_consolidado',
         AtencionConsolidadoView.as_view(), name='consolidad_atencion'),

]
