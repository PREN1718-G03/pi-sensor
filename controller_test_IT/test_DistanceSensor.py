from unittest import TestCase
from controller.DistanceToPillarSensor import DistanceToPillarSensor


class TestDistanceSensor(TestCase):
    def test_get_distance(self):
        sensor = DistanceToPillarSensor()
        height = sensor.get_distance()
        self.assertIsInstance(height, float)
        print height
        sensor.close()

    def test_get_multiple_measurements(self):
        sensor = DistanceToPillarSensor()
        distance1 = sensor.get_distance()
        distance2 = sensor.get_distance()
        distance3 = sensor.get_distance()

        print "Height 1: " + str(distance1)
        print "Height 2: " + str(distance2)
        print "Height 3: " + str(distance3)

        average_distance = (distance1 + distance2 + distance3)/3

        difference = distance1 - average_distance
        print "Difference: " + str(difference)

        assert -2.5 < difference < 2.5
