from communicator.CommunicationInterfaceObserver import CommunicationInterfaceObserver
from communicator.CommunicatorFactory import CommunicatorFactory
from communicator.CommunicationInterfaceListener import CommunicationInterfaceListener
from communicator.CommunicationInterfaceSender import CommunicationInterfaceSender
from camera_sensor.CameraSensorFactory import CameraSensorFactory
from controller.DistanceToPillarSensor import DistanceToPillarSensor
from controller.HeightSensor import HeightSensor
import warnings


class PiController(CommunicationInterfaceObserver):
    # Implementation of SerialInterfaceObserver methods
    def update(self, received_message):
        if received_message == "SendData":
            pass

    def __init__(self):
        self.not_stopped = True
        self.__height = 0;
        self.__distance = 0;

        self.__communication_interface_listener = CommunicatorFactory.get_communication_interface_listener()
        self.__communication_interface_sender = CommunicatorFactory.get_communication_interface_sender()

        self.__camera_sensor_factory = CameraSensorFactory()
        self.__camera_sensor = CameraSensorFactory.get_sensor_controller()

        self.__height_sensor = HeightSensor()
        self.__distance_sensor = DistanceToPillarSensor()

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
        self.__distance_sensor.close()
        self.__camera_sensor.close()

    def control(self):
        self.__height = self.__height_sensor.get_height()
        self.__distance = self.__distance_sensor.get_distance()

        self.__camera_sensor.set_height(self.__height)
        target_recognized, distance = self.__camera_sensor.get_target_and_distance()

        if target_recognized:
            print "Target recognized in a distance of " + str(distance) + " cm"
        else:
            print "Target not recognized"


if __name__ == '__main__':
    controller = PiController()
    while controller.not_stopped:
        controller.control()
        # TODO remove raw input and provide graceful shutdown possibility
        user_input = raw_input("Press Enter...")
        if user_input == "end":
            controller.not_stopped = False
    controller.close()
