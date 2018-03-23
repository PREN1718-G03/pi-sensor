from abc import abstractmethod,ABCMeta


class CommunicationInterfaceSender(object):

    @abstractmethod
    def send_message(self, message):
        pass