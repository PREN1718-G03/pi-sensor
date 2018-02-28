import abc


class SerialObserver(object):
    """\
    Abstract class for the SerialListener
    """
    def __init__(self):
        pass

    @abc.abstractmethod
    def update(self, received_message):
        pass
