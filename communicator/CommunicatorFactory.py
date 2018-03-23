from communicator.SerialCommunicationInterfaceSender import SerialCommunicationInterfaceSender
from communicator.SerialCommunicationInterfaceListener import SerialCommunicationInterfaceListener


class CommunicatorFactory(object):
    """Returns the objects of interfaces CommunicationInterfaceListener and CommunicationInterfaceSender"""

    @staticmethod
    def get_communication_interface_sender(self):
        return SerialCommunicationInterfaceSender()

    @staticmethod
    def get_communication_interface_listener(self):
        return SerialCommunicationInterfaceListener()
