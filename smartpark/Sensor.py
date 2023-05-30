
from sense_hat import SenseHat

class Sensor:
    def __init__(self):
        self.sense_hat = SenseHat()

    def get_temperature(self):
        return self.sense_hat.get_temperature()