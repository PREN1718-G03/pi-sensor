import unittest
from camera_sensor.TargetModel import TargetModel

class TestTargetModel(TestCase):
    def setUp(self):
        pass

    def testConstructor(self):
        target = TargetModel()
        assert isinstance(target, TargetModel)

    def testConstructorWithAttributes(self):
        target_found = True
        polygons = [1,2,3]
        distance = -1.0

        target = TargetModel(target_found,polygons,distance)

        if target.target_found != target_found:
            self.fail('target_found not set')
        if target.polygons != polygons:
            self.fail('polygons not set')
        if target.distance != distance:
            self.fail('distance not set')

    @unittest.expectedFailure
    def testConstructorTarget_foundBogusAttribute(self):
        self.fail()

    @unittest.expectedFailure
    def testConstructorDistanceBogusAttribute(self):
        self.fail()

    @unittest.expectedFailure
    def testConstructorPolygonsBogusAttribute(self):
        self.fail()

    def tearDown(self):
        pass
