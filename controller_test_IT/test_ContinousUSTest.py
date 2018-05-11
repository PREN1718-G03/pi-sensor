from controller.DistanceToPillarSensor import DistanceToPillarSensor
from controller.HeightSensor import HeightSensor


def test_get_multiple_measurements():
    distance1 = distance_sensor.get_distance()
    distance2 = distance_sensor.get_distance()
    distance3 = distance_sensor.get_distance()
    # height1 = height_sensor.get_height()
    # height2 = height_sensor.get_height()
    # height3 = height_sensor.get_height()
    #
    print "Distance 1: " + str(distance1)
    print "Distance 2: " + str(distance2)
    print "Distance 3: " + str(distance3)
    #
    # print "Height 1: " + str(height1)
    # print "Height 2: " + str(height2)
    # print "Height 3: " + str(height3)
    #
    average_distance = (distance1 + distance2 + distance3) / 3

    distance_difference = distance1 - average_distance
    print "Difference: " + str(distance_difference)
    #
    # average_height = (height1 + height2 + height3) / 3
    #
    # height_difference = height1 - average_height
    # print "Difference: " + str(height_difference)

if __name__ == '__main__':
    distance_sensor = DistanceToPillarSensor()
    height_sensor = HeightSensor()
    while True:
        test_get_multiple_measurements()