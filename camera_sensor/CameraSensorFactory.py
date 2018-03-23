from camera_sensor.SensorControllerImplementation import SensorControllerImplementation


class CameraSensorFactory(object):
    """Returns a SensorController object"""

    @staticmethod
    def get_sensor_controller(self):
        return SensorControllerImplementation()
