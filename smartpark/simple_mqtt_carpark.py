import paho.mqtt.client as paho
import simple_mqtt_device
class Carpark(simple_mqtt_device.MqttDevice):
    """Creats a carpark object to store the state of cars in the lot"""
    def __init__(self,config):
        super().__init__(config)
        self.total_spaces = config['total-spaces']
        self.total_cars = config['total-cars']
        self.client.on_message = self.on_message
        self.client.subscribe('+/+/+/+')
        self.client.loop_forever()


    def available_spaces(self):
        available = self.total_spaces - self.total_cars
        return available if available > 0 else 0
    def enter_car(self):
        self.total_cars += 1
        # TODO: Publish to MQTT
    def car_exit(self):
        self.total_cars -= 1
        # TODO: Publish to MQTT

    def on_message(self, client, userdata, msg):
        print(f'Received {msg.payload.decode()}')

if __name__ == '__main__':
    config = {'name': 'saepark',
              'total-spaces': 130,
              'total-cars': 0,
              'location': 'L306',
              'topic': "lot/sensor",
              'broker': 'localhost',
              'port': 1883,
              'type': 'ENTRY'
              }

carpark = Carpark(config)
print("Carpark initialized")



