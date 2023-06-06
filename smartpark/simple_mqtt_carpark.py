from datetime import datetime

import mqtt_device
import paho.mqtt.client as paho
from paho.mqtt.client import MQTTMessage


class CarPark(mqtt_device.MqttDevice):
    """Creates a carpark object to store the state of cars in the lot"""

    def __init__(self, config):
        super().__init__(config['broker'])
        carpark_name = config['broker'] ['location']
        self.total_spaces = config.get(f" {carpark_name}.total_spaces",192)
        self.total_cars = config.get(f" {carpark_name}.total-cars",0)
        self.temperature = None
        print(f" Carpark at {carpark_name} is ready")
        self.client.on_message = self.on_message
        self.client.subscribe('sensor')
        self.client.subscribe('car/detection')

        self.client.loop_forever()


    @property
    def available_spaces(self):
        available = self.total_spaces - self.total_cars
        return max(available, 0)

    @property
    def temperature(self):
        return self._temperature
    
    @temperature.setter
    def temperature(self, value):
        self._temperature = value

        
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
        self.client.publish('display', message)

    def on_car_entry(self):
        self.total_cars += 1
        self._publish_event()



    def on_car_exit(self):
        self.total_cars -= 1
        self._publish_event()

    def on_message(self, client, userdata, msg: MQTTMessage):
        payload = msg.payload.decode()
        topic =  msg.topic
        if topic == 'sensor':
            temperature = payload.split(',')[-1]
            self.temperature = temperature
        # TODO: Extract temperature from payload -done*
        # self.temperature = ... # Extracted value
        if 'exit' in payload:
            self.on_car_exit()
        else:
            self.on_car_entry()


if __name__ == '__main__':
    # TODO: Read config from file - done
    from config_parser import parse_config
    config = parse_config("config.toml")
    CarPark(config)
    print("Carpark initialized")

