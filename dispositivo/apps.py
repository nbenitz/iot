from django.apps import AppConfig

class DispositivoConfig(AppConfig):
    name = 'dispositivo'
    # def ready(self):
    #     from .mqtt_to_database import mqtt_loop
    #     from .models import Logs
    #     from django.utils import timezone
    #     event = 'MQTT to Database connected OK. Returned code = 0'
    #     last_pub = Logs.objects.filter(evento=event).last()
    #     if last_pub:          
    #         seconds_diff = (timezone.now() - last_pub.fecha).total_seconds()
    #         if seconds_diff > 120:
    #             mqtt_loop()
    #     else:
    #         mqtt_loop()
       
            
