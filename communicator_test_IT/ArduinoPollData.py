import warnings
from communicator.CommunicationInterfaceListener import CommunicationInterfaceListener
from communicator.CommunicationInterfaceObserver import CommunicationInterfaceObserver
from communicator.CommunicationInterfaceSender import CommunicationInterfaceSender
from communicator.CommunicatorFactory import CommunicatorFactory
from controller.HeightSensor import HeightSensor
from controller.DistanceToPillarSensor import DistanceToPillarSensor


class ArduinoPollData(CommunicationInterfaceObserver):

    def update(self, received_message):
        if received_message == "SendData":
            print "Received request for data from ET board"
            data_to_send = ''
            usb, lsb = self.__transform_to_char_ints(self.__distance)
            data_to_send = usb + lsb
            usb, lsb = self.__transform_to_char_ints(self.__height)
            data_to_send = data_to_send + usb + lsb
            if self.__target_recognised:
                usb, lsb = self.__transform_to_char_ints(self.__distance_to_target)
                data_to_send = data_to_send + usb + lsb
            else:
                data_to_send = data_to_send + chr(255) + chr(255)
            print data_to_send
            self.__communication_interface_sender.send_message(data_to_send)
        else:
            print str(self) + " " + received_message

    def __transform_to_char_ints(self, value):
        result_value = int(round(value))
        integer_as_bitstring = '{0:016b}'.format(result_value)
        upper_significant_byte_as_char = chr(int(integer_as_bitstring[:8], 2))
        lower_significant_byte_as_char = chr(int(integer_as_bitstring[8:], 2))
        return upper_significant_byte_as_char, lower_significant_byte_as_char

    def __init__(self):
        self.__target_recognised = True
        self.not_stopped = True
        self.__height = 0
        self.__distance = 0
        self.__distance_to_target = 10.0

        self.__communication_interface_listener = CommunicatorFactory.get_communication_interface_listener()
        self.__communication_interface_sender = CommunicatorFactory.get_communication_interface_sender()

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

    def control(self):
        self.__height = self.__height_sensor.get_height()
        self.__distance = self.__distance_sensor.get_distance()

    def close(self):
        print "Cleaning up PiController object"
        self.__communication_interface_listener.stop()
        self.__height_sensor.close()
        self.__distance_sensor.close()


if __name__ == '__main__':
    controller = ArduinoPollData()
    while controller.not_stopped:
        controller.control()
    controller.close()
