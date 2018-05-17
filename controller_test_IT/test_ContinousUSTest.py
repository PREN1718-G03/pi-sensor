from controller.DistanceToPillarSensor import DistanceToPillarSensor
from controller.HeightSensor import HeightSensor
import os
import datetime


def test_get_multiple_measurements(filename, index):
    log_file = open(filename, 'a')
    log_file.write('--- ' + str(index) + ' ---\n')
    log_file.write(str(datetime.datetime.now()) + '\n')
    average_height = 0
    average_distance = 0
    distance1 = distance_sensor.get_distance()
    distance2 = distance_sensor.get_distance()
    distance3 = distance_sensor.get_distance()
    height1 = height_sensor.get_height()
    height2 = height_sensor.get_height()
    height3 = height_sensor.get_height()

    log_file.write("Distance 1: " + str(distance1) + '\n')
    log_file.write("Distance 2: " + str(distance2) + '\n')
    log_file.write("Distance 3: " + str(distance3) + '\n')

    log_file.write("Height 1: " + str(height1) + '\n')
    log_file.write("Height 2: " + str(height2) + '\n')
    log_file.write("Height 3: " + str(height3) + '\n')

    if not (distance1 is None or distance2 is None or distance3 is None):
        average_distance = (distance1 + distance2 + distance3) / 3
        log_file.write(str(average_distance) + '\n')

    if not (height1 is None or height2 is None or height3 is None):
        average_height = (height1 + height2 + height3) / 3
        log_file.write(str(average_height) + '\n')

    log_file.close()


if __name__ == '__main__':
    distance_sensor = DistanceToPillarSensor()
    height_sensor = HeightSensor()
    home = os.chdir('/home/pi/logs')
    file = 'us_log.txt'
    with open(file, 'w') as logfile:
        logfile.write(str(datetime.datetime.now()) + '\n')
    index = 1
    while True:
        test_get_multiple_measurements(file, index)
        index += 1
