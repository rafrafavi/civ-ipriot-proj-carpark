import time

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
