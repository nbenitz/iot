# estructura/urls.py
from django.urls import path

from .views import SensorListado, SensorCrear, SensorActualizar, SensorDetalle, SensorEliminar, \
    ActuadorListado, ActuadorCrear, ActuadorActualizar, ActuadorDetalle, ActuadorEliminar, \
        DispositivoListado, DispositivoCrear, DispositivoActualizar, DispositivoDetalle, DispositivoEliminar, \
            TipoSensorListado, TipoSensorCrear, TipoSensorActualizar, TipoSensorDetalle, TipoSensorEliminar, \
                TipoActuadorListado, TipoActuadorCrear, TipoActuadorActualizar, TipoActuadorDetalle, TipoActuadorEliminar, \
                    ajax_controlador_detalle, ajax_controlador_actualizar, SensorPubListado, ajax_sensor_pubs
from dispositivo.views import SensorMonitor, SensorMonitor2

urlpatterns = [
    path('controlador/', DispositivoListado.as_view(template_name = "controlador/index.html"), name='leerDispositivo'),
    path('controlador/detalle/<str:pk>', DispositivoDetalle.as_view(template_name = "controlador/detalles.html"), name='detallesDispositivo'),
    path('controlador/crear', DispositivoCrear.as_view(template_name = "controlador/crear.html"), name='crearDispositivo'),
    path('controlador/editar/<str:pk>', DispositivoActualizar.as_view(template_name = "controlador/actualizar.html"), name='actualizarDispositivo'),
    path('controlador/eliminar/<str:pk>', DispositivoEliminar.as_view(), name='eliminarDispositivo'),

    path('sensor/', SensorListado.as_view(template_name = "sensor/index.html"), name='leerSensor'),
    path('sensor/detalle/<str:pk>', SensorDetalle.as_view(template_name = "sensor/detalles.html"), name='detallesSensor'),
    path('sensor/crear', SensorCrear.as_view(template_name = "sensor/crear.html"), name='crearSensor'),
    path('sensor/editar/<str:pk>', SensorActualizar.as_view(template_name = "sensor/actualizar.html"), name='actualizarSensor'),
    path('sensor/eliminar/<str:pk>', SensorEliminar.as_view(), name='eliminarSensor'),

    path('actuador/', ActuadorListado.as_view(template_name = "actuador/index.html"), name='leerActuador'),
    path('actuador/detalle/<str:pk>', ActuadorDetalle.as_view(template_name = "actuador/detalles.html"), name='detallesActuador'),
    path('actuador/crear', ActuadorCrear.as_view(template_name = "actuador/crear.html"), name='crearActuador'),
    path('actuador/editar/<str:pk>', ActuadorActualizar.as_view(template_name = "actuador/actualizar.html"), name='actualizarActuador'),
    path('actuador/eliminar/<str:pk>', ActuadorEliminar.as_view(), name='eliminarActuador'),

    path('tipo-sensor/', TipoSensorListado.as_view(template_name = "tipo-sensor/index.html"), name='leerTipoSensor'),
    path('tipo-sensor/detalle/<str:pk>', TipoSensorDetalle.as_view(template_name = "tipo-sensor/detalles.html"), name='detallesTipoSensor'),
    path('tipo-sensor/crear', TipoSensorCrear.as_view(template_name = "tipo-sensor/crear.html"), name='crearTipoSensor'),
    path('tipo-sensor/editar/<str:pk>', TipoSensorActualizar.as_view(template_name = "tipo-sensor/actualizar.html"), name='actualizarTipoSensor'),
    path('tipo-sensor/eliminar/<str:pk>', TipoSensorEliminar.as_view(), name='eliminarSensor'),

    path('tipo-actuador/', TipoActuadorListado.as_view(template_name = "tipo-actuador/index.html"), name='leerTipoActuador'),
    path('tipo-actuador/detalle/<str:pk>', TipoActuadorDetalle.as_view(template_name = "tipo-actuador/detalles.html"), name='detallesTipoActuador'),
    path('tipo-actuador/crear', TipoActuadorCrear.as_view(template_name = "tipo-actuador/crear.html"), name='crearTipoActuador'),
    path('tipo-actuador/editar/<str:pk>', TipoActuadorActualizar.as_view(template_name = "tipo-actuador/actualizar.html"), name='actualizarTipoActuador'),
    path('tipo-actuador/eliminar/<str:pk>', TipoActuadorEliminar.as_view(), name='eliminarTipoActuador'),

    path('monitor/', SensorMonitor.as_view(template_name = "sensor/monitor2.html"), name='monitorSensor'),
    path('monitor-example/', SensorMonitor2.as_view(template_name = "sensor/monitor3.html"), name='monitorSensor2'),

    path('sensor/pub/<str:id_sensor>', SensorPubListado.as_view(template_name = "pub-sensor/index.html"), name='leerSensorPub'),

    #  ajax_calls
    path('ajax/controller-details/<int:pk>', ajax_controlador_detalle, name='ajax_controller_detail'),
    path('ajax/controller-edit/<int:pk>', ajax_controlador_actualizar, name='ajax_controller_edit'),

    path('ajax/sensor-pubs/<int:id_sensor>', ajax_sensor_pubs, name='ajax_sensor_pub'),

]
