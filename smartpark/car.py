import sensor
import random


class Car:

    def __init__(self):
        with open("../sample_data/license_plates.txt", "r") as license_plate:
            all_license_plates = license_plate.read()
            plates = all_license_plates.split()
            plates_line_pos = random.randint(0, len(plates) - 1)
            print(plates[plates_line_pos])
            print(plates_line_pos)

        with open("../sample_data/car_makes.txt", "r") as car_make:
            all_car_makes = car_make.read()
            makes = all_car_makes.split()
            makes_line_pos = random.randint(0, len(makes) - 1)
            print(makes[makes_line_pos])
            print(makes_line_pos)

    entry = ...
    exit = ...


car1 = Car()
