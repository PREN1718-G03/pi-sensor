from communicator.CommunicationInterfaceObserver import CommunicationInterfaceObserver
from communicator.CommunicatorFactory import CommunicatorFactory
from communicator.CommunicationInterfaceListener import CommunicationInterfaceListener
from communicator.CommunicationInterfaceSender import CommunicationInterfaceSender
from camera_sensor.CameraSensorFactory import CameraSensorFactory
from camera_sensor.SensorController import SensorController
from controller.HeightSensor import HeightSensor
import warnings

class PiController(CommunicationInterfaceObserver):
    # Implementation of SerialInterfaceObserver methods
    def update(self, received_message):
        print received_message

    def __init__(self):
        self.__communication_interface_listener = CommunicatorFactory.get_communication_interface_listener()
        self.__communication_interface_sender = CommunicatorFactory.get_communication_interface_sender()

        self.__camera_sensor_factory = CameraSensorFactory()
        self.__camera_sensor = CameraSensorFactory.get_sensor_controller()

        self.__height_sensor = HeightSensor()

        if isinstance(self.__communication_interface_listener, CommunicationInterfaceListener):
            print "Setting up listener"
            self.__communication_interface_listener.start()
            self.__communication_interface_listener.attach(self)
        else:
            warnings.warn("Listener not started", RuntimeWarning)

        if not isinstance(self.__communication_interface_sender, CommunicationInterfaceSender):
            warnings.warn("Sender is not subtype of CommunicationInterfaceSender")

    def close(self):
        print "Cleaning up PiController object"
        self.__communication_interface_listener.stop()
        self.__height_sensor.close()
        self.__camera_sensor.close()

if __name__ == '__main__':
    controller = PiController()
    controller.close()
