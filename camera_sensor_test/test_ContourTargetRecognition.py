from camera_sensor.ContourTargetRecognition import ContourTargetRecognition
from camera_sensor.TargetModel import TargetModel
import unittest


class TestTargetRecognition(unittest.TestCase):
    def setUp(self):
        self.target_recogniser = ContourTargetRecognition()
        self.target_recogniser.start()

    def testTargetRecognition(self):
        target = self.target_recogniser.detect_target()
        self.assertIsInstance(target, TargetModel)

    def tearDown(self):
        self.target_recogniser.stop()
        pass
