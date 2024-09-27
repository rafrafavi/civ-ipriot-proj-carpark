import mqtt_device
import time
import config_parser
class Display(mqtt_device.MqttDevice):
    """Displays the number of cars and the temperature"""
    def __init__(self, config):
        super().__init__(config)
        self.client.on_message = self.on_message
        self.client.subscribe('display')
        self.client.loop_forever()

    def display(self, *args):
        print('*' * 20)
        for val in args:
            print(val)
            time.sleep(1)

        print('*' * 20)
    def on_message(self, client, userdata, msg):
        data = msg.payload.decode()
        print(data)
        self.display(*data.split(','))
        # TODO: Parse the message and extract free spaces,\
        #  temperature, time
        time = self.display[0]
        free_spaces = self.display[1]
        temperature = self.display[2]





if __name__ == '__main__':
    # TODO: Read config from file
    display = Display(config_parser.parse_config())

