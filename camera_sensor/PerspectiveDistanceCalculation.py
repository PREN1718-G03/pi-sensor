from camera_sensor.DistanceCalculation import DistanceCalculation
from camera_sensor.TargetModel import TargetModel
import cv2
import numpy


class PerspectiveDistanceCalculation(DistanceCalculation):
    def __init__(self):
        self.__target = None

    def calculate_distance(self, target):
        if not isinstance(target, TargetModel):
            raise TypeError('target not of type TargetModel')
        else:
            self.__target = target
            self._print_diagnostic_information(target)
            # TODO remove before shipping
            print(self._find_target_center())
            
            height = self._get_vertical_distance()


    def _get_vertical_distance(self):
        return 53.3

    def _calculate_horizontal_distance(self):
        if self.__target is not None:
            pass
        else:
            raise TypeError('target of type None')

    def _find_target_center(self):
        target_center = None
        if isinstance(self.__target, TargetModel):
            # calculate coordinates of specific contours
            coordinate_array = []

            for contour in self.__target.contours:
                moments = cv2.moments(contour)
                cx = int(moments['m10'] / moments['m00'])
                cy = int(moments['m01'] / moments['m00'])

                coordinates = (cx, cy)
                coordinate_array.append(coordinates)

                # err_max: How near the two middle points should be in pixels
                err_max = 20
                match = 0

                compared_coordinates = (0, 0)
                for coordinates in coordinate_array:
                    difference_x = abs(compared_coordinates[0] - coordinates[0])
                    difference_y = abs(compared_coordinates[1] - coordinates[1])
                    if difference_x < err_max and difference_y < err_max:
                        match += 1
                    else:
                        match = 0
                        compared_coordinates = coordinates
                    if match >= 3:
                        target_center = compared_coordinates
        return target_center

    def _print_diagnostic_information(self, target, message_string=''):
        if isinstance(target, TargetModel):
            i = 0
            for contour in target.contours:
                i += 1
                print('Contour ' + str(i) + ': ' + str(contour))
                print('Area ' + str(cv2.contourArea(contour)))
                print(str(message_string))
        else:
            pass
