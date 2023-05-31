import paho.mqtt.client as mqtt
import time
import random
import json
from datetime import datetime, date
import car_class
import mqtt_device




class Carpark(mqtt_device.MqttDevice, car_class.Car):
    ''' createa a carpark object to store the state of the car'''

    def __int__(self, config):
        super().__init__(config)
        self.total_spaces = config['total-spaces']
        self.total_cars = config['total-cars']
        self.client.on_message = self.on_message
        self.client.loop_forever()
        self.client.subscribe(self.topic)


    @property
    def avalible_spaces(self):
        avaliable = self.total_spaces - self.total_cars
        return avaliable if avaliable > 0 else 0

    def on_car_entry(self):
        self.total_cars += 1
        # todo : publish to mqtt

    def on_car_exit(self):
        self.total_cars -= 1
        # todo : publish to mqtt

    def on_message(client, userdata, msg, self):
        print(f'Received {msg.payload.decode()}')

    if __name__ == '__main__':
        config = {'name': 'Big Red carpark',
                  'total-spaces': 130,
                  'total-cars': 0,
                  'broker': 'localhost',
                  'port': 1883,
                  'topic-qualifier': 'Carpark'
                  }
    carpark = Carpark(config)
    print("Sensor initialized")


    parking_spaces = {}
    for i in range(1, 193):
        parking_spaces[i] = {"Status": "Empty"}

    random_index = random.sample(range(1, 193), 100)

    for i in random_index:
        car = car_class.Car(parked=True, brand_list=Car.brand_list, colour_list=Car.colour_list)
        car.arrival = datetime.now()
        parking_spaces[i] = {"Status": "Occupied", "Car": car.__dict__}




    def add_car_to_parking(car_data, print_data,parking_spaces):
        empty_spaces = [index for index, value in parking_spaces.items() if value.get("Status") == "Empty"]
        if empty_spaces:
            first_empty_space = empty_spaces[0]
            parking_spaces[first_empty_space]['Status'] = 'Occupied'
            parking_spaces[first_empty_space]['Car'] = car_data
            print("Car has parked in space:", first_empty_space, ", ".join(print_data))
            print("Number of available parking spaces:", len(empty_spaces))
        else:
            print("No empty parking spaces available.")

       # publish_parking_spaces(parking_spaces)  # Publish the updated parking spaces


