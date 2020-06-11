# estructura/urls.py
"""
from django.urls import path

from .views import UserDispositivoListado, UserDispositivoCrear, UserDispositivoActualizar, UserDispositivoDetalle, UserDispositivoEliminar

urlpatterns = [
    path('user_devices/', UserDispositivoListado.as_view(template_name = "user_devices/index.html"), name='leerUserDispositivo'),
    path('user_devices/detalle/<str:pk>', UserDispositivoDetalle.as_view(template_name = "user_devices/detalles.html"), name='detallesUserDispositivo'),
    path('user_devices/crear', UserDispositivoCrear.as_view(template_name = "user_devices/crear.html"), name='crear'),
    path('user_devices/editar/<str:pk>', UserDispositivoActualizar.as_view(template_name = "user_devices/actualizar.html"), name='actualizarUserDispositivo'),
    path('user_devices/eliminar/<str:pk>', UserDispositivoEliminar.as_view(), name='eliminarUserDispositivo'),

]
"""