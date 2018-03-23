from communicator.SerialCommunicationInterfaceSender import SerialCommunicationInterfaceSender
from communicator.SerialCommunicationInterfaceListener import SerialCommunicationInterfaceListener


class CommunicatorFactory(object):
    """Returns the objects of interfaces CommunicationInterfaceListener and CommunicationInterfaceSender"""

    @staticmethod
    def get_communication_interface_sender():
        return SerialCommunicationInterfaceSender()

    @staticmethod
    def get_communication_interface_listener():
        return SerialCommunicationInterfaceListener()
