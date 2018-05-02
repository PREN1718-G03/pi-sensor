import serial
from communicator.CommunicationInterfaceSender import CommunicationInterfaceSender
from SingletonMetaclass import Singleton


class ArduinoSerialCommunicationInterfaceSender(CommunicationInterfaceSender):
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
            timeout=1
        )

    def __write_string(self, message_string):
        if isinstance(message_string, str):
            message = message_string.strip('\r\n') + '\r\n'
            buffer = self.__convert_to_arduino_buffer(message)
            if len(buffer)>0:
                for byte in buffer:
                    self.ser.write(byte)
        else:
            raise TypeError('Variable messageString is not of type String')

    def send_message(self, message):
        try:
            self.__write_string(str(message))
        except TypeError as error:
            self.logger.error(error)
            raise

    def __convert_to_arduino_buffer(self, message_string):
        send_buffer = []
        for character in message_string:
            send_buffer.append(character)
        return send_buffer
