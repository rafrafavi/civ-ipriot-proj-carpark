import paho.mqtt.client as paho
from paho.mqtt.client import MQTTMessage

BROKER, PORT = "localhost", 1883

def on_message(client, userdata, msg):
    print(f'Received {msg.payload.decode()}')

client = paho.Client()
client.on_message = on_message
client.connect(BROKER, PORT)
client.subscribe("lot/sensor")
client.loop_forever()
