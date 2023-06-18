import random
import threading
import time
import tkinter as tk
from typing import Iterable
import paho.mqtt.client as mqtt
import toml
from paho.mqtt.client import MQTTMessage
from config_parser import parse_config

config = parse_config()

MQTT_HOST = config['display']['broker_host']  # "localhost"
MQTT_PORT = config['display']['broker_port']  # "1883"
MQTT_CLIENT_NAME = config['display']['name']  # "Car Park Display"
MQTT_TOPIC = config['display']['topic']
# MQTT_TOPIC_1 = config['display']['topic_1']  # "Available Bays"
# MQTT_TOPIC_2 = config['display']['topic_2']  # "Date/Time"
# MQTT_TOPIC_3 = config['display']['topic_3']  # "Current Temp"
MQTT_KEEP_ALIVE = 300

# ------------------------------------------------------------------------------------#
# You don't need to understand how to implement this class, just how to use it.       #
# ------------------------------------------------------------------------------------#
# TODO: got to the main section of this script **first** and run the CarParkDisplay.  #


class WindowedDisplay:
    """Displays values for a given set of fields as a simple GUI window. Use .show() to display the window; use .update() to update the values displayed.
    """

    DISPLAY_INIT = '– – –'
    SEP = ':'  # field name separator

    def __init__(self, title: str, display_fields: Iterable[str]):
        """Creates a Windowed (tkinter) display to replace sense_hat display. To show the display (blocking) call .show() on the returned object.

        Parameters
        ----------
        title : str
            The title of the window (usually the name of your carpark from the config)
        display_fields : Iterable
            An iterable (usually a list) of field names for the UI. Updates to values must be presented in a dictionary with these values as keys.
        """
        self.window = tk.Tk()
        self.window.title(f'{title}: Parking')
        self.window.geometry('800x400')
        self.window.resizable(False, False)
        self.display_fields = display_fields

        self.gui_elements = {}
        for i, field in enumerate(self.display_fields):

            # create the elements
            self.gui_elements[f'lbl_field_{i}'] = tk.Label(
                self.window, text=field+self.SEP, font=('Arial', 50))
            self.gui_elements[f'lbl_value_{i}'] = tk.Label(
                self.window, text=self.DISPLAY_INIT, font=('Arial', 50))

            # position the elements
            self.gui_elements[f'lbl_field_{i}'].grid(
                row=i, column=0, sticky=tk.E, padx=5, pady=5)
            self.gui_elements[f'lbl_value_{i}'].grid(
                row=i, column=2, sticky=tk.W, padx=10)

    def show(self):
        """Display the GUI. Blocking call."""
        self.window.mainloop()

    def update(self, updated_values: dict):
        """Update the values displayed in the GUI. Expects a dictionary with keys matching the field names passed to the constructor."""
        for field in self.gui_elements:
            if field.startswith('lbl_field'):
                field_value = field.replace('field', 'value')
                self.gui_elements[field_value].configure(
                    text=updated_values[self.gui_elements[field].cget('text').rstrip(self.SEP)])
        self.window.update()

# -----------------------------------------#
# TODO: STUDENT IMPLEMENTATION STARTS HERE #
# -----------------------------------------#


class CarParkDisplay:
    """Provides a simple display of the car park status. This is a skeleton only. The class is designed to be customizable without requiring and understanding of tkinter or threading."""
    # determines what fields appear in the UI
    fields = ['Available Bays', 'Temperature', 'Time']


    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEP_ALIVE)
        self.client.loop_start()
        self.window = WindowedDisplay(
            'Moondalup', CarParkDisplay.fields)
        self.window.show()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        self.client.subscribe(MQTT_TOPIC)

    def on_message(self, client, userdata, msg):
        # Check to see if MQTT message is received
        print('a message was received')
        payload = msg.payload.decode("UTF-8")
        print(payload)
        data = toml.loads(payload)
        available_bays = data.get('Available Bays')
        current_time = data.get('Time')
        temperature = data.get('Temperature')
        print(available_bays)

        field_values = dict(zip(CarParkDisplay.fields, [
            f"{available_bays}",
            f'{temperature}℃',
            f'{current_time}']))
        # Pretending to wait on updates from MQTT
        # time.sleep(random.randint(1, 10))
        # When you get an update, refresh the display.
        self.window.update(field_values)


if __name__ == '__main__':
    CarParkDisplay()
