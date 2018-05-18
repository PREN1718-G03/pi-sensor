import datetime
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
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
            self.__file.write("Received request for data from ET board")
            data_to_send = ''
            usb, lsb = self.__transform_to_char_ints(self.__distance * 10)
            data_to_send = usb + lsb
            usb, lsb = self.__transform_to_char_ints(self.__height * 10)
            data_to_send = data_to_send + usb + lsb
            if self.__target_recognised:
                # Add 18 cm, as the camera is in front
                distance_to_send = self.__distance_to_target + 18.0
                usb, lsb = self.__transform_to_char_ints(distance_to_send * 10)
                data_to_send = data_to_send + usb + lsb
            else:
                data_to_send = data_to_send + chr(255) + chr(255)
                self.__file.write(data_to_send)
            self.__communication_interface_sender.send_message(data_to_send)

    def __transform_to_char_ints(self, value):
        result_value = int(round(value))
        integer_as_bitstring = '{0:016b}'.format(result_value)
        upper_significant_byte_as_char = chr(int(integer_as_bitstring[:8], 2))
        lower_significant_byte_as_char = chr(int(integer_as_bitstring[8:], 2))
        return upper_significant_byte_as_char, lower_significant_byte_as_char

    def print_debug_information(self):
        self.__file.write("Height: " + str(self.__height) + "; Distance: " + str(self.__distance) + "; Target: " + str(
            self.__distance_to_target))

    def __init__(self):
        super(PiController, self).__init__()
        self.not_stopped = True
        self.__height = 0.0
        self.__distance = 0.0
        self.__target_recognised = False
        self.__distance_to_target = 0.0

        file = '/home/pi/logs/us_log' + str(datetime.datetime.now()) + '.log'
        with open(file, 'w') as logfile:
            logfile.write(str(datetime.datetime.now()) + '\n')
        self.__file = open(file, 'a')

        self.__communication_interface_listener = CommunicatorFactory.get_communication_interface_listener()
        self.__communication_interface_sender = CommunicatorFactory.get_communication_interface_sender()

        self.__camera_sensor_factory = CameraSensorFactory()
        self.__camera_sensor = CameraSensorFactory.get_sensor_controller()

        self.__height_sensor = HeightSensor()
        self.__distance_sensor = DistanceToPillarSensor()

        if isinstance(self.__communication_interface_listener, CommunicationInterfaceListener):
            self.__file.write("Setting up listener")
            self.__communication_interface_listener.start()
            self.__communication_interface_listener.attach(self)
        else:
            self.__file.write("Listener not started!")
            warnings.warn("Listener not started", RuntimeWarning)

        if not isinstance(self.__communication_interface_sender, CommunicationInterfaceSender):
            self.__file.write("Sender is not subtype of CommunicationInterfaceSender")
            warnings.warn("Sender is not subtype of CommunicationInterfaceSender")

    def close(self):
        self.__file.write("Cleaning up PiController object")
        self.__file.close()
        self.__communication_interface_listener.stop()
        self.__height_sensor.close()
        self.__distance_sensor.close()
        self.__camera_sensor.close()

    def control(self):
        measured_height = self.__height_sensor.get_height()
        if 0 < measured_height < 500:
            self.__height = measured_height

        measured_distance = self.__distance_sensor.get_distance()
        if 0 < measured_distance < 500:
            self.__distance = measured_distance

        self.__camera_sensor.set_height(self.__height)
        self.__target_recognised, distance = self.__camera_sensor.get_target_and_distance()


def main_loop():
    controller = PiController()
    not_stopped = True
    try:
        while not_stopped:
            controller.control()
            controller.print_debug_information()
    except (KeyboardInterrupt, SystemExit):
        controller.close()
        raise


if __name__ == '__main__':
    main_loop()
