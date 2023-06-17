import random
import time
import tkinter as tk
from typing import Iterable
import paho.mqtt.client as mqtt
from config_parser import parse_config


config = parse_config()

MQTT_HOST = config['sensor']['broker_host']
MQTT_PORT = config['sensor']['broker_port']
MQTT_CLIENT_NAME = config['sensor']['name']
MQTT_TOPIC = config['sensor']['topic']
MQTT_KEEP_ALIVE = 300
# print(f"Port: {MQTT_PORT}\nBroker: {MQTT_HOST}\nTopic: {MQTT_TOPIC}\nName: {MQTT_CLIENT_NAME}")

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
class CarDetector:
    client = mqtt.Client()
    client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEP_ALIVE)
    client.publish(MQTT_TOPIC)
    """Provides a couple of simple buttons that can be used to represent a sensor detecting a car."""
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Car Detector ULTRA")

        self.btn_incoming_car = tk.Button(
            self.root, text='🚘 Incoming Car', font=('Arial', 50), cursor='right_side', command=self.incoming_car)
        self.btn_incoming_car.pack(padx=10, pady=5)
        self.btn_outgoing_car = tk.Button(
            self.root, text='Outgoing Car 🚘',  font=('Arial', 50), cursor='bottom_left_corner', command=self.outgoing_car)
        self.btn_outgoing_car.pack(padx=10, pady=5)

        self.root.mainloop()

    def on_connect(client, userdata, flags, rc):
        print("Connected with result code " + str(rc))

    def on_message(self):
        pass

    def incoming_car(self):
        # TODO: implement this method to publish the detection via MQTT
        print("Car goes in")
        payload = 'Car goes in'
        self.client.publish(MQTT_TOPIC, payload)

    def outgoing_car(self):
        # TODO: implement this method to publish the detection via MQTT
        print("Car goes out")
        payload = 'Car goes out'
        self.client.publish(MQTT_TOPIC, payload)

    # Activate when connection established
    client.on_connect = on_connect
    # Listen for message and activate when message received
    client.on_message = on_message


if __name__ == '__main__':
    CarDetector()
