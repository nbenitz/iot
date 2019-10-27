# estructura/urls.py
from django.urls import path

from .views import SensorListado, SensorCrear, SensorActualizar, SensorDetalle, SensorEliminar
from dispositivo.views import SensorMonitor

urlpatterns = [
    path('sensor/', SensorListado.as_view(template_name = "sensor/index.html"), name='leerSensor'),
    path('sensor/detalle/<str:pk>', SensorDetalle.as_view(template_name = "sensor/detalles.html"), name='detallesSensor'),
    path('sensor/crear', SensorCrear.as_view(template_name = "sensor/crear.html"), name='crearSensor'),
    path('sensor/editar/<str:pk>', SensorActualizar.as_view(template_name = "sensor/actualizar.html"), name='actualizarSensor'),
    path('sensor/eliminar/<str:pk>', SensorEliminar.as_view(), name='eliminarSensor'),

    path('monitor/', SensorMonitor.as_view(template_name = "sensor/monitor.html"), name='monitorSensor'),

]
