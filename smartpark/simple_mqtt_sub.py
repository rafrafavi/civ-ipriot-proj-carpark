# import mqtt client
import paho.mqtt.client as paho

BROKER, PORT = "localhost", 1883

# Set up the message handler
def on_message(client, userdata, msg):
    print(f'Received {msg.payload.decode()}')

# start the client & connect to MQTT broker/server
client = paho.Client()
# when a message arrives - display it
client.on_message = on_message
client.connect(BROKER, PORT)
client.subscribe("lot/sensor")

# listen forever
client.loop_forever()
