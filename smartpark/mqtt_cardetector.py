import tkinter as tk
import mqtt_device

class CarDetector(mqtt_device.MqttDevice):
    """Provides a couple of simple buttons that can be used to represent a sensor detecting a car. This is a skeleton only."""

    def __init__(self, config):
        super().__init__(config['broker'])
        self.root = tk.Tk()
        self.root.title("Car Detector ULTRA")

        self.btn_incoming_car = tk.Button(
            self.root, text='🚘 Incoming Car', font=('Arial', 50), cursor='right_side', command=self.incoming_car)
        self.btn_incoming_car.pack(padx=10, pady=5)
        self.btn_outgoing_car = tk.Button(
            self.root, text='Outgoing Car 🚘',  font=('Arial', 50), cursor='bottom_left_corner', command=self.outgoing_car)
        self.btn_outgoing_car.pack(padx=10, pady=5)

        self.root.mainloop()


    def incoming_car(self):
        # TODO: implement this method to publish the detection via MQTT - done
        # Publish the incoming car detection via MQTT
        self.client.publish("car/detection", "incoming")
        print("Car goes in")
    def outgoing_car(self):
        # TODO: implement this method to publish the detection via MQTT -done
        self.client.publish("car/detection", "outgoing")
        print("Car goes out")


if __name__ == '__main__':
    # TODO: Run each of these classes in a separate terminal. You should see the CarParkDisplay update when you click the buttons in the CarDetector. -done
    # These classes are not designed to be used in the same module - they are both blocking. If you uncomment one, comment-out the other.

    #CarParkDisplay()
    from config_parser import parse_config
    config = parse_config("config.toml")
    CarDetector(config)