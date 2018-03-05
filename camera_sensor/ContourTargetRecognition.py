from camera_sensor.TargetRecognition import TargetRecognition
from camera_sensor.TargetRecognition import TargetModel


class ContourTargetRecognition(TargetRecognition):
    def __init__(self):
        super(ContourTargetRecognition, self).__init__()
        pass

    def detect_target(self):
        return self.target
