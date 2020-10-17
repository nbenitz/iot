from django.apps import AppConfig

class DispositivoConfig(AppConfig):
    name = 'dispositivo'
    def ready(self):
        from .mqtt_to_database import mqtt_loop
        mqtt_loop() # startup code here
