import settings
import MySQLdb
import paho.mqtt.client as mqtt


from functools import reduce
import operator
#from project.settings import DATABASES

broker_address = "test.mosquitto.org"
broker_port = 1883
topic = "yonestor87@gmail.com/#"
#topic = "cetapar.19@gmail.com/#"

def getFromDict(dataDict, mapList):
    return reduce(operator.getitem, mapList, dataDict)  

host = getFromDict(settings.DATABASES, ["default", "HOST"])
user = getFromDict(settings.DATABASES, ["default", "USER"])
password = getFromDict(settings.DATABASES, ["default", "PASSWORD"])
database = getFromDict(settings.DATABASES, ["default", "NAME"])

db = MySQLdb.connect(host, user, password, database)
cursor = db.cursor()


def registrar_sensor_mysql(id_sensor, msg):  
    sql = "INSERT INTO `publicacion_sensor` (`id_sensor_fk`, `valor`) VALUES ('{0}', '{1}')".format(id_sensor, msg)  
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print("\nerror :(\n")
        
    db.close
    
def registrar_feedback_mysql(id_actuador, msg):  
    sql = "INSERT INTO `publicacion_actuador` (`id_actuador_fk`, `valor`) VALUES ('{0}', '{1}')".format(id_actuador, msg)  
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print("")
        
    db.close

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
    if sub_topic == "sensor":
        registrar_sensor_mysql(id_sensor, msg)
        
    if sub_topic == "feedback":
        registrar_feedback_mysql(id_sensor, msg)

client = mqtt.Client('Cliente1', userdata="UsuarioDePrueba") 
client.on_connect = on_connect 
client.on_message = on_message 
client.connect(broker_address, broker_port, 60) 
client.loop_forever()