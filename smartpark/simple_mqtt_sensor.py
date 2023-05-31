import time
import paho.mqtt.client as paho


class Sensor:
    def __init__(self, config):
        self.name = config["name"]
        self.location = config["location"]
        self.broker = config["broker"]
        self.port = config["port"]
        self.client = paho.Client()
        self.client.connect(self.broker, self.port)
        self.topic = config["topic"]

    def on_detection(self, message):
        self.client.publish(self.topic, message)

    def start_sensing(self):
        while True:
            reply = input("Is there a car?")
            if reply == "y":
                self.on_detection("Car, I saw a car!!")


if __name__ == "__main__":
    config = {"name": "super sensor",
              "location": "L306",
              "broker": "localhost",
              "port": 1883,
              "topic": "lot/sensor"
              }
    sensor = Sensor(config)
    print("Sensor initialized")
    sensor.start_sensing()