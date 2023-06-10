""""Demonstrates a simple implementation of an 'event' listener that triggers
a publication via mqtt"""

import mqtt_device
import time
import random
import json
from car import Car
import threading

class Sensor(mqtt_device.MqttDevice):


    def __init__(self, config):
        super().__init__(config)
        self.client.on_message = self.on_message
        self.client.subscribe('+/+/+/+')
        self.available_spaces = 0

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
        case Enter presses on the event of a car coming a random car object is generated if there
         is not any avalible bays a message is displayed and a car can not be created till on exits   """
        while True:
            if self.available_spaces <= 130:
                if random.randrange(2) == 1:
                    car = Car(parked=True, brand_list=Car.brand_list, colour_list=Car.colour_list)
                    car.arrived()
                    temp = 'temperature', self.temperature
                    car_data = {"Car": {
                            "brand": car.brand,
                            "colour": car.colour,
                            "registration": car.registration,
                            "parked": car.parked,
                            "arrival": car.arrival.strftime("%Y-%m-%dT%H:%M:%SZ")}}, temp

                    json_car_data = json.dumps(car_data)
                    self.on_detection_entry(json_car_data)
                    print(f"New Car Arrival: {car.colour} {car.brand}, Registration: {car.registration},"
                        f"Arrival: {car.arrival.strftime('%Y-%m-%dT%H:%M:%SZ')}")
                time.sleep(5)

            elif self.available_spaces >= 130:
                print('Carpark is Full')
                time.sleep(5)

    def start_sensing_exit(self):
        """ If there is no empty bays it isnt possible for the a car exiting event to occur"""
        if self.available_spaces <= 130:
            while True:
                if random.randrange(2) == 1:
                    temp = 'temperature', self.temperature
                    car_exited = "Car Exited"
                    message = car_exited, temp
                    json_message = json.dumps(message)
                    self.on_detection_exit(json_message)
                    print("A car has exited")
                time.sleep(5)

        elif self.available_spaces <= 0:
            print('Carpark is Empty')
            time.sleep(5)

    def on_message(self, client, userdata, msg):
        """I decided the most accurate way to get the value of avalible bays is to get a message from the time a entry
        or exit event occurs in Carpark"""
        msg_data = msg.payload.decode("utf-8")
        topic = msg.topic
        #print(f"Received message. Topic: {topic}, Payload: {msg_data}")
        if topic == "lot/L306/sensor/available_bays":
           self.available_spaces = int(msg_data)


if __name__ == '__main__':
    config = {'name': 'super sensor',
              'location': 'L306',
              'topic-root': "lot",
              'broker': 'localhost',
              'port': 1883,
              'topic-qualifier': 'entry'
              }

    sensor = Sensor(config)
    sensor.client.loop_start()
    print("Sensor initialized")

    """I had a issue with both sensors running at the same time as the start_sensing_entry is the orginal program
    was looping and blocking the start_sensing_exit. I did some research and came across this method of threading the
    two methods so that they can both run simualtamisly"""
    sensing_entry_thread = threading.Thread(target=sensor.start_sensing_entry)
    sensing_exit_thread = threading.Thread(target=sensor.start_sensing_exit)
    sensing_entry_thread.start()
    sensing_exit_thread.start()
    sensing_entry_thread.join()
    sensing_exit_thread.join()



