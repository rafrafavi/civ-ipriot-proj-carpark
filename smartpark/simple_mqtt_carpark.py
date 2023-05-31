import paho.mqtt.client as paho
import mqtt_device

class Carpark(mqtt_device.MqttDevice):
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
    def on_car_entry(self):
        self.total_cars += 1
        # TODO: Publish to MQTT

    def on_car_exit(self):
        self.total_cars -= 1
        # TODO: Publish to MQTT

    def on_message(self, client, userdata, msg):
        print(f'Received {msg.payload.decode()}')


if __name__ == '__main__':
    config = {'name': "raf-park",
              'total-spaces': 130,
              'total-cars': 0,
              'location': 'L306',
              'topic-root': "lot",
              'broker': 'localhost',
              'port': 1883,
              'topic-qualifier': 'entry'
              }

    carpark = Carpark(config)
    print("Carpark initialized")
