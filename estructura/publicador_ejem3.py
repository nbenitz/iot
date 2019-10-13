import paho.mqtt.publish as publish

broker_address = "localhost"
topic = "casa/habitaciones/hab1/luz"
mensaje1 = "Mensaje 1 de un envío multiple"
mensaje2 = "Mensaje 2 de un envío multiple"
mensaje3 = "Mensaje 3 de un envío multiple"

msgs = [{'topic': topic, 'payload': mensaje1},
(topic, mensaje2, 0, False),
(topic, mensaje3, 0, False)]

publish.multiple(msgs, hostname=broker_address)