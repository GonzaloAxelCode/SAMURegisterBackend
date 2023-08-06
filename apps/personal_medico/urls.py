from django.urls import path
from .views import ActivarPersonalMedicoView, ActualizarPersonalMedicoView, AgregarPersonalMedicoView, DesactivarPersonalMedicoView, PersonalMedicoView

urlpatterns = [
    path('get-personal', PersonalMedicoView.as_view(), name='get-personal'),
    path('add-personal', AgregarPersonalMedicoView.as_view(), name='add-personal'),
    path('update-personal/<int:id_personal>',
         ActualizarPersonalMedicoView.as_view(), name='update-personal'),
    path('personal/<int:id_personal>/activar/',
         ActivarPersonalMedicoView.as_view(), name='activar_personal'),
    path('personal/<int:id_personal>/desactivar/',
         DesactivarPersonalMedicoView.as_view(), name='desactivar_personal'),
]
