from camera_sensor.DistanceCalculation import DistanceCalculation
from camera_sensor.TargetModel import TargetModel
import unittest


class TestDistanceCalculation(unittest.TestCase):
    def setUp(self):
        self.distance_calculator = DistanceCalculation()

    def testCalculateDistance(self):
        target = TargetModel()
        with self.assertRaises(NotImplementedError):
            self.distance_calculator.calculate_distance(target)

    def testCalculateDistanceBogusAttribute(self):
        target = []
        with self.assertRaises(TypeError):
            self.distance_calculator.calculate_distance(target)

    def tearDown(self):
        pass
