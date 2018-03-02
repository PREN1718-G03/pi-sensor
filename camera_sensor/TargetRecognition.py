import abc
import TargetModel

class TargetRecognition(object):
    """\
    Abstract class for all target recognition classes / modules
    """

    def __init__(self):
        self.target = TargetModel()
        pass

    @abc.abstractmethod
    def detect_target(self):
        raise NotImplementedError("Class %s doesn't implement aMethod()" % self.__class__.__name__)
        return self.target
