from unittest import TestCase
from controller.DistanceToPillarSensor import DistanceToPillarSensor
from controller.HeightSensor import HeightSensor


class TestDistanceSensor(TestCase):
    def test_get_distance(self):
        sensor = DistanceToPillarSensor()
        height = sensor.get_distance()
        self.assertIsInstance(height, float)
        print height
        sensor.close()

    def test_get_height(self):
        sensor = HeightSensor()
        height = sensor.get_height()
        self.assertIsInstance(height, float)
        print height
        sensor.close()

    def test_get_multiple_measurements(self):
        distance_sensor = DistanceToPillarSensor()
        height_sensor = HeightSensor()

        distance1 = distance_sensor.get_distance()
        distance2 = distance_sensor.get_distance()
        distance3 = distance_sensor.get_distance()
        height1 = height_sensor.get_height()
        height2 = height_sensor.get_height()
        height3 = height_sensor.get_height()

        print "Distance 1: " + str(distance1)
        print "Distance 2: " + str(distance2)
        print "Distance 3: " + str(distance3)

        print "Height 1: " + str(height1)
        print "Height 2: " + str(height2)
        print "Height 3: " + str(height3)

        average_distance = (distance1 + distance2 + distance3)/3

        distance_difference = distance1 - average_distance
        print "Difference: " + str(distance_difference)

        average_height = (height1 + height2 + height3)/3

        height_difference = height1 - average_height
        print "Difference: " + str(height_difference)

        assert -2.5 < distance_difference < 2.5
        assert -2.5 < height_difference < 2.5
