import abc


class SensorController(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_target_and_distance(self):
        raise NotImplementedError('Must define get_target_and_distance to use this class')
