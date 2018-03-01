from SerialInterfaceObserver import SerialInterfaceObserver
from SingletonMetaclass import Singleton
import serial
import threading

class SerialInterfaceListener(threading.Thread):
    """\
    Class which listens to the serial UART port of the raspberry pi and informs observers
    """
    __metaclass__ = Singleton

    def __init__(self):
        threading.Thread.__init__(self)
        self.ser = serial.Serial('/dev/serial0')
        self.ser.parity = serial.PARITY_NONE
        self.ser.stopbits = serial.STOPBITS_ONE
        self.ser.bytesize = serial.EIGHTBITS
        self.ser.timeout = 1
        self.observers = []
        self.listen_to_interface = True

    def attach(self, observer):
        if isinstance(observer, SerialInterfaceObserver):
            self.observers.append(observer)
        else:
            raise TypeError('Attribute observer is not a subclass of SerialObserver')

    def detach(self, observer):
        if isinstance(observer, SerialInterfaceObserver):
            self.observers.remove(observer)
        else:
            raise TypeError('Attribute observer is not a subclass of SerialObserver')

    def _notify(self, received_message):
        for observer in self.observers:
            observer.update(received_message)

    def _read_serial_interface(self):
        serial_interface_string = str(self.ser.readline())
        # Split the line on the \n and get the first element (the message)
        serial_interface_string = serial_interface_string.split('\n')[0]
        if serial_interface_string != '':
            print serial_interface_string
            self._notify(serial_interface_string)

    def run(self):
        while self.listen_to_interface:
            self._read_serial_interface()

    def stop(self):
        self.listen_to_interface = False
