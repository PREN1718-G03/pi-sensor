import unittest
from communicator.CommunicatorFactory import CommunicatorFactory
from communicator.CommunicationInterfaceListener import CommunicationInterfaceListener
from communicator.CommunicationInterfaceSender import CommunicationInterfaceSender


class test_SerialCommunicatorFactory(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_communication_interface_sender(self):
        sender = CommunicatorFactory.get_communication_interface_sender()
        self.assertIsInstance(sender, CommunicationInterfaceSender)

    def test_get_communication_interface_listener(self):
        listener = CommunicatorFactory.get_communication_interface_listener()
        self.assertIsInstance(listener, CommunicationInterfaceListener)
