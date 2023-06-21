import unittest
from simple_mqtt_carpark import CarPark
from unittest.mock import patch

class Test_NegativeCarCheck(unittest.TestCase):
    def test_available_spaces_lower_limit(self):
        # Mock the MQTT client and disable the loop
        self.patcher = patch('paho.mqtt.client.Client')
        self.mock_client_class = self.patcher.start()
        self.mock_client = self.mock_client_class.return_value
        self.mock_client.loop_start.return_value = None
        self.mock_client.loop_stop.return_value = None

        # Carpark Instance
        config = {
            'name': 'Test Car Park',
            'location': 'Test Location',
            'topic-root': 'test root',
            'topic-qualifier': 'test qualifier',
            "broker": "127.0.0.1",
            "port": 1883,
            'total-spaces': 10,
            'total-cars': 0
        }

        car_park = CarPark(config)
        car_park.temperature = 25

        # Set total_cars to a negative value
        car_park.on_car_exit()
        # The total cars should be 0
        total_cars = car_park.total_cars
        self.assertEqual(total_cars, 0)

if __name__ == '__main__':
    unittest.main()