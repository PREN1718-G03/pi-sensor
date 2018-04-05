from CommunicationInterfaceListener import CommunicationInterfaceListener
from CommunicationInterfaceObserver import CommunicationInterfaceObserver
from SingletonMetaclass import Singleton
import serial
import threading


class SerialCommunicationInterfaceListener(threading.Thread, CommunicationInterfaceListener):
    """\
    Class which listens to the serial UART port of the raspberry pi and informs observers
    """
    __metaclass__ = Singleton

    def __init__(self):
        threading.Thread.__init__(self)
        self.ser = serial.Serial(
            port='/dev/serial0',
            baudrate=9600,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1,
            dsrdtr=True
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
        if self.ser.inWaiting() is not 0:
            serial_interface_string = ''
            serial_interface_buffer = []
            character = ''

            while character != '\n':
                byte_character = self.ser.read()
                if len(byte_character) > 0:
                    if isinstance(byte_character, bytes):
                        if 0 < ord(byte_character) < 128:
                            character = byte_character.decode()
                            serial_interface_buffer.append(character)

            if len(serial_interface_buffer) != 0:
                serial_interface_string = ''.join(serial_interface_buffer)
                serial_interface_string = serial_interface_string.strip('\r\n')

            if serial_interface_string != '':
                self._notify(serial_interface_string)

    def run(self):
        while self.listen_to_interface:
            self.ser.timeout = 1
            self._read_serial_interface()

    def stop(self):
        self.listen_to_interface = False
        self.ser.close()
