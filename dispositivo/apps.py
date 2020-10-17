from django.apps import AppConfig

class DispositivoConfig(AppConfig):
    name = 'dispositivo'
    def ready(self):
        from .mqtt_to_database import mqtt_loop
        from project.config import mqtt_run
        if not mqtt_run:
            mqtt_loop() # startup code here
            mqtt_run = True
