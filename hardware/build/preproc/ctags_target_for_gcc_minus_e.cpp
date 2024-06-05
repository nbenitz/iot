# 1 "/home/desarrollo/Escritorio/capacitacion/iot/hardware/hardware.ino"
# 2 "/home/desarrollo/Escritorio/capacitacion/iot/hardware/hardware.ino" 2
# 3 "/home/desarrollo/Escritorio/capacitacion/iot/hardware/hardware.ino" 2
# 4 "/home/desarrollo/Escritorio/capacitacion/iot/hardware/hardware.ino" 2




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

NetworkClient espClient;
PubSubClient client(espClient);
DHT dht(15 /* Pin donde está conectado el sensor DHT22*/, DHT22 /* Tipo de sensor DHT*/);

float prev_values[5] = {0, 0, 0, 0, 0};

// Función de conexión WiFi
void setup_wifi()
{
    Serial0.println();
    Serial0.print("Connecting to ");
    Serial0.println(ssid);
    WiFi.begin(ssid, password, 6);
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(100);
        Serial0.print(".");
    }
    Serial0.println(" Connected!");
}

// Función de conexión MQTT
void reconnect()
{
    // Loop hasta que se conecte
    while (!client.connected())
    {
        Serial0.print("Attempting MQTT connection...");
        // Crear cliente MQTT
        if (client.connect("arduino-weather-demo"))
        {
            Serial0.println("connected");
        }
        else
        {
            Serial0.print("failed, rc=");
            Serial0.print(client.state());
            Serial0.println(" try again in 5 seconds");
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
        Serial0.print("Reporting to MQTT topic ");
        Serial0.print(topic);
        Serial0.print(": ");
        Serial0.println(message);
        client.publish(topic, message.c_str());
        prev_value = new_value;
    }
}

void setup()
{
    Serial0.begin(115200);
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
        Serial0.println("Failed to read from DHT sensor!");
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
