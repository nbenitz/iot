# estructura/urls.py

from django.urls import path

from .views import UserDispositivoListado, UserDispositivoCrear, UserDispositivoActualizar, UserDispositivoDetalle, UserDispositivoEliminar, \
    TableroListado, TableroCrear, TableroActualizar, TableroDetalle, TableroEliminar, \
        ajax_tablero_buttons

urlpatterns = [
    path('user-devices/', UserDispositivoListado.as_view(template_name = "user_devices/inicio.html"), name='leerUserDispositivo'),
    path('user-devices/detalle/<str:pk>', UserDispositivoDetalle.as_view(template_name = "user_devices/detalles.html"), name='detallesUserDispositivo'),
    path('user-devices/crear', UserDispositivoCrear.as_view(template_name = "user_devices/crear.html"), name='crearUserDispositivo'),
    path('user-devices/editar/<str:pk>', UserDispositivoActualizar.as_view(template_name = "user_devices/actualizar.html"), name='actualizarUserDispositivo'),
    path('user-devices/eliminar/<str:pk>', UserDispositivoEliminar.as_view(), name='eliminarUserDispositivo'),

    path('', TableroListado.as_view(template_name = "tablero/index.html"), name='leerTablero'),
    path('tablero/detalle/<str:pk>', TableroDetalle.as_view(template_name = "tablero/detalles.html"), name='detallesTablero'),
    path('tablero/crear', TableroCrear.as_view(template_name = "tablero/crear.html"), name='crearTablero'),
    path('tablero/editar/<str:pk>', TableroActualizar.as_view(template_name = "tablero/actualizar.html"), name='actualizarTablero'),
    path('tablero/eliminar/<str:pk>', TableroEliminar.as_view(), name='eliminarTablero'),

    #  ajax_calls
    path('ajax/tablero-buttons/', ajax_tablero_buttons, name='ajax_tablero_buttons'),

]
