from communicator.SerialCommunicationInterfaceSender import SerialCommunicationInterfaceSender
from communicator.SerialCommunicationInterfaceListener import SerialCommunicationInterfaceListener

class CommunicatorFactory(object):
    """Returns the objects of interfaces CommunicationInterfaceListener and CommunicationInterfaceSender"""

    def __init__(self):
        self.__sender = SerialCommunicationInterfaceSender()
        self.__listener = SerialCommunicationInterfaceListener()

    def get_communication_interface_sender(self):
        return self.__sender

    def get_communication_interface_listener(self):
        return self.__listener
