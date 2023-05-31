""""Demonstrates a simple implementation of an 'event' listener that triggers
a publication via mqtt"""

import mqtt_device

class Sensor(mqtt_device.MqttDevice):

    def on_detection(self, message):
        """Triggered when a detection occurs"""
        self.client.publish(self.topic, message)

    def start_sensing(self):
        """ A blocking event loop that waits for detection events, in this
        case Enter presses"""
        while True:
            input("Press Enter when 🚗 detected!")
            self.on_detection("Car-Detected")


if __name__ == '__main__':
    config = {'name': 'sensor',
              'location': 'L306',
              'topic-root': "lot",
              'broker': 'localhost',
              'port': 1883,
              'topic-qualifier': 'entry'
              }

    sensor = Sensor(config)
    print("Sensor initialized")
    sensor.start_sensing()
