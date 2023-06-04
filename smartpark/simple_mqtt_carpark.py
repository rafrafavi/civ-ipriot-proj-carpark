import paho.mqtt.client as paho
import mqtt_device
import time
from random import randrange, uniform
import json
from datetime import datetime
from Car_Class import Car

class Carpark(mqtt_device.MqttDevice):
    """Creates a carpark object to store the state of cars in the lot"""

    def __init__(self, config):
        super().__init__(config)
        self.config = config
        self.total_spaces = config['total-spaces']
        self.total_cars = config['total-cars']
        self.client.on_message = self.on_message
        self.client.subscribe('+/+/+/+')
        self.client.loop_forever()

    @property
    def available_spaces(self):
        available = self.total_spaces - self.total_cars
        return available if available > 0 else 0
    def on_car_entry(self, msg_data):
        self.total_cars += 1

        topic = "lot/L306/sensor/car_arrived"
        message = f"A car arrived at the carpark. Total parked cars: {self.total_cars}. " \
                  f"Total empty parking bays {self.available_spaces}"
        self.client.publish(topic, message)
        #print(message)



    def on_car_exit(self):
        self.total_cars -= 1
        # TODO: Publish to MQTT

    def on_message(self, client, userdata, msg):
        msg_data = msg.payload.decode("utf-8")
        topic = msg.topic
        #print(f"Received message. Topic: {topic}, Payload: {msg_data}")

        try:
            msg_data = json.loads(msg_data)
        except json.JSONDecodeError:
            print("Failed to convert JSON data")
            return

        if topic == 'lot/L306/sensor/entry':
            self.on_car_entry(msg_data)
            brand = msg_data.get('Brand')
            colour = msg_data.get('Colour')
            print(f"A {colour} {brand} has parked there are {self.total_cars} cars parked and "
            f"{self.available_spaces} parking spaces left")
        elif topic == "another topic":
            print(f'Received message from topic2: {msg_data}')



if __name__ == '__main__':
    config = {'name': "raf-park",
              'total-spaces': 130,
              'total-cars': 0,
              'location': 'L306',
              'topic-root': "lot",
              'broker': 'localhost',
              'port': 1883,
              'topic-qualifier': 'entry'
              }

    carpark = Carpark(config)
    carpark.client.loop_forever()
    print("Carpark initialized")
