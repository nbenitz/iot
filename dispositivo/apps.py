from django.apps import AppConfig

class DispositivoConfig(AppConfig):
    name = 'dispositivo'
    def ready(self):
        from .mqtt_to_database import mqtt_loop
        print("startup")
        # mqtt_loop() # startup code here
