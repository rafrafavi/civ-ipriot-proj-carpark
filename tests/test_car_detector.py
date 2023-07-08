import sys
import os
import unittest

# Add the parent directory to sys.path to recognize the import
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from displays.car_detector import CarDetector
class TestCarDetector(unittest.TestCase):
    def test_incoming_car(self):
        # Test case for incoming car event
        config = {
            'name': 'Test Car Detector',
            'total-spaces': 10,
            'broker': 'localhost',
            'port': 1883
        }
        car_detector = CarDetector(config)
        car_detector.incoming_car()
        self.assertEqual(car_detector.available_bays, 1)

    def test_outgoing_car(self):
        # Test case for outgoing car event
        config = {
            'name': 'Test Car Detector',
            'total-spaces': 10,
            'broker': 'localhost',
            'port': 1883
        }
        car_detector = CarDetector(config)
        car_detector.available_bays = 5
        car_detector.outgoing_car()
        self.assertEqual(car_detector.available_bays, 4)

if __name__ == '__main__':
    unittest.main()
