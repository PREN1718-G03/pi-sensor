import abc


class SensorController(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_target_and_distance(self):
    	"""Returns if target is found and the distance to the target in cm"""
        raise NotImplementedError('Must define get_target_and_distance to use this class')
