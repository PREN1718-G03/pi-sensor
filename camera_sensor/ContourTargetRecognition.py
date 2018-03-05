from camera_sensor.TargetRecognition import TargetRecognition
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
        return self.target

    def recognise_target(self, coordinate_array):
        # err_max: How near the two middle points should be in pixels
        err_max = 4
        match = 0
        found = False
        target_coordinates = (None, None)
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
                target_coordinates = coordinates
        return target_coordinates, found

    def run(self):
        self._setup()
        while self.keep_camera_running:
            ret, self.frame = self.cam.read()

    def stop(self):
        self.keep_camera_running = False
