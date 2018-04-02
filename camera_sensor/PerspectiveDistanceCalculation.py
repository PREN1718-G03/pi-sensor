from camera_sensor.DistanceCalculation import DistanceCalculation
from camera_sensor.TargetModel import TargetModel
import cv2
import numpy


class PerspectiveDistanceCalculation(DistanceCalculation):

    def __init__(self):
        self.__target = None
        self.__CENTER_COORDINATES = (545, 240)

    def calculate_distance(self, target):
        if not isinstance(target, TargetModel):
            raise TypeError('target not of type TargetModel')
        else:
            self.__target = target
            self.__print_diagnostic_information(target)

            height = self.__get_vertical_distance()
            distance_to_target = self.__calculate_horizontal_distance(height)
        return distance_to_target


    def __get_vertical_distance(self):
        return 52.5

    def __calculate_horizontal_distance(self, height):
        if 50.0 <= height <= 90.0:
            if self.__target is not None:
                target_center = self.__find_target_center()
                pixel_distance_to_target_center = numpy.sqrt(((target_center[0]) - self.__CENTER_COORDINATES[0]) ** 2
                                     + ((target_center[1]) - self.__CENTER_COORDINATES[1]) ** 2)
                a = 0.000115
                b = 0.002585856 * height - 0.064546103
                c = -2/75 * height + 3/5
                # CM = a * px^2 + b * px + c
                cm_distance_to_target_center = a * pixel_distance_to_target_center ** 2 \
                                               + b * pixel_distance_to_target_center + c
                return cm_distance_to_target_center
            else:
                raise TypeError('target of type None')
        else:
            raise AttributeError('height out of bounds for model')

    def __find_target_center(self):
        target_center = (0,0)
        if isinstance(self.__target, TargetModel):
            # calculate coordinates of specific contours
            target_centers = []

            for contour in self.__target.contours:
                moments = cv2.moments(contour)
                cx = int(moments['m10'] / moments['m00'])
                cy = int(moments['m01'] / moments['m00'])

                coordinates = (cx, cy)
                target_centers.append(coordinates)

            count = 0
            sum_x = 0
            sum_y = 0
            for (x, y) in target_centers:
                count += 1
                sum_x += x
                sum_y += y
            if count == 0:
                count = 1
            average_x = sum_x / count
            average_y = sum_y / count
            target_center = (average_x, average_y)
        return target_center

    def __print_diagnostic_information(self, target, message_string=''):
        if isinstance(target, TargetModel):
            i = 0
            for contour in target.contours:
                i += 1
                print('Contour ' + str(i) + ': ' + str(contour))
                print('Area ' + str(cv2.contourArea(contour)))
                print(str(message_string))
            if target.target_found:
                target_center = self.__find_target_center()
                print numpy.sqrt(((target_center[0]) - self.__CENTER_COORDINATES[0]) ** 2
                                 + ((target_center[1]) - self.__CENTER_COORDINATES[1]) ** 2)
        else:
            pass
