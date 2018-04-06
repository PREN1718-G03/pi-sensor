from unittest import TestCase
from camera_sensor.HeightSensor import HeightSensor


class TestHeightSensor(TestCase):
    def test_get_height(self):
        sensor = HeightSensor()
        height = sensor.get_height()
        self.assertIsInstance(height, float)