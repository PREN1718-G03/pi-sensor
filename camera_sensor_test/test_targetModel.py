import unittest
from camera_sensor.TargetModel import TargetModel


class TestTargetModel(unittest.TestCase):
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
        target_found = None
        polygons = [1, 2, 3]
        distance = -1.0
        TargetModel(target_found, polygons, distance)

    def testConstructorDistanceBogusAttribute(self):
        target_found = True
        polygons = [1, 2, 3]
        distance = 'Fail'
        target = TargetModel(target_found, polygons, distance)
        assert (target.distance is None)

    @unittest.expectedFailure
    def testConstructorPolygonsBogusAttribute(self):
        target_found = True
        polygons = 1
        distance = -1.0
        TargetModel(target_found, polygons, distance)


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()