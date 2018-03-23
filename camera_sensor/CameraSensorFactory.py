from camera_sensor.SensorController import SensorController


class CameraSensorFactory(object):
    """Returns a SensorController object"""

    def __init__(self):
        self.__sensor_controller = None

    def get_sensor_controller(self):
        return self.__sensor_controller
