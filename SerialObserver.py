import abc

class SerialObserver:
    """\
    Abstract class for the SerialListener
    """

    @abc.abstractmethod
    def update(self, receivedMessage):
        pass