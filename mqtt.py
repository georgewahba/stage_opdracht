import paho.mqtt.client as mqtt

# informatie om te connecten aan de MQTT broker (username en password via input zoat niemand erbij kan)
mqtt_host = "b-f84435c1-82a1-406e-86b0-60bd06dc1598-1.mq.eu-central-1.amazonaws.com"
mqtt_port = 8883
mqtt_topic = "tele/tasmota_48551917CE6C/SENSOR"
mqtt_connection_type = "ssl"
mqtt_username = input("Enter username: ")
mqtt_password = input("Enter password: ")


def on_connect(client, userdata, flags, rc):

    print(f"Connected with result code {rc}")
    client.subscribe(mqtt_topic)

def on_message(client, userdata, msg):
    print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")

#client defineren
client = mqtt.Client()

#ophalen en verwerken van de username en password
client.username_pw_set(mqtt_username, mqtt_password)

# instelling voor ssl
if mqtt_connection_type == "ssl":
    client.tls_set()

#callbacks
client.on_connect = on_connect
client.on_message = on_message

# verbinen aan de broker
client.connect(mqtt_host, mqtt_port, 60)

#lopen voor altijd
client.loop_forever()
