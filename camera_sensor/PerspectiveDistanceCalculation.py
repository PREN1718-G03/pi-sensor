from camera_sensor.DistanceCalculation import DistanceCalculation
from camera_sensor.TargetModel import TargetModel
import cv2
import numpy


class PerspectiveDistanceCalculation(DistanceCalculation):

    def __init__(self):
        self.__target = None
        self.__CENTER_COORDINATES = (545, 240)
        self.__height = 52.5

    def calculate_distance(self, target):
        if not isinstance(target, TargetModel):
            raise TypeError('target not of type TargetModel')
        else:
            self.__target = target
            distance_to_target = self.__calculate_horizontal_distance(self.__height)
        return distance_to_target

    def set_height(self, height):
        if isinstance(height, float):
            self.__height = height
        else:
            raise TypeError('height not of type float')
        return True

    def __calculate_horizontal_distance(self, height):
        if height <= 50.0 or 90.0 <= height:
            print('height out of bounds for model')
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
            print ('target of type None')

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
