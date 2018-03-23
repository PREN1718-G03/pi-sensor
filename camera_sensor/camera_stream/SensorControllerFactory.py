from camera_sensor.SensorController import SensorController


class SensorControllerFactory(object):
    """Delivers an object which is a concrete implementation of SensorController"""

    def __init__(self):
        self.sensor_controller = None

    def get_sensor_controller(self):
        return self.sensor_controller
