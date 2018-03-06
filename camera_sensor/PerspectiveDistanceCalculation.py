from camera_sensor.DistanceCalculation import DistanceCalculation
from camera_sensor.TargetModel import TargetModel


class PerspectiveDistanceCalculation(DistanceCalculation):
    def __init__(self):
        pass

    def calculate_distance(self, target):
        if not isinstance(target, TargetModel):
            raise TypeError('target not of type TargetModel')
        else:
            pass