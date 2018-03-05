from camera_sensor.TargetRecognition import TargetRecognition
from camera_sensor.TargetModel import TargetModel
from VideoStream import VideoStream
from SingletonMetaclass import Singleton
import cv2
import copy
import time
import threading


class ContourTargetRecognition(TargetRecognition, threading.Thread):
    __metaclass__ = Singleton

    def __init__(self):
        super(ContourTargetRecognition, self).__init__()
        threading.Thread.__init__(self)
        self.keep_camera_running = True
        self.frame = []

    def _setup(self):
        self.cam = VideoStream().start()
        time.sleep(2.0)

    def detect_target(self):
        # Empty lists are considered false in Python
        if not self.frame.count():
            pass

            # Change the picture to gray scale
            gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)

            # Calculate the binary threshold -> Everything lower than threshold turns black, everything over turns white
            ret_threshold, threshold = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

            # Find the contours, RETR_TREE preserves the inner contours and doesn't limit itself to the outermost one like RETR_EXTERNAL
            image_contours, contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            # I want to enumerate the found rectangles
            rect_count = 0
            coordinate_array = []

            for contour in contours:
                perimeter = cv2.arcLength(contour, True)
                # Epsilon = Maximum Distance from contour to approximated contour; Usually 1-5% of ArcLength,
                # we're setting it to 15% :D
                epsilon = 0.15 * perimeter
                approximated_contour = cv2.approxPolyDP(contour, epsilon, True)

                contour_area = cv2.contourArea(approximated_contour)
                if len(approximated_contour) == 4 and contour_area > 50.0:
                    rect_count += 1

                    # Calculate the centroid from moments https://docs.opencv.org/trunk/dd/d49/tutorial_py_contour_features.html
                    moments = cv2.moments(approximated_contour)
                    cx = int(moments['m10'] / moments['m00'])
                    cy = int(moments['m01'] / moments['m00'])

                    coordinates = (cx, cy)
                    coordinate_array.append(coordinates)

                print coordinate_array
                target_found = self.recognise_target(coordinate_array)
                self.target = TargetModel(target_found, coordinate_array)
        return self.target

    def recognise_target(self, coordinate_array):
        # err_max: How near the two middle points should be in pixels
        err_max = 4
        match = 0
        found = False
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
                found = True
        return found

    def run(self):
        self._setup()
        while self.keep_camera_running:
            ret, self.frame = self.cam.read()

    def stop(self):
        self.keep_camera_running = False
