from abc import abstractmethod


class CommunicationInterfaceListener(object):

    @abstractmethod
    def attach(self, observer):
        raise NotImplementedError

    @abstractmethod
    def detach(self, observer):
        raise NotImplementedError

    @abstractmethod
    def _notify(self, received_message):
        raise NotImplementedError

    @abstractmethod
    def run(self):
        raise NotImplementedError

    @abstractmethod
    def stop(self):
        raise NotImplementedError
