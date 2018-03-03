import abc
from TargetModel import TargetModel


class DistanceCalculation(object):
    @abc.abstractmethod
    def calculate_distance(self, target):
        if not isinstance(target, TargetModel):
            raise TypeError('target not of type TargetModel')
        raise NotImplementedError("Class %s doesn't implement aMethod()" % self.__class__.__name__)
