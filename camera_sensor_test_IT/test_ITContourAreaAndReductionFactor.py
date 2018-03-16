from camera_sensor.ContourTargetRecognition import ContourTargetRecognition
from camera_sensor.PerspectiveDistanceCalculation import PerspectiveDistanceCalculation
import cv2
import os
import datetime

class ContourAreaAndReductionFactorTest(object):
    def __init__(self):
        self.target_recogniser = ContourTargetRecognition()
        self.distance_calculator = PerspectiveDistanceCalculation()
        self.run = True

    def start_test(self):
        self.target_recogniser.start()
        os.chdir('/home/pi/Desktop')
        bildnummer = 0
        while self.run:
            user_input = raw_input("Press Enter...")
            bildnummer += 1
            if str(user_input) == 'end':
                self.run = False
            else:
                target = self.target_recogniser.detect_target()
                self.distance_calculator.calculate_distance(target)
                frame = self.target_recogniser.cam.read()
                image_name = './imagePython' + str(bildnummer) + '.jpg'
                cv2.imwrite(image_name, frame)
        self.end_test_and_cleanup()

    def end_test_and_cleanup(self):
        self.target_recogniser.stop()


if __name__ == '__main__':
    tester = ContourAreaAndReductionFactorTest()
    tester.start_test()
