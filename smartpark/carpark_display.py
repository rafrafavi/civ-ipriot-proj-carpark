from windowed_display import WindowedDisplay
import threading
import time
import paho.mqtt.client as paho
from config_parser import parse_config
class CarParkDisplay:
    """Provides a simple display of the car park status. This is a skeleton only. The class is designed to be customizable without requiring and understanding of tkinter or threading."""
    # determines what fields appear in the UI
    fields = ['Available bays', 'Temperature', 'At']

    def __init__(self):
        self.window = WindowedDisplay(
            'Moondalup', CarParkDisplay.fields)
        print("Initialised.") # Can delete once its working

        updater = threading.Thread(target=self.check_updates)
        updater.daemon = True
        updater.start()

        self.window.show()


    def on_message(self, client, userdata, message):
        data = message.payload.decode()
        split_data = data.split(',')
        for item in split_data:
            key, value = item.split(": ")
            if key.strip() == 'SPACES':
                self.spaces = int(value)
            if key.strip() == 'TIME':
                self.time = value
            if key.strip() == 'TEMPC':
                self.temp = float(value)

        field_values = {
            'Available bays': self.spaces,
            'Temperature': f'{self.temp}℃',
            'At': self.time
        }
        self.window.update(field_values)

    def check_updates(self):
        self.spaces = ""
        self.temp = ""
        self.time = ""

        while True:
            field_values = {
                'Available bays': self.spaces,
                'Temperature': f'{self.temp}℃',
                'At': self.time
            }
            config = parse_config("config2.json")
            self.client = paho.Client(config['name'])
            self.client.connect(config["broker"], config["port"])
            self.client.on_message = self.on_message
            self.client.loop_start()
            self.client.subscribe('display1')
            time.sleep(5)
            self.client.loop_stop()


if __name__ == '__main__':
    CarParkDisplay()