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


def registrar_mysql(id_sensor, msj):  
    sql = "INSERT INTO `publicacion_sensor` (`id_sensor_fk`, `valor`) VALUES ('{0}', '{1}')".format(id_sensor, msj)  
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print("error :(")
        
    db.close

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    print("UserData= " + str(userdata))
    print("flags= " + str(flags))
    print("")
    client.subscribe(topic)

def on_message(client, userdata, message):
    msj = str(message.payload.decode("utf-8"))
    print("Mensaje recibido=", msj)
    print("Topic=", message.topic)
    print("Nivel de calidad [0|1|2]=", message.qos)
    print("Flag de retención=", message.retain)
    print("---------------------------------------------")
    print("")
    id_sensor = message.topic.split("/")[-1]
    registrar_mysql(id_sensor, msj)

client = mqtt.Client('Cliente1', userdata="UsuarioDePrueba") 
client.on_connect = on_connect 
client.on_message = on_message 
client.connect(broker_address, broker_port, 60) 
client.loop_forever()