import abc
from TargetModel import TargetModel


class TargetRecognition(object):
    """\
    Abstract class for all target recognition classes / modules
    """

    def __init__(self):
        self.target = TargetModel()
        pass

    @abc.abstractmethod
    def detect_target(self):
        """\
        Tries to detect the target platform and returns a target element
        """
        raise NotImplementedError("Class " + self.__class__.__name__ + " doesn't implement detect_target()")
