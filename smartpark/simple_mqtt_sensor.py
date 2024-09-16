""""Demonstrates a simple implementation of an 'event' listener that triggers
a publication via mqtt"""
import random

import mqtt_device


class Sensor(mqtt_device.MqttDevice):
    def __init__(self, config):
        super().__init__(config['broker'])
        sensor_name = config['broker']['sensor']
        print(f" Sensor at {sensor_name} is ready")
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
            detection = input("E or X> ").upper()
            if detection == 'E':
                self.on_detection(f"entered, {self.temperature}")
            else:
                self.on_detection(f"exited, {self.temperature}")


if __name__ == '__main__':

    # TODO: Read previous config from file instead of embedding - done
    from config_parser import parse_config

    config1 = parse_config("moo.toml")
    sensor1 = Sensor(config1)
    print("Sensor initialized")
    sensor1.start_sensing()


