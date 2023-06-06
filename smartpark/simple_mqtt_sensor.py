""""Demonstrates a simple implementation of an 'event' listener that triggers
a publication via mqtt"""

import mqtt_device
import time
from random import randrange, uniform
import json
from datetime import datetime
from Car_Class import Car

class Sensor(mqtt_device.MqttDevice):

    def on_detection(self, message):
        """Triggered when a detection occurs"""
        self.client.publish(self.topic, message)

    def start_sensing(self):
        """ A blocking event loop that waits for detection events, in this
        case Enter presses"""
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
                self.on_detection(json_car_data)
                print(f"New Car Arrival: {car.colour} {car.brand}, Registration: {car.registration},"
                f"Arrival: {car.arrival.strftime('%Y-%m-%dT%H:%M:%SZ')}")


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
    sensor.start_sensing()

