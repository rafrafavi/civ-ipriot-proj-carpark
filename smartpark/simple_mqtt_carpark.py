import paho.mqtt.client as paho
from paho.mqtt.client import MQTTMessage
import mqtt_device
from datetime import datetime


class CarPark(mqtt_device.MqttDevice):
    """Creates a carpark object to store the state of cars in the lot"""

    def __init__(self, config):
        super().__init__(config)
        self.total_spaces = config['total-spaces']
        self.total_cars = config['total-cars']
        self.client.on_message = self.on_message
        self.client.subscribe('+/+/+/+')
        self.client.loop_forever()

    @property
    def available_spaces(self):
        available = self.total_spaces - self.total_cars
        return available if available > 0 else 0

    def _publish_event(self):
        readable_time = datetime.now().strftime('%H:%M')
        print(f"TIME: {readable_time}, " +
              f"SPACES: {self.available_spaces}, " +
              f"TEMP°C: 42")  # TODO: Temperature
        # TODO: Publish to MQTT

    def on_car_entry(self):
        self.total_cars += 1
        self._publish_event()

    def on_car_exit(self):
        self.total_cars -= 1
        self._publish_event()

    def on_message(self, client, userdata, msg: MQTTMessage):
        # print(f'Received {msg.payload.decode()}')
        print(msg.topic)
        topic = msg.topic.strip().split('/')[-1]
        print(topic)
        if topic == 'entry':
            self.on_car_entry()
        else:
            self.on_car_exit()


if __name__ == '__main__':
    config = {'name': "raf-park",
              'total-spaces': 130,
              'total-cars': 0,
              'location': 'L306',
              'topic-root': "lot",
              'broker': 'localhost',
              'port': 1883,
              'topic-qualifier': 'entry',
              'is_stuff': False
              }
    car_park = CarPark(config)
    print("Carpark initialized")
