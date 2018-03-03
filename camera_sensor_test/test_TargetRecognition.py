from camera_sensor.TargetRecognition import TargetRecognition
from camera_sensor.TargetModel import TargetModel
import unittest


class TestDistanceCalculation(unittest.TestCase):
    def setUp(self):
        self.target_recogniser = TargetRecognition()

    def testTargetRecognition(self):
        with self.assertRaises(NotImplementedError):
            target = self.target_recogniser.detect_target()
            self.assertIsInstance(target, TargetModel)

    def tearDown(self):
        pass
