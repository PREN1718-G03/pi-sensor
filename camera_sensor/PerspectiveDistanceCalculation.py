from camera_sensor.DistanceCalculation import DistanceCalculation
from camera_sensor.TargetModel import TargetModel
import cv2


class PerspectiveDistanceCalculation(DistanceCalculation):
    def __init__(self):
        pass

    def calculate_distance(self, target):
        if not isinstance(target, TargetModel):
            raise TypeError('target not of type TargetModel')
        else:
            self._print_diagnostic_information(target)

    def _print_diagnostic_information(self, target):
        if isinstance(target, TargetModel):
            i = 0
            for contour in target.contours:
                i += 1
                print('Contour ' + str(i) + ': ' + str(contour))
                print('Area ' + str(cv2.contourArea(contour)))
                print('Sides ' + str(cv2.arcLength(contour)))
        else:
            pass
