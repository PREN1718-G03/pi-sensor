from controller.ControllerSerialInterfaceObserver import ControllerSerialInterfaceObserver
from communicator.CommunicatorFactory import CommunicatorFactory
from communicator.CommunicationInterfaceListener import CommunicationInterfaceListener
from communicator.CommunicationInterfaceSender import CommunicationInterfaceSender


class PiController(object):
    def __init__(self):
        communication_interface_observer = ControllerSerialInterfaceObserver()
        communication_interface_listener = CommunicatorFactory.get_communication_interface_listener()
        communication_interface_sender = CommunicatorFactory.get_communication_interface_sender()



if __name__ == '__main__':
    controller = PiController()
