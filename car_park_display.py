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

