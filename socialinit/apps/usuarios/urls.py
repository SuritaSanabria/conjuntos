from django.urls import path
from django.views.generic import TemplateView

from apps.usuarios.views import crear_usuario,agregar_telefono, verificar_exito, verificarTelefono, verificarCorreo


urlpatterns = [
    path('registro/', crear_usuario, name='registro'),
    path('tlf/<int:user_id>/', agregar_telefono, name='editar_telefono'),
    path('tlf/<int:user_id>/verify/', verificarTelefono, name='verificartlf'),
    path('email/<int:user_id>/verify/', verificarCorreo, name='verificaremail'),
    path('success/<str:token>/', verificar_exito, name='verificar_exito'),
]
