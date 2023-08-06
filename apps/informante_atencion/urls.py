from apps.informante_atencion.views import ActivarInformanteAtencionView,  ActualizarInformanteAtencionView,  AgregarInformanteAtencionView, DesactivarInformanteAtencion, InformanteAtencionView
from django.urls import path

urlpatterns = [
    path('get-informantes', InformanteAtencionView.as_view(), name='get-informantes'),
    path('add-informante', AgregarInformanteAtencionView.as_view(),
         name='add-informante'),
    path('update-informante/<int:informante_id>',
         ActualizarInformanteAtencionView.as_view(), name='update-informante'),
    path('informantes/<int:informante_id>/activar/',
         ActivarInformanteAtencionView.as_view(), name='activar_informante'),
    path('informantes/<int:informante_id>/desactivar/',
         DesactivarInformanteAtencion.as_view(), name='desactivar_paciente'),
]
