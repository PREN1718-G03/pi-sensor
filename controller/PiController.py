from communicator.CommunicationInterfaceObserver import CommunicationInterfaceObserver
from communicator.CommunicatorFactory import CommunicatorFactory
from communicator.CommunicationInterfaceListener import CommunicationInterfaceListener
from communicator.CommunicationInterfaceSender import CommunicationInterfaceSender
from camera_sensor.CameraSensorFactory import CameraSensorFactory
from camera_sensor.SensorController import SensorController


class PiController(CommunicationInterfaceObserver):
    def update(self, received_message):
        print received_message

    def __init__(self):
        self.__communication_interface_listener = CommunicatorFactory.get_communication_interface_listener()
        self.__communication_interface_sender = CommunicatorFactory.get_communication_interface_sender()

        self.__camera_sensor_factory = CameraSensorFactory()
        self.__camera_sensor = CameraSensorFactory.get_sensor_controller()

        if isinstance(self.__communication_interface_listener, CommunicationInterfaceListener):
            self.__communication_interface_listener.attach(self)

if __name__ == '__main__':
    controller = PiController()
