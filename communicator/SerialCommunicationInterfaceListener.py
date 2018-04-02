from CommunicationInterfaceListener import CommunicationInterfaceListener
from CommunicationInterfaceObserver import CommunicationInterfaceObserver
from SingletonMetaclass import Singleton
import serial
import threading
import string

rot13 = string.maketrans(
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")

class SerialCommunicationInterfaceListener(threading.Thread, CommunicationInterfaceListener):
    """\
    Class which listens to the serial UART port of the raspberry pi and informs observers
    """
    __metaclass__ = Singleton

    def __init__(self):
        threading.Thread.__init__(self)
        self.ser = serial.Serial(
            port='/dev/serial0',
            baudrate=9600
        )
        self.observers = []
        self.listen_to_interface = True

    def attach(self, observer):
        if isinstance(observer, CommunicationInterfaceObserver):
            self.observers.append(observer)
        else:
            raise TypeError('Attribute observer is not a subclass of SerialObserver')

    def detach(self, observer):
        if isinstance(observer, CommunicationInterfaceObserver):
            self.observers.remove(observer)
        else:
            raise TypeError('Attribute observer is not a subclass of SerialObserver')

    def _notify(self, received_message):
        for observer in self.observers:
            observer.update(received_message)

    def _read_serial_interface(self):
        input_line = self.ser.read_until()
        serial_interface_string = string.translate(input_line, rot13)
        if serial_interface_string != '':
            self._notify(serial_interface_string)

    def run(self):
        while self.listen_to_interface:
            self._read_serial_interface()

    def stop(self):
        self.listen_to_interface = False
