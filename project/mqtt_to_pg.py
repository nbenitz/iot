from settings import DATABASES
import psycopg2
import paho.mqtt.client as mqtt
import datetime
from functools import reduce
import operator
import random
import string
from django.utils import timezone

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

# connect to the PostgreSQL server
db = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password)

# create a cursor
cursor = db.cursor()

now = timezone.now()
sql = "INSERT INTO `publicacion_sensor` (`id_sensor_fk`, `valor`, `fecha`, `retain`) VALUES ({0}, {1}, '{2}', '{3}')".format(26, '50', now, 1)  
try:
    cursor.execute(sql)
    db.commit()
    print("\nInsert Ok\n")
except:
    db.rollback()
    print("\nerror :(\n")
        
db.close

def registrar_sensor(id_sensor, msg, retain):
    now = timezone.now()
    sql = "INSERT INTO `publicacion_sensor` (`id_sensor_fk`, `valor`, `fecha`, `retain`) VALUES ({0}, {1}, '{2}', '{3}')".format(id_sensor, msg, now, retain)  
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print("\nerror :(\n")
        
    db.close
    
def registrar_feedback_mysql(id_actuador, msg):
    now = datetime.datetime.now()
    sql = "INSERT INTO `publicacion_actuador` (`id_actuador_fk`, `valor`, `fecha`) VALUES ({0}, {1}, '{2}')".format(id_actuador, msg, now.strftime("%Y-%m-%d %H:%M:%S"))  
    #print(sql)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print("error")
        
    db.close

def registrar_log(log):
    now = timezone.now()
    # try:
    #     pub = Logs(fecha=now, evento=log)
    #     pub.save()
    # except:
    #     print("\nError :(\n")

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    print("UserData= " + str(userdata))
    print("flags= " + str(flags))
    print("")
    client.subscribe(topic)

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

    # if sub_topic == "feedback":
    #     registrar_feedback(id_disp, msg, retain)

    # if sub_topic == "status":
    #     registrar_status(id_disp, msg, retain)


def on_disconnect(client, userdata, rc):
    registrar_log("Disconnecting. Reason:  " + str(rc))

#@background(schedule=5)
def mqtt_loop():
    print("loop")
    client = mqtt.Client('Cliente1', userdata="UsuarioServer") 
    client.on_connect = on_connect 
    client.on_message = on_message 
    client.connect(broker_address, broker_port, 60)
    client.loop_start()

if __name__ == '__main__':
    mqtt_loop()
