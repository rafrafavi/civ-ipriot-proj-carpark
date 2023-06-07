""""Demonstrates a simple implementation of an 'event' listener that triggers
a publication via mqtt"""
import random
import paho.mqtt.client as paho

import mqtt_device # importing mqtt_device's attributes and properties.


class Sensor(mqtt_device.MqttDevice):

    def __init__(self, config): # Sensor class' attributes are referred to config file, where all the infos are kept.
        self.name = config["name"] # so that people who don't code, can also access the config file(json) and change the value.
        self.location = config["location"]
        self.broker = config["broker"]
        self.port = config["port"]
        self.client = paho.Client()
        self.client.connect(self.broker, self.port)
        self.topic = config["topic"] # connected to the topic.

    @property
    def temperature(self):
        """Returns the current temperature"""
        return random.randint(10, 35)

    def on_detection(self, message):
        """Triggered when a detection occurs"""
        self.client.publish('sensor', message)  # publish the message argument to "sensor" topic

    def start_sensing(self):
        """ A blocking event loop that waits for detection events, in this
        case Enter presses"""
        while True:
            print("Press E when 🚗 entered!")
            print("Press X when 🚖 exited!")
            detection = input("E or X> ").upper()
            if detection == 'E':
                self.on_detection(f"entered, {self.temperature}")
            else:
                self.on_detection(f"exited, {self.temperature}")


if __name__ == '__main__':
    # when the program is run directly by the Python interpreter.
    # The code inside the if statement is not executed when the file's code is imported as a module.
    config1 = {'name': 'sensor', # a dictionary to hold all the values.
               'location': 'moondalup',
               'topic-root': "lot",
               'broker': 'localhost',
               'port': 1883,
               "topic": "lot/sensor"
               }
    # TODO: Read previous config from file instead of embedding

    sensor1 = Sensor(config1)  # create an object of the class, to access its methods

    print("Sensor initialized")
    sensor1.start_sensing()

