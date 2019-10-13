import paho.mqtt.publish as publish

broker_address = "localhost"
topic = "casa/habitaciones/hab1/luz"
publish.single(topic, "Ejemplo de publicador simple desde Python", hostname=broker_address,
client_id='publicador_ejem2.py')