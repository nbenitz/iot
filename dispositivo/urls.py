# estructura/urls.py
from django.urls import path

from .views import SensorListado, SensorCrear, SensorActualizar, SensorDetalle, SensorEliminar

urlpatterns = [
    path('sensor/', SensorListado.as_view(template_name = "sensor/index.html"), name='leerSensor'),
    path('sensor/detalle/<str:pk>', SensorDetalle.as_view(template_name = "sensor/detalles.html"), name='detalles'),
    path('sensor/crear', SensorCrear.as_view(template_name = "sensor/crear.html"), name='crear'),
    path('sensor/editar/<str:pk>', SensorActualizar.as_view(template_name = "sensor/actualizar.html"), name='actualizar'),
    path('sensor/eliminar/<str:pk>', SensorEliminar.as_view(), name='eliminar'),

]
