import paho.mqtt.client as paho
import mqtt_device
import time
import random
import json
from datetime import datetime
from car import Car

class Carpark(mqtt_device.MqttDevice):
    """Creates a carpark object to store the state of cars in the lot"""

    def __init__(self, config):
        super().__init__(config)
        self.config = config
        self.total_spaces = config['total-spaces']
        self.total_cars = config['total-cars']
        self.client.on_message = self.on_message
        self.client.subscribe('+/+/+/+')
        self.parking_spaces = {}
        for i in range(1, 130):
            self.parking_spaces[i] = {"Status": "Empty"}
        random_index = random.sample(range(1, 130), 70)
        for i in random_index:
            car = Car(parked=True, brand_list=Car.brand_list, colour_list=Car.colour_list)
            car.arrival = datetime.now()
            self.parking_spaces[i] = {"Status": "Occupied", "Car": car.__dict__}
        self.client.loop_forever()

    @property
    def available_spaces(self):
        available = self.total_spaces - self.total_cars
        return available if available > 0 else 0

    def on_car_entry(self, car_dict, temp):
        for space, status in self.parking_spaces.items():
            if status["Status"] == "Empty":
                parking_space = space
                break

        if parking_space is None:
            print("No available parking spaces")
            return
        car = car_dict["Car"]



        self.parking_spaces[parking_space]["Status"] = "Occupied"
        self.parking_spaces[parking_space]["Car"] = car

        self.total_cars += 1

        topic = f"lot/{self.config['location']}/sensor/car_arrived"
        message = f"A car arrived at parking space {parking_space}. Total parked cars: {self.total_cars}. " \
                  f"Total empty parking bays: {self.available_spaces}\n       The current temperature is : {temp}"
        self.client.publish(topic, message)
        print(message)



    def on_car_exit(self,message, temp):
  #suscribe to topic to change to amout of cars
        if message == "Car Exited":
            occupied_spaces = [space for space, status in self.parking_spaces.items() if status["Status"] == "Occupied"]
            selected_space = random.choice(occupied_spaces)
            car = self.parking_spaces[selected_space]["Car"]
            colour = car["colour"]
            brand = car["brand"]

            del self.parking_spaces[selected_space]
            self.parking_spaces[selected_space] = {"Status": "Empty"}

            self.total_cars -= 1
            print(f"A {colour} {brand} has exited. There are {self.total_cars} cars parked and "
                  f"{self.available_spaces} parking spaces left\n       The current temperature is : {temp}")
            topic = "lot/L306/sensor/car_left"
            message = f"A car has exited the carpark. Total parked cars: {self.total_cars}. " \
                      f"Total empty parking bays {self.available_spaces}\n    The current temperature is : {temp}"
            self.client.publish(topic, message)
            #print(message)












    def on_message(self, client, userdata, msg):
        msg_data = msg.payload.decode("utf-8")
        topic = msg.topic
        print(f"Received message. Topic: {topic}, Payload: {msg_data}")

        if topic == 'lot/L306/sensor/entry':
            msg_data = json.loads(msg_data)
            car_dict = msg_data[0]
            temp = msg_data[1][1]
            self.on_car_entry(car_dict, temp)
            brand = car_dict["Car"]["brand"]
            colour = car_dict["Car"]["colour"]
            print(f"A {colour} {brand} has parked there are {self.total_cars} cars parked and "
                  f"{self.available_spaces} parking spaces left")

        elif topic == "lot/L306/sensor/car_exited":
            msg_data = json.loads(msg_data)
            temp = msg_data[1]
            message = msg_data[0]
            self.on_car_exit(message, temp)








if __name__ == '__main__':
    config = {'name': "raf-park",
              'total-spaces': 130,
              'total-cars': 70,
              'location': 'L306',
              'topic-root': "lot",
              'broker': 'localhost',
              'port': 1883,
              'topic-qualifier': 'entry'
              }

    carpark = Carpark(config)

    carpark.client.loop_forever()
    print("Carpark initialized")



