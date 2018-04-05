from communicator.SerialCommunicationInterfaceListener import SerialCommunicationInterfaceListener
from communicator.CommunicationInterfaceObserver import CommunicationInterfaceObserver
from communicator.SerialCommunicationInterfaceSender import SerialCommunicationInterfaceSender
import time


class ArduinoSerialListener(CommunicationInterfaceObserver):
    def __init__(self):
        self.stored_message = ''

    def update(self, received_message):
        print str(self) + str(received_message)
        self.stored_message = received_message

    def get_stored_message(self):
        return self.stored_message


if __name__ == '__main__':
    time.sleep(2)
    serial_listener = SerialCommunicationInterfaceListener()
    serial_sender = SerialCommunicationInterfaceSender()
    arduino_listener = ArduinoSerialListener()
    serial_listener.attach(arduino_listener)
    serial_listener.start()
    not_stop = True
    index = 1
    while not_stop:
        string_message = "Test " + str(index)
        print "Sending " + string_message
        serial_sender.send_message(string_message)
        user_input = raw_input("Press Enter...")
        if user_input == "end":
            not_stop = False
        index += 1
    serial_listener.stop()