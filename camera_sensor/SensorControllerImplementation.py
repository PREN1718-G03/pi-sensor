from SensorController import SensorController
from ContourTargetRecognition import ContourTargetRecognition
from PerspectiveDistanceCalculation import PerspectiveDistanceCalculation
from TargetModel import TargetModel


class SensorControllerImplementation(SensorController):
    def __init__(self):
        self.__target_recognition = ContourTargetRecognition()
        self.__distance_calculation = PerspectiveDistanceCalculation()
        self.__target_recognition.start()

    def get_target_and_distance(self):
        target = self.__target_recognition.detect_target()
        distance = None
        if isinstance(target, TargetModel):
            if target.target_found:
                distance = self.__distance_calculation.calculate_distance(target)
            return target.target_found, distance

    def set_height(self):
        self.__distance_calculation.set_height()

    def close(self):
        self.__target_recognition.stop()
