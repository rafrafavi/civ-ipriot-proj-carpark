import paho.mqtt.client as mqtt
import time
import toml

MQTT_HOST = "localhost"
MQTT_PORT = 1883
MQTT_KEEP_ALIVE = 30
MQTT_CLIENT_NAME = "Temperature Receiver"
MQTT_TOPIC = "Temperature"


# Instantiate MQTT Client as 'Temperature Receiver'
client = mqtt.Client(MQTT_CLIENT_NAME)
# Connect to the server/broker
client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEP_ALIVE)
# Display 'print' on connect and subscribe to MQTT Topic
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(MQTT_TOPIC)

# Activate when message has been received and 'print'
def on_message(client, userdata, msg):
    message = msg
    message_data = str(message.payload.decode("UTF-8"))
    data = toml.loads(message_data)
    # output = f"{MQTT_CLIENT_NAME}: The temperature was {data['current temp']} at {data['datetime']}!"
    # print(output)


# Activate when connection established
client.on_connect = on_connect
# Listen for message and activate when message received
client.on_message = on_message
# Keep listening until manually stopped
client.loop_forever()
