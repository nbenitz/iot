#include <Arduino.h>
#line 1 "/home/desarrollo/Escritorio/capacitacion/iot/hardware/hardware.ino"
#include <WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>

#define DHTPIN 15     // Pin donde está conectado el sensor DHT22
#define DHTTYPE DHT22 // Tipo de sensor DHT

// Parámetros del servidor MQTT
const char *ssid = "Wokwi-GUEST";
const char *password = "";
const char *mqtt_server = "broker.mqttdashboard.com";

const char *sensor_topics[] = {
    "myiot87/sensor/1",
    "myiot87/sensor/2",
    "myiot87/sensor/3",
    "myiot87/sensor/4",
    "myiot87/sensor/5"};

WiFiClient espClient;
PubSubClient client(espClient);
DHT dht(DHTPIN, DHTTYPE);

float prev_values[5] = {0, 0, 0, 0, 0};

// Función de conexión WiFi
#line 27 "/home/desarrollo/Escritorio/capacitacion/iot/hardware/hardware.ino"
void setup_wifi();
#line 42 "/home/desarrollo/Escritorio/capacitacion/iot/hardware/hardware.ino"
void reconnect();
#line 65 "/home/desarrollo/Escritorio/capacitacion/iot/hardware/hardware.ino"
void publish_if_changed(float new_value, float &prev_value, const char *topic);
#line 79 "/home/desarrollo/Escritorio/capacitacion/iot/hardware/hardware.ino"
void setup();
#line 87 "/home/desarrollo/Escritorio/capacitacion/iot/hardware/hardware.ino"
void loop();
#line 27 "/home/desarrollo/Escritorio/capacitacion/iot/hardware/hardware.ino"
void setup_wifi()
{
    Serial.println();
    Serial.print("Connecting to ");
    Serial.println(ssid);
    WiFi.begin(ssid, password, 6);
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(100);
        Serial.print(".");
    }
    Serial.println(" Connected!");
}

// Función de conexión MQTT
void reconnect()
{
    // Loop hasta que se conecte
    while (!client.connected())
    {
        Serial.print("Attempting MQTT connection...");
        // Crear cliente MQTT
        if (client.connect("arduino-weather-demo"))
        {
            Serial.println("connected");
        }
        else
        {
            Serial.print("failed, rc=");
            Serial.print(client.state());
            Serial.println(" try again in 5 seconds");
            // Esperar 5 segundos antes de reintentar
            delay(5000);
        }
    }
}

// Función para publicar si hay cambios
void publish_if_changed(float new_value, float &prev_value, const char *topic)
{
    if (new_value != prev_value)
    {
        String message = String(new_value);
        Serial.print("Reporting to MQTT topic ");
        Serial.print(topic);
        Serial.print(": ");
        Serial.println(message);
        client.publish(topic, message.c_str());
        prev_value = new_value;
    }
}

void setup()
{
    Serial.begin(115200);
    dht.begin();
    setup_wifi();
    client.setServer(mqtt_server, 1883);
}

void loop()
{
    if (!client.connected())
    {
        reconnect();
    }
    client.loop();

    // Medir condiciones meteorológicas
    float voltage = 5.0;
    float wind = dht.readTemperature();
    float pressure = 1005.7;
    float humidity = dht.readHumidity();
    float current = 200.0;

    // Verificar si la lectura es correcta
    if (isnan(wind) || isnan(humidity))
    {
        Serial.println("Failed to read from DHT sensor!");
        return;
    }

    // Crear un array de las lecturas actuales
    float current_values[5] = {voltage, wind, pressure, humidity, current};

    // Publicar si hay cambios
    for (int i = 0; i < 5; i++)
    {
        publish_if_changed(current_values[i], prev_values[i], sensor_topics[i]);
    }

    delay(1000);
}

