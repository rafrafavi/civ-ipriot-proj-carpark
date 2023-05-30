import paho.mqtt.client as mqtt

broker_host, broker_port = 'TBD', 0

client = mqtt.Client()
client.connect(broker_host, broker_port)
client.subscribe("topic_name")

def on_message(client, userdata, message):
    print("")

client.on_message = on_message


client.loop_start()