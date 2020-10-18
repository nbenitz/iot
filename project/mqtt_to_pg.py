from .settings import DATABASES
import psycopg2
import paho.mqtt.client as mqtt
import datetime
import pytz
from functools import reduce
import operator
import random
import string

broker_address = "broker.mqtt-dashboard.com"
broker_port = 1883
topic = "myiot87/#"
client_name = 'myiot87-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))

def getFromDict(dataDict, mapList):
    return reduce(operator.getitem, mapList, dataDict)  

host = getFromDict(DATABASES, ["default", "HOST"])
user = getFromDict(DATABASES, ["default", "USER"])
password = getFromDict(DATABASES, ["default", "PASSWORD"])
database = getFromDict(DATABASES, ["default", "NAME"])

db = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password)

cursor = db.cursor()

def registrar_sensor(id_sensor, msg, retain):
    now = datetime.datetime.now().astimezone(pytz.timezone('UTC'))
    sql = "INSERT INTO publicacion_sensor (id_sensor_fk, valor, fecha, retain) VALUES(%s, %s, %s, %s)"
    try:
        cursor.execute(sql, (id_sensor, msg, now.strftime("%Y-%m-%d %H:%M:%S"), bool(retain)))
        db.commit()
    except:
        db.rollback()
        print("\nerror :(\n")

    db.close
    
def registrar_feedback(id_actuador, msg, retain):
    now = datetime.datetime.now().astimezone(pytz.timezone('UTC'))
    sql = "INSERT INTO publicacion_actuador (id_actuador_fk, valor, fecha, retain) VALUES(%s, %s, %s, %s)"
    try:
        cursor.execute(sql, (id_actuador, msg, now.strftime("%Y-%m-%d %H:%M:%S"), bool(retain)))
        db.commit()
    except:
        db.rollback()
        print("error")
        
    db.close

def registrar_status(id_controlador, msg, retain):
    now = datetime.datetime.now().astimezone(pytz.timezone('UTC'))
    sql = "INSERT INTO publicacion_controlador (controlador, valor, fecha, retain) VALUES(%s, %s, %s, %s)"
    try:
        cursor.execute(sql, (id_controlador, msg, now.strftime("%Y-%m-%d %H:%M:%S"), bool(retain)))
        db.commit()
    except:
        db.rollback()
        print("error")
        
    db.close

def registrar_log(log):
    now = datetime.datetime.now().astimezone(pytz.timezone('UTC'))
    sql = "INSERT INTO logs (fecha, evento) VALUES(%s, %s)"
    try:
        cursor.execute(sql, (now.strftime("%Y-%m-%d %H:%M:%S"), log))
        db.commit()
    except:
        db.rollback()
        print("error")
        
    db.close

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
        registrar_log("Error en la conexión MQTT.")

# if __name__ == '__main__':
#     mqtt_loop()
