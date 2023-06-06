import paho.mqtt.client as paho

BROKER, PORT = "127.0.0.1", 1883

client = paho.Client()
client.connect(BROKER, PORT)
client.publish("lot/sensor", "Hello from Python")

