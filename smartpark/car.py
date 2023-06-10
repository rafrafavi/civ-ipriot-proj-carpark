import random
from datetime import datetime

class Car:
    """I created this class Car to create object of cars with random attriubutes to simulate the sort of data a
     carpark might want to keep on their database. I made some list with common car brands and colours """

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
        """this method creates a random registration number to be used for the database """
        registration_number = ''.join(str(random.randint(0, 9)) for _ in range(7))
        return registration_number

    def arrived(self):
        """This method marks the car as parked or not and stamps the times it arrives """
        self.parked = True
        self.arrival = datetime.now()

    def exited(self):
        """This method marks the car as parked or not and stamps the times it exits """
        self.parked = False
        self.exit = datetime.now()