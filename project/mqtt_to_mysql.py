from .settings import DATABASES
import MySQLdb
import paho.mqtt.client as mqtt
import datetime
#from background_task import background


from functools import reduce
import operator

broker_address = "broker.mqtt-dashboard.com"
broker_port = 1883
topic = "myiot87/#"
#topic = "cetapar.19@gmail.com/#"

def getFromDict(dataDict, mapList):
    return reduce(operator.getitem, mapList, dataDict)  

host = getFromDict(DATABASES, ["default", "HOST"])
user = getFromDict(DATABASES, ["default", "USER"])
password = getFromDict(DATABASES, ["default", "PASSWORD"])
database = getFromDict(DATABASES, ["default", "NAME"])

db = MySQLdb.connect(host, user, password, database)
cursor = db.cursor()


def registrar_sensor_mysql(id_sensor, msg):
    now = datetime.datetime.now()
    sql = "INSERT INTO `publicacion_sensor` (`id_sensor_fk`, `valor`, `fecha`) VALUES ({0}, {1}, '{2}')".format(id_sensor, msg, now.strftime("%Y-%m-%d %H:%M:%S"))  
    #print(sql)
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