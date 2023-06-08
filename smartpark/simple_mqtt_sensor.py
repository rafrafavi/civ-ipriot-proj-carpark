""""Demonstrates a simple implementation of an 'event' listener that triggers
a publication via mqtt"""

import mqtt_device
import time
import random
import json
from datetime import datetime
from car import Car
from simple_mqtt_carpark import Carpark
import threading

class Sensor(mqtt_device.MqttDevice):

    @property
    def temperature(self):
        """Returns the current temperature"""
        return random.randint(10, 35)
    def on_detection_entry(self, message):
            """Triggered when a detection occurs"""
            self.client.publish(self.topic, message)

    def on_detection_exit(self, json_message):
        """Triggered when a detection occurs"""
        topic = "lot/L306/sensor/car_exited"
        self.client.publish(topic, json_message)

    def start_sensing_entry(self):
        """ A blocking event loop that waits for detection events, in this
        case Enter presses"""
        while True:

            if random.randrange(2) == 1:
                car = Car(parked=True, brand_list=Car.brand_list, colour_list=Car.colour_list)
                car.arrived()
                temp = 'temperature', self.temperature
                car_data = {"Car": {
                        "brand": car.brand,
                        "colour": car.colour,
                        "registration": car.registration,
                        "parked": car.parked,
                        "arrival": car.arrival.strftime("%Y-%m-%dT%H:%M:%SZ") }}, temp

                json_car_data = json.dumps(car_data)
                self.on_detection_entry(json_car_data)
                print(f"New Car Arrival: {car.colour} {car.brand}, Registration: {car.registration},"
                f"Arrival: {car.arrival.strftime('%Y-%m-%dT%H:%M:%SZ')}")


            time.sleep(5)
    def start_sensing_exit(self):
        while True:
            if random.randrange(2) == 1:
                temp = 'temperature', self.temperature
                car_exited = "Car Exited"
                message = car_exited, temp
                json_message = json.dumps(message)
                self.on_detection_exit(json_message)
                print("A car has exited")



            time.sleep(5)









if __name__ == '__main__':
    config = {'name': 'super sensor',
              'location': 'L306',
              'topic-root': "lot",
              'broker': 'localhost',
              'port': 1883,
              'topic-qualifier': 'entry'
              }

    sensor = Sensor(config)
    print("Sensor initialized")

    # I had a issue with both sensors running at the same time as the start_sensing_entry is the orginal program
    # was looping and blocking the start_sensing_exit. I did some research and came across this method of threading the
    # two methods so that they can both run automaticly.
    sensing_entry_thread = threading.Thread(target=sensor.start_sensing_entry)
    sensing_exit_thread = threading.Thread(target=sensor.start_sensing_exit)
    sensing_entry_thread.start()
    sensing_exit_thread.start()
    sensing_entry_thread.join()
    sensing_exit_thread.join()
