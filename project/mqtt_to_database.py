from dispositivo.models import Sensor, Actuador, Dispositivo, PublicacionSensor, PublicacionActuador, PublicacionControlador, Logs
from django.utils import timezone
import pytz
import paho.mqtt.client as mqtt
# import datetime
import random
import string
# from decouple import config

broker_address = "broker.mqtt-dashboard.com"
broker_port = 1883
topic = "myiot87/#"
client_name = 'myiot87-' + \
    ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
# client_name = config('MQTT_CLIENT', default='myiot87-django')


def registrar_sensor(id_sensor, msg, retain):
    now = timezone.now()
    try:
        sensor = Sensor.objects.get(id=id_sensor)
        last_pub = PublicacionSensor.objects.filter(id_sensor_fk=sensor).last()
        seconds_diff = (now - last_pub.fecha).total_seconds()
        if seconds_diff > 60:
            pub = PublicacionSensor(id_sensor_fk=sensor,
                                    valor=msg, fecha=now, retain=retain)
            pub.save()
    except:
        print("\nError :(\n")


def registrar_feedback(id_actuador, msg, retain):
    now = timezone.now()
    try:
        actuador = Actuador.objects.get(id=id_actuador)
        last_pub = PublicacionActuador.objects.filter(id_actuador_fk=actuador).last()
        seconds_diff = (now - last_pub.fecha).total_seconds()
        if seconds_diff > 60:
            pub = PublicacionActuador(
                id_actuador_fk=actuador, valor=msg, fecha=now, retain=retain)
            pub.save()
    except:
        print("\nError :(\n")


def registrar_status(id_controlador, msg, retain):
    now = timezone.now()
    try:
        controlador = Dispositivo.objects.get(id=id_controlador)
        last_pub = PublicacionControlador.objects.filter(controlador=controlador).last()
        seconds_diff = (now - last_pub.fecha).total_seconds()
        if seconds_diff > 60:
            pub = PublicacionControlador(
                controlador=controlador, valor=msg, fecha=now, retain=retain)
            pub.save()
    except:
        print("\nError :(\n")


def registrar_log(log):
    now = timezone.now()
    try:
        pub = Logs(fecha=now, evento=client_name + " | " + log)
        pub.save()
    except:
        print("\nError :(\n")


def on_connect(client, userdata, flags, rc):
    msg = ""
    if rc == 0:
        msg = "MQTT to Database connected OK. Returned code = " + str(rc)
        print("Connected OK Returned code = " + str(rc))
        print("UserData= " + str(userdata))
        print("flags= " + str(flags))
        print("")
        client.subscribe(topic)
    else:
        msg = "MQTT to Database Bad connection. Returned code = " + str(rc)
        print("Bad connection Returned code=", rc)
    registrar_log(msg)


def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    retain = bool(message.retain)
    print("Mensaje recibido=", msg)
    print("Topic=", message.topic)
    print("Nivel de calidad [0|1|2]=", message.qos)
    print("Flag de retención=", retain)
    print("---------------------------------------------")
    print("")
    topic_parts = message.topic.split('/')
    sub_topic = topic_parts[1]
    id_disp = topic_parts[2]
    print("Topic: ", sub_topic, ",  id: ", id_disp)
    if sub_topic == "sensor":
        registrar_sensor(id_disp, msg, retain)

    if sub_topic == "feedback":
        registrar_feedback(id_disp, msg, retain)

    if sub_topic == "status":
        registrar_status(id_disp, msg, retain)


def on_disconnect(client, userdata, rc):
    registrar_log("Disconnecting. Reason:  " + str(rc))
    # client.connected_flag=False
    # client.disconnect_flag=True


def mqtt_loop():
    print("loop")
    client = mqtt.Client(client_name, userdata="UsuarioServer")
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    try:
        client.connect(broker_address, broker_port, 60)
        client.loop_start()
    except:
        print("\nError en la conexión MQTT.\n")
