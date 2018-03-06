from camera_sensor.PerspectiveDistanceCalculation import PerspectiveDistanceCalculation
from camera_sensor.TargetModel import TargetModel
import unittest


class TestDistanceCalculation(unittest.TestCase):
    def setUp(self):
        self.distance_calculator = PerspectiveDistanceCalculation()

    def testCalculateDistance(self):
        target = TargetModel()
        distance = self.distance_calculator.calculate_distance(target)
        assert isinstance(distance, float)

    def testCalculateDistanceBogusAttribute(self):
        target = []
        with self.assertRaises(TypeError):
            self.distance_calculator.calculate_distance(target)

    def tearDown(self):
        pass
