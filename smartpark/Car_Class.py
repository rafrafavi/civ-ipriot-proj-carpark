import random
from datetime import datetime





class Car:

    brand_list = ["Toyota", "Ford", "Honda", "Tesla", "BMW", "Audi", "Mercedes"]
    colour_list = ["Red", "Blue", "Green", "White", "Black", "Yellow"]

    def __init__(self, parked, brand_list, colour_list ):
        self.brand = random.choice(brand_list)
        self.colour = random.choice(colour_list)
        self.registration = self.generate_registration()
        self.parked = parked
        self.arrival = None
        self.exit = None

    def generate_registration(self):
        # Generate a random 7-digit registration number
        registration_number = ''.join(str(random.randint(0, 9)) for _ in range(7))
        return registration_number

    def arrived(self):
        self.parked = True
        self.arrival = datetime.now()

    def exited(self):
        self.parked = False
        self.exit = datetime.now()