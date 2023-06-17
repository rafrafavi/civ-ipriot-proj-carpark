from datetime import datetime
from mqtt_device import MqttDevice
from paho.mqtt.client import MQTTMessage
from config_parser import parse_config


class CarPark(MqttDevice):

    def __init__(self, config):
        super().__init__(config)
        self.total_spaces = config['config']['total_spaces']
        self.total_cars = config['config']['total_cars']
        # print(f"{self.name}, {self.location}, {self.broker}, {self.port}")
        # print({self.topic})
        self.client.on_message = self.on_message
        # self.client.subscribe('sensor')
        self.client.subscribe(config['config']['topic'])
        self.client.loop_forever()
        self._temperature = None


    @property
    def available_spaces(self):
        available = self.total_spaces - self.total_cars
        return max(available, 0)

    @property
    def temperature(self):
        self._temperature
    
    @temperature.setter
    def temperature(self, value):
        self._temperature = value
        
    def _publish_event(self):
        readable_time = datetime.now().strftime('%H:%M')
        print(
            (
                f"TIME: {readable_time}, "
                + f"SPACES: {self.available_spaces}, "
                + "TEMPC: 42"
            )
        )
        message = (
            f"TIME: {readable_time}, "
            + f"SPACES: {self.available_spaces}, "
            + "TEMPC: 42"
        )
        self.client.publish('display', message)

    def on_car_entry(self):
        self.total_cars += 1
        print(self.total_cars)
        self._publish_event()



    def on_car_exit(self):
        self.total_cars -= 1
        print(self.total_cars)
        self._publish_event()

    def on_message(self, client, userdata, msg: MQTTMessage):
        payload = msg.payload.decode()
        print(payload)
        # TODO: Extract temperature from payload
        # self.temperature = ... # Extracted value
        if 'Car goes out' in payload:
            self.on_car_exit()
        else:
            self.on_car_entry()


if __name__ == '__main__':
    config = parse_config()
    car_park = CarPark(config)
    print("Carpark initialized")
