import paho.mqtt.client as paho

BROKER, PORT = "localhost", 1883

client = paho.Client()
client.connect(BROKER, PORT)
client.publish("lot/sensor", "Hello from Python")

