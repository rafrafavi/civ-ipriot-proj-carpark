import paho.mqtt.client as mqtt
import time
from random import randrange, uniform
import json
from datetime import datetime
from car_class import Car


BROKER, PORT = "localhost", 1883



MQTT_HOST = "localhost"  # actual machine is "L306-25" aka Broker
MQTT_PORT = 1883  # default MQTT port
MQTT_KEEP_ALIVE = 300  # send an "oi" message every 5 minutes
TOPIC = "Carpark"
MQTT_CLIENT_NAME = "Entry Gate"

TOPIC = "Carpark"

client = mqtt.Client(MQTT_CLIENT_NAME)
client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEP_ALIVE)

while True:
    now = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    if randrange(2) == 1:
        car = Car(parked=True, brand_list=Car.brand_list, colour_list=Car.colour_list)
        car.arrived()
        car_data = {
            "Brand": car.brand,
            "Colour": car.colour,
            "Registration": car.registration,
            "Parked": car.parked,
            "Arrival": car.arrival.strftime("%Y-%m-%dT%H:%M:%SZ")
        }
        json_car_data = json.dumps(car_data)
        client.publish(TOPIC, json_car_data)

        print(f"New Car Arrival: {car.colour} {car.brand}, Registration: {car.registration}, Arrival: {car.arrival.strftime('%Y-%m-%dT%H:%M:%SZ')}")

    time.sleep(5)