from datetime import datetime
from mqtt_device import MqttDevice
from paho.mqtt.client import MQTTMessage
from config_parser import parse_config
import toml

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
        self.client.subscribe(config['temperature']['topic'])
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
        readable_time = datetime.now().strftime('%H:%M:%S')
        #print(
        #    (
        #        f"Available Spaces: {self.available_spaces}, "
        #        + f"Time: {readable_time}, "
        #        + f"Temperature: {self._temperature}"
        #    )
        #)
        message = (
            f"Available Bays: {self.available_spaces}, "
            + f"Time: {readable_time}, "
            + f"Temperature: {self._temperature}"
        )
        print(message)
        self.client.publish('display', message)

    def on_car_entry(self):
        if self.available_spaces != 0:
            self.total_cars += 1
        else:
            pass
        # print(self.total_cars)
        print(f"Available Spaces: {self.available_spaces}")
        self._publish_event()



    def on_car_exit(self):
        if self.total_cars != 0:
            self.total_cars -= 1
        else:
            pass
        # print(self.total_cars)
        print(f"Available Spaces: {self.available_spaces}")
        self._publish_event()

    def on_message(self, client, userdata, msg: MQTTMessage):
        payload = msg.payload.decode("UTF-8")
        # print(payload)
        if 'Car goes out' in payload:
            self.on_car_exit()
        elif 'Car goes in' in payload:
            self.on_car_entry()
        elif 'Current Temp' in payload:
            data = toml.loads(payload)
            temperature = data['Current Temp']
            # print(temperature)
            self._temperature = temperature
            self._publish_event()
            # print(self._temperature)
        else:
            pass


if __name__ == '__main__':
    config = parse_config()
    car_park = CarPark(config)
    print("Carpark initialized")
