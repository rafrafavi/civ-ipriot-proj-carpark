import paho.mqtt.client as mqtt
from random import randrange, uniform
from datetime import datetime
import time
import toml
from config_parser import parse_config


config = parse_config()
MQTT_HOST = config['temperature']['broker_host']
MQTT_PORT = config['temperature']['broker_port']
MQTT_KEEP_ALIVE = 300
MQTT_CLIENT_NAME = config['temperature']['name']
MQTT_TOPIC = config['temperature']['topic']

# Instantiate MQTT Client as 'Temperature Monitor'
client = mqtt.Client(MQTT_CLIENT_NAME)
# Connect to the server/broker
client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEP_ALIVE)

print(f"Sending Message to {MQTT_HOST} on port {MQTT_PORT} with topic {MQTT_TOPIC}")

while True:
    current_temp = uniform(20.0, 24.0)
    current_time = datetime.now().strftime("%H:%M:%S")
    message_data = {
        "client": MQTT_CLIENT_NAME,
        "temp": current_temp,
        "datetime": current_time,
    }
    send_message = toml.dumps(message_data)
    # Publish topic / Republish topic
    client.publish(MQTT_TOPIC, send_message)
    time.sleep(5)



