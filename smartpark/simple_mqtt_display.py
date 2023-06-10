import mqtt_device

class Display(mqtt_device.MqttDevice):

    def __init__(self, config):
        super().__init__(config)
        self.config = config
        self.client.on_message = self.on_message
        self.client.subscribe('+/+/+/+')
        self.client.loop_forever()
    def on_message(self, client, userdata, msg):
        """I made this program simple to just print the data recieved containing the amount of bays avalible
        and the temprature. This data could be display on screen at the entry and exit of the carpark"""
        msg_data = msg.payload.decode("utf-8")
        topic = msg.topic
        #print(f"Received message. Topic: {topic}, Payload: {msg_data}")

        if topic == 'lot/L306/sensor/car_arrived':
            print(f'{msg_data}')
        elif topic == "lot/L306/sensor/car_left":
            print(f'{msg_data}')


if __name__ == '__main__':
    config = {'name': 'super sensor',
              'location': 'L306',
              'topic-root': "lot",
              'broker': 'localhost',
              'port': 1883,
              'topic-qualifier': 'display'
              }

    display = Display(config)

