from camera_sensor.ContourTargetRecognition import ContourTargetRecognition
from controller.DistanceToPillarSensor import DistanceToPillarSensor
from controller.HeightSensor import HeightSensor
import os
import cv2


class TestDistanceSensor():
    def __init__(self):
        filepath = os.path.join('/home/pi', 'Testlog.csv')
        self.__log = open(filepath, "w")
        self.__log.write("distance1, distance2, distance3, height1, height2, height3")

    def test_get_multiple_measurements(self):
        distance_sensor = DistanceToPillarSensor()
        height_sensor = HeightSensor()

        distance1 = distance_sensor.get_distance()
        distance2 = distance_sensor.get_distance()
        distance3 = distance_sensor.get_distance()
        height1 = height_sensor.get_height()
        height2 = height_sensor.get_height()
        height3 = height_sensor.get_height()

        self.__log.write(
            str(distance1) + ", " + str(distance2) + ", " + str(distance3) + ", " + str(height1) + ", " + str(
                height2) + ", " + str(height3))

        if distance1 is None or distance2 is None or distance3 is None:
            average_distance = None
        else:
            average_distance = (distance1 + distance2 + distance3) / 3
        print "Distance: " + str(average_distance) + " "
        if height1 is None or height2 is None or height3 is None:
            average_height = None
        else:
            average_height = (height1 + height2 + height3) / 3

        print "Height: " + str(average_height) + " "


if __name__ == '__main__':
    sensor = TestDistanceSensor()
    target_recogniser = ContourTargetRecognition()
    target_recogniser.start()
    not_stopped = True
    bildnummer = 1
    while not_stopped:
        sensor.test_get_multiple_measurements()
        frame = target_recogniser.get_camera_frame()
        image_path = os.path.join('/home/pi', 'image_US_' + str(bildnummer) + '.jpg')
        bildnummer += 1
        cv2.imwrite(image_path, frame)
        user_input = raw_input("Press Enter: ")
        if user_input == "end":
            not_stopped = False
    target_recogniser.stop()
