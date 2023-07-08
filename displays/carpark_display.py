import random
import threading
import time
import paho.mqtt.client as mqtt
from windowed_display import WindowedDisplay
from config_parser import ConfigParser


class CarParkDisplay:
    fields = ['Available bays', 'Temperature', 'At']

    def __init__(self, config):
        """
        Initializes the CarParkDisplay class.

        Args:
            config (dict): Configuration parameters for the car park display.
        """
        self.config = config
        self.window = WindowedDisplay(self.config["name"], CarParkDisplay.fields)
        self.available_bays = self.config["total-spaces"]
        updater = threading.Thread(target=self.check_updates)
        updater.daemon = True
        updater.start()

        # MQTT client setup
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.connect(self.config["broker"], self.config["port"])
        self.mqtt_client.subscribe("car_detection")
        self.mqtt_client.on_message = self.on_message
        self.mqtt_client.loop_start()

        self.window.show()

    def on_message(self, client, userdata, message):
        """
        Callback function to handle MQTT message events.

        Updates the available bays count based on the car detection events received via MQTT.

        Args:
            client (mqtt.Client): The MQTT client instance.
            userdata: Custom user data.
            message (mqtt.MQTTMessage): The received MQTT message.
        """
        payload = message.payload.decode()
        if "_incoming" in payload:
            self.available_bays -= 1
        elif "_outgoing" in payload:
            self.available_bays += 1

    def check_updates(self):
        """
        Periodically checks for updates and updates the display.

        Retrieves field values (available bays, temperature, and current time) and updates the display
        at random intervals between 1 and 10 seconds.
        """
        while True:
            field_values = {
                'Available bays': f'{self.available_bays}',
                'Temperature': f'{random.randint(0, 45)}℃',
                'At': time.strftime("%H:%M:%S")
            }
            time.sleep(random.randint(1, 10))
            self.window.update(field_values)


if __name__ == '__main__':
    # Load the config from the TOML file
    config = ConfigParser.load_config('config.toml')

    # Create an instance of CarParkDisplay with the config
    car_park_display = CarParkDisplay(config)
