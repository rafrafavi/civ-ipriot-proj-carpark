import unittest
from simple_mqtt_carpark import CarPark
from unittest.mock import patch

class Test_CarPark(unittest.TestCase):
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
            'total-cars': 3
        }
        car_park = CarPark(config)
        available_spaces = car_park.available_spaces
        self.assertEqual(available_spaces, 7)

        car_park.total_cars = 12
        available_spaces = car_park.available_spaces
        self.assertEqual(available_spaces, 0)

        car_park.total_cars = 5
        available_spaces = car_park.available_spaces
        self.assertEqual(available_spaces, 5)

    def test_available_spaces_upper_limit(self):
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
            'total-cars': 3
        }
        car_park = CarPark(config)
        available_spaces = car_park.available_spaces
        self.assertEqual(available_spaces, 7)

        car_park.total_cars = 0
        available_spaces = car_park.available_spaces
        self.assertEqual(available_spaces, 10)

        car_park.total_cars -= 4
        available_spaces = car_park.available_spaces
        self.assertEqual(available_spaces, 10)


if __name__ == '__main__':
    unittest.main()