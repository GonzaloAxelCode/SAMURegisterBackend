

from apps.medico.views import ActivarMedicoView, ActualizarMedicoView, AgregarMedicoView, DesactivarMedicoView, MedicoView
from django.urls import path


urlpatterns = [
    path('get-medicos', MedicoView.as_view(),
         name='get-medicos'),
    path('add-medico', AgregarMedicoView.as_view(),
         name='add-medico'),
    path('update-medico/<int:id_medico>', ActualizarMedicoView.as_view(),
         name='update-medico'),
    path('medicos/<int:id_medico>/activar/',
         ActivarMedicoView.as_view(), name='activar_medico'),
    path('medicos/<int:id_medico>/desactivar/',
         DesactivarMedicoView.as_view(), name='desactivar_medico'),
]
