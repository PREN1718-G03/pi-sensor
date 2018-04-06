from camera_sensor.PerspectiveDistanceCalculation import PerspectiveDistanceCalculation
from camera_sensor.TargetModel import TargetModel
import unittest


class TestDistanceCalculation(unittest.TestCase):
    def setUp(self):
        self.distance_calculator = PerspectiveDistanceCalculation()

    def testSetHeight(self):
        height = 55.0
        assert self.distance_calculator.set_height(height)

    def testSetHeightBogusAttribute(self):
        height = 'a'
        with self.assertRaises(TypeError):
            self.distance_calculator.set_height(height)

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
