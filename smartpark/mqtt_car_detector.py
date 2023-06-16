import random

import mqtt_device

import random
import threading
import time
import tkinter as tk


class Sensor(mqtt_device.MqttDevice):

    @property
    def temperature(self):
        """Returns the current temperature"""
        return random.randint(10, 35) 

    def on_detection(self, message):
        """Triggered when a detection occurs"""
        self.client.publish('temperature', message)
        self.client.publish('sensor', message)


class CarDetector:
    """Provides a couple of simple buttons that can be used to represent a sensor detecting a car. This is a skeleton only."""

    def __init__(self, sensor):
        self.sensor = sensor
        self.root = tk.Tk()
        self.root.title("Car Detector ULTRA")

        self.btn_incoming_car = tk.Button(
            self.root, text='🚘 Incoming Car', font=('Arial', 50), cursor='right_side', command=self.incoming_car)
        self.btn_incoming_car.pack(padx=10, pady=5)
        self.btn_outgoing_car = tk.Button(
            self.root, text='Outgoing Car 🚘',  font=('Arial', 50), cursor='bottom_left_corner', command=self.outgoing_car)
        self.btn_outgoing_car.pack(padx=10, pady=5)

        self.root.mainloop()


    def outgoing_car(self):
        # TODO: implement this method to publish the detection via MQTT
        self.sensor.on_detection('Car has exited')
        print("Car goes out")
        

    def incoming_car(self):
        self.sensor.on_detection('Car has entered')
        print("Car goes in")
        


if __name__ == '__main__':
    config1 = {
        'name': 'sensor',
        'location': 'moondalup',
        'topic-root': "lot",
        'broker': 'localhost',
        'topic-qualifier': 'sensor',
        'port': 1883,
    }
    sensor = Sensor(config1)
    cardetector = CarDetector(sensor)


