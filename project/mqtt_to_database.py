from dispositivo.models import Sensor, Actuador, PublicacionSensor, PublicacionActuador
import paho.mqtt.client as mqtt
import datetime

broker_address = "broker.mqtt-dashboard.com"
broker_port = 1883
topic = "myiot87/#"


def registrar_sensor(id_sensor, msg):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        sensor = Sensor.objects.get(id=id_sensor)
        pub = PublicacionSensor(id_sensor_fk=sensor, valor=msg, fecha=now)
        pub.save()
    except:
        print("\nError :(\n")
        
    
def registrar_feedback(id_actuador, msg):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        actuador = Actuador.objects.get(id=id_actuador)
        pub = PublicacionActuador(id_actuador_fk=actuador, valor=msg, fecha=now)
        pub.save()
    except:
        print("\nError :(\n")

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    print("UserData= " + str(userdata))
    print("flags= " + str(flags))
    print("")
    client.subscribe(topic)

def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    print("Mensaje recibido=", msg)
    print("Topic=", message.topic)
    print("Nivel de calidad [0|1|2]=", message.qos)
    print("Flag de retención=", message.retain)
    print("---------------------------------------------")
    print("")
    topic_parts = message.topic.split('/')
    sub_topic = topic_parts[1]
    id_sensor = topic_parts[2]
    print("Topic: ", sub_topic, ",  id: ", id_sensor)
    if sub_topic == "sensor":
        registrar_sensor(id_sensor, msg)
        
    if sub_topic == "feedback":
        registrar_feedback(id_sensor, msg)



#@background(schedule=5)
def mqtt_loop():
    print("loop")
    client = mqtt.Client('Cliente1', userdata="UsuarioServer") 
    client.on_connect = on_connect 
    client.on_message = on_message 
    client.connect(broker_address, broker_port, 60)
    client.loop_start()    

#mqtt_loop()
#print("ok")