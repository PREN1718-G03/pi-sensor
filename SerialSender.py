import serial
import logging

class SerialSender:
    """\
    Serial sending class, used to send messages to the MC of the ETs
    """

    def __int__(self):
        self.ser = serial.Serial('/dev/serial0')
        self.ser.parity = serial.PARITY_NONE
        self.ser.stopbits = serial.STOPBITS_ONE
        self.ser.bytesize = serial.EIGHTBITS
        self.ser.timeout = 1
        self.logger = logging.getLogger(__name__)

    def _writeString(self, messageString):
        if (isinstance(messageString, str)):
            self.ser.write(messageString)
        else:
            raise TypeError('Variable messageString is not of type String')

    def sendMessage(self, message):
        try:
            self._writeString(str(message))
        except TypeError as error:
            self.logger.error(error)
            raise