""""Demonstrates a simple implementation of an 'event' listener that triggers
a publication via mqtt"""
import random

import mqtt_device
import config_parser


class Sensor(mqtt_device.MqttDevice):

    @property
    def temperature(self):
        """Returns the current temperature"""
        return random.randint(10, 35) 

    def on_detection(self, message):
        """Triggered when a detection occurs"""
        self.client.publish('sensor', message)

    def start_sensing(self):
        """ A blocking event loop that waits for detection events, in this
        case Enter presses"""
        while True:
            print("Press E when 🚗 entered!")
            print("Press X when 🚖 exited!")
            cars_in_carpark = 0
            detection = input("E or X> ").upper()
            if detection == 'E':
                self.on_detection(f"entered, {self.temperature}")
                cars_in_carpark += 1
            elif detection == 'X':
                self.on_detection(f"exited, {self.temperature}")
                cars_in_carpark -= 1


            '''if detection == 'E' and self.total_cars >= cars_in_carpark:
                self.on_detection(f"entered, {self.temperature}")
                cars_in_carpark += 1
            elif detection == 'X' and self.total_cars < cars_in_carpark:
                self.on_detection(f"exited, {self.temperature}")
                cars_in_carpark -= 1'''

if __name__ == '__main__':

    # TODO: Read previous config from file instead of embedding

    config = config_parser.parse_config()
    sensor1 = Sensor(config)
    print("Sensor initialized")
    sensor1.start_sensing()

    sensor1.start_sensing()

