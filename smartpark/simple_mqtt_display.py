import mqtt_device
import time


class Display(mqtt_device.MqttDevice):
    """Displays the number of cars and the temperature"""

    def __init__(self, config):
        super().__init__(config)
        self.client.on_message = self.on_message
        self.client.subscribe('display')  # subscribed to "display" topic in carpark class.
        self.client.loop_forever()  # listen forever.

    def display(self, *args):
        print('*' * 20)
        for val in args:
            print(val) # then print them in this method.
            time.sleep(1)

        print('*' * 20)

    def on_message(self, client, userdata, msg):
        data = msg.payload.decode()  # takes the message
        self.display(*data.split(','))  # splits the message into 3 sections,
        # TODO: Parse the message and extract free spaces,\
        #  temperature, time


if __name__ == '__main__':
    config = {'name': 'display',
              'location': 'L306',
              'topic-root': "lot",
              'broker': 'localhost',
              'port': 1883,
              'topic-qualifier': 'na'
              }
    # TODO: Read config from file
    display = Display(config)  # create an object of Display class, so its methods will run.
