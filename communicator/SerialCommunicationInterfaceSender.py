import serial
from communicator.CommunicationInterfaceSender import CommunicationInterfaceSender
from SingletonMetaclass import Singleton


class SerialCommunicationInterfaceSender(CommunicationInterfaceSender):
    """\
    Serial sending class, used to send messages to the MC of the ETs
    """
    __metaclass__ = Singleton

    def __init__(self):
        self.ser = serial.Serial(
            port='/dev/serial0',
            baudrate=9600,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1,
            dsrdtr=True
        )

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
