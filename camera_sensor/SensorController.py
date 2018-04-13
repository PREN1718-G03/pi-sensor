import abc


class SensorController(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_target_and_distance(self):
    	"""Returns if target is found and the distance to the target in cm"""

    @abc.abstractmethod
    def set_height(self, height):
        """Sets the current camera height"""

    @abc.abstractmethod
    def close(self):
        """Cleans up all target recognition and distance calculation objects"""
