import tkinter as tk

class CarDetector:
    """Provides a couple of simple buttons that can be used to represent a sensor detecting a car. This is a skeleton only."""

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

    def incoming_car(self):
        # TODO: implement this method to publish the detection via MQTT
        """if data['CarParks'][0]['total-spaces'] > 0 and data['CarParks'][0]['total-cars'] < 130:
            data['CarParks'][0]['total-spaces'] -= 1
            data['CarParks'][0]['total-cars'] += 1
            print("Car goes in")
        else:
            print("Car cannot go in because car park is full")
        print(data)
        """

        print("Car goes in")



    def outgoing_car(self):
        # TODO: implement this method to publish the detection via MQTT
        """if data['CarParks'][0]['total-cars'] > 0:
            data['CarParks'][0]['total-spaces'] += 1
            data['CarParks'][0]['total-cars'] -= 1
            print("Car goes out")
        else:
            print("Car park is empty.")
        print(data)
        """

        print("Car goes out")
