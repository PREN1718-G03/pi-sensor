from communicator.ArduinoSerialCommunicationInterfaceSender import ArduinoSerialCommunicationInterfaceSender
from communicator.ArduinoSerialCommunicationInterfaceListener import ArduinoSerialCommunicationInterfaceListener


class CommunicatorFactory(object):
    """Returns the objects of interfaces CommunicationInterfaceListener and CommunicationInterfaceSender"""

    @staticmethod
    def get_communication_interface_sender():
        return ArduinoSerialCommunicationInterfaceSender()

    @staticmethod
    def get_communication_interface_listener():
        return ArduinoSerialCommunicationInterfaceListener()
