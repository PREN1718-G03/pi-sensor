from unittest import TestCase
from camera_sensor.SensorController import SensorController
from camera_sensor.CameraSensorFactory import CameraSensorFactory


class TestCameraSensorFactory(TestCase):
    def test_get_sensor_controller(self):
        senor_controller = CameraSensorFactory.get_sensor_controller()
        self.assertIsInstance(senor_controller, SensorController)
