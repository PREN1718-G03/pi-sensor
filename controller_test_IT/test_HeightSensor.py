from unittest import TestCase
from controller.HeightSensor import HeightSensor

class TestHeightSensor(TestCase):
    def test_get_height(self):
        sensor = HeightSensor()
        height = sensor.get_height()
        self.assertIsInstance(height, float)
        print height
        sensor.close()

    def test_get_multiple_measurements(self):
        sensor = HeightSensor()
        height1 = sensor.get_height()
        height2 = sensor.get_height()
        height3 = sensor.get_height()

        print "Height 1: " + str(height1)
        print "Height 2: " + str(height2)
        print "Height 3: " + str(height3)

        average_height = (height1 + height2 + height3)/3

        difference = height1 - average_height
        print "Difference: " + str(difference)

        assert -2.5 < difference < 2.5
