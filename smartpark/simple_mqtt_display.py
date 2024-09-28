import mqtt_device
import time
from random import randrange, uniform
import json
from datetime import datetime
from Car_Class import Car


class Display(mqtt_device.MqttDevice):

    def __init__(self, config):
        super().__init__(config)
        self.config = config
        self.client.on_message = self.on_message
        self.client.subscribe('+/+/+/+')
        self.client.loop_forever()
    def on_message(self, client, userdata, msg):
        msg_data = msg.payload.decode("utf-8")
        topic = msg.topic
        #print(f"Received message. Topic: {topic}, Payload: {msg_data}")

        if topic == 'lot/L306/sensor/car_arrived':
            print(f'Update : {msg_data}')
        elif topic == "lot/L306/sensor/car_exited":
            print(f'Update : {msg_data}')



if __name__ == '__main__':
    config = {'name': 'super sensor',
              'location': 'L306',
              'topic-root': "lot",
              'broker': 'localhost',
              'port': 1883,
              'topic-qualifier': 'display'
              }

    display = Display(config)


