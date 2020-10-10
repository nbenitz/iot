from django.contrib import admin

# Register your models here.
from .models import Dispositivo, Sensor, TipoSensor, Actuador, TipoActuador, PublicacionSensor, \
    PublicacionActuador, PublicacionControlador

admin.site.register(Dispositivo)
admin.site.register(Sensor)
admin.site.register(TipoSensor)
admin.site.register(Actuador)
admin.site.register(TipoActuador)
admin.site.register(PublicacionSensor)
admin.site.register(PublicacionActuador)
admin.site.register(PublicacionControlador)