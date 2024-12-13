import random
import threading
import time
from windowed_display import WindowedDisplay


class CarParkDisplay:
    """Provides a simple display of the car park status. This is a skeleton only. The class is designed to be customizable without requiring an understanding of tkinter or threading."""

    # determines what fields appear in the UI
    fields = ['Available bays', 'Temperature', 'At']

    def __init__(self):
        self.window = WindowedDisplay('Moondalup', CarParkDisplay.fields)
        updater = threading.Thread(target=self.check_updates)
        updater.daemon = True
        updater.start()
        self.window.show()

    def check_updates(self):
        while True:
            # NOTE: Dictionary keys *must* be the same as the class fields
            field_values = dict(zip(CarParkDisplay.fields, [
                f'{random.randint(0, 150):03d}',
                f'{random.randint(0, 45):02d}℃',
                time.strftime("%H:%M:%S")]))
            # Pretending to wait on updates from MQTT
            time.sleep(1)


class CarDetector:
    """Simulates a car detection system and updates the car park display."""

    def __init__(self, car_park_display):
        self.car_park_display = car_park_display

    def simulate_car_entry(self):
        print("Car detected entering the car park.")
        # Pretending to perform car entry operations...
        time.sleep(2)
        self.update_display()

    def simulate_car_exit(self):
        print("Car detected exiting the car park.")
        # Pretending to perform car exit operations...
        time.sleep(2)
        self.update_display()

    def update_display(self):
        # Update the car park display by triggering an update
        self.car_park_display.check_updates()


if __name__ == "__main__":
    car_park_display = CarParkDisplay()
    car_detector = CarDetector(car_park_display)

    # Simulate car entry and exit
    car_detector.simulate_car_entry()
    car_detector.simulate_car_exit()
