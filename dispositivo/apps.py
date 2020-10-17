from django.apps import AppConfig
from django.utils import timezone

class DispositivoConfig(AppConfig):
    name = 'dispositivo'
    def ready(self):
        from .mqtt_to_database import mqtt_loop
        from .models import Logs
        event = 'MQTT to Database connected OK. Returned code = 0'
        last_pub = Logs.objects.filter(evento=event).last()
        seconds_diff = (timezone.now() - last_pub.fecha).total_seconds()
        print(seconds_diff)
        if seconds_diff > 120:
            mqtt_loop() # startup code here
