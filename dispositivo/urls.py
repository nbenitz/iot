# estructura/urls.py
from django.urls import path

from .views import SensorListado, SensorCrear, SensorActualizar, SensorDetalle, SensorEliminar, \
    DispositivoListado, DispositivoCrear, DispositivoActualizar, DispositivoDetalle, DispositivoEliminar
from dispositivo.views import SensorMonitor

urlpatterns = [
    path('sensor/', SensorListado.as_view(template_name = "sensor/index.html"), name='leerSensor'),
    path('sensor/detalle/<str:pk>', SensorDetalle.as_view(template_name = "sensor/detalles.html"), name='detallesSensor'),
    path('sensor/crear', SensorCrear.as_view(template_name = "sensor/crear.html"), name='crearSensor'),
    path('sensor/editar/<str:pk>', SensorActualizar.as_view(template_name = "sensor/actualizar.html"), name='actualizarSensor'),
    path('sensor/eliminar/<str:pk>', SensorEliminar.as_view(), name='eliminarSensor'),

    path('controlador/', DispositivoListado.as_view(template_name = "controlador/index.html"), name='leerDispositivo'),
    path('controlador/detalle/<str:pk>', DispositivoDetalle.as_view(template_name = "controlador/detalles.html"), name='detallesDispositivo'),
    path('controlador/crear', DispositivoCrear.as_view(template_name = "controlador/crear.html"), name='crearDispositivo'),
    path('controlador/editar/<str:pk>', DispositivoActualizar.as_view(template_name = "controlador/actualizar.html"), name='actualizarDispositivo'),
    path('controlador/eliminar/<str:pk>', DispositivoEliminar.as_view(), name='eliminarDispositivor'),

    path('monitor/', SensorMonitor.as_view(template_name = "sensor/monitor3.html"), name='monitorSensor'),

]
