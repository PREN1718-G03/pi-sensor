from camera_sensor.DistanceCalculation import DistanceCalculation
from camera_sensor.TargetModel import TargetModel
import cv2
import numpy


class PerspectiveDistanceCalculation(DistanceCalculation):
    def __init__(self):
        self.__target = None
        self.__DEF_CONTOUR_AREA = [
            1.0,
            2.0,
            3.0,
            4.0,
            5.0,
            6.0
        ]
        self.__DEF_DISTANCE = 0.0

    def calculate_distance(self, target):
        if not isinstance(target, TargetModel):
            raise TypeError('target not of type TargetModel')
        else:
            self.__target = target
            self._print_diagnostic_information(target)
            # TODO remove before shipping
            print(self._find_target_center())

    def _calculate_vertical_distance(self):
        result = None
        if self.__target is not None:
            target_center_coordinates = self._calculate_horizontal_distance()
            self._print_diagnostic_information(self.__target, 'Center coordinates ' + str(target_center_coordinates))

            # Sort contours from smallest to biggest
            sorted_contours = []
            for index in range(len(self.__target.contours)):
                if len(sorted_contours) == 0:
                    sorted_contours.append(self.__target.contours[index])
                else:
                    insert_index = 0
                    contour_area = cv2.contourArea(self.__target.contours[index])
                    for sorted_index in range(len(sorted_contours)):
                        sorted_contour_area = cv2.contourArea(self.__target.contours[sorted_index])
                        if contour_area < sorted_contour_area:
                            insert_index = sorted_index
                            break
                        else:
                            insert_index += 1
                    sorted_contours.insert(insert_index)

            # TODO debug - remove before shipping
            print(sorted_contours)

            reduction_factor = []
            for index in range(len(sorted_contours)):
                factor = cv2.contourArea(sorted_contours)/self.__DEF_CONTOUR_AREA[index]
                reduction_factor.append(factor)

            factor = numpy.mean(reduction_factor)
            # Inverse Square Law
            # https://www.youtube.com/watch?v=d-o3eB9sfls
            result = 2 * factor * self.__DEF_DISTANCE
        else:
            raise TypeError('target of type None')
        return result

    def _calculate_horizontal_distance(self, reduction_factor = 1.0):
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
                err_max = 4
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
                    if match > 3:
                        target_center = compared_coordinates
        return target_center

    def _print_diagnostic_information(self, target, message_string=''):
        if isinstance(target, TargetModel):
            i = 0
            for contour in target.contours:
                i += 1
                print('Contour ' + str(i) + ': ' + str(contour))
                print('Area ' + str(cv2.contourArea(contour)))
                print('Sides ' + str(cv2.arcLength(contour)))
                print(str(message_string))
        else:
            pass
