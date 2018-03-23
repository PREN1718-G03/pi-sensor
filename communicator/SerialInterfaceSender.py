import serial
from communicator.CommunicationInterfaceSender import CommunicationInterfaceSender
from SingletonMetaclass import Singleton


class SerialInterfaceSender(CommunicationInterfaceSender):
    """\
    Serial sending class, used to send messages to the MC of the ETs
    """
    __metaclass__ = Singleton

    def __init__(self):
        self.ser = serial.Serial('/dev/serial0')
        self.ser.parity = serial.PARITY_NONE
        self.ser.stopbits = serial.STOPBITS_ONE
        self.ser.bytesize = serial.EIGHTBITS
        self.ser.timeout = 1

    def _write_string(self, message_string):
        if isinstance(message_string, str):
            self.ser.write(message_string)
        else:
            raise TypeError('Variable messageString is not of type String')

    def send_message(self, message):
        try:
            self._write_string(str(message))
        except TypeError as error:
            self.logger.error(error)
            raise
