from datetime import datetime
import mqtt_device
import paho.mqtt.client as paho
from paho.mqtt.client import MQTTMessage
import json
import random
class CarPark(mqtt_device.MqttDevice):
    """Creates a carpark object to store the state of cars in the lot"""
    def __init__(self, config):
        super().__init__(config)
        self.carpark_name = config['name']
        print(config['name'])
        self.total_spaces = config['total-spaces']
        self.max_spaces = config['total-spaces']
        self.total_cars = config['total-cars']
        self.client.on_message = self.on_message
        self.client.subscribe('sensor')
        self.client.loop_forever()

    @property
    def available_spaces(self):
        available = self.total_spaces - self.total_cars
        # To stop the available spaces dipping below 0.
        if available < 0:
            available = 0
        # Caps the available parking to the upper limit so it cant exceed this.
        if available > self.max_spaces:
            available = self.max_spaces
        return max(available, 0)

    @property
    def temperature(self):
        return self._temperature
    
    @temperature.setter
    def temperature(self, value):
        value = random.gauss(30, 1)
        self._temperature = round(value, 1)
        
    def _publish_event(self):
        readable_time = datetime.now().strftime('%H:%M')
        print(
            (
                f"TIME: {readable_time}, "
                + f"SPACES: {self.available_spaces}, "
                + f"TEMPC: {self.temperature}"
            )
        )
        message = (
            f"TIME: {readable_time}, "
            + f"SPACES: {self.available_spaces}, "
            + f"TEMPC: {self.temperature}"
        )
        self.client.publish('display1', message)

    def on_car_entry(self):
        self.total_cars += 1
        self._publish_event()

    def on_car_exit(self):
        self.total_cars -= 1
        if self.total_cars < 0:
            self.total_cars = 0
        self._publish_event()

    def on_message(self, client, userdata, msg: MQTTMessage):
        payload = msg.payload.decode()
        # Extract temperature from payload
        self.temperature = random.gauss(30, 1)

        if 'exit' in payload:
            self.on_car_exit()
        else:
            self.on_car_entry()


if __name__ == '__main__':
    # Read config from file
    from config_parser import parse_config
    config = parse_config("config.json")
    print("Carpark initialized")
    car_park = CarPark(config)
