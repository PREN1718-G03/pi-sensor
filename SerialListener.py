import serial
import SerialObserver

class SerialListener:
    """\
    Class which listens to the serial UART port of the raspberry pi and informs observers
    """

    def __int__(self):
        self.ser = serial.Serial('/dev/serial0')
        self.ser.parity = serial.PARITY_NONE
        self.ser.stopbits = serial.STOPBITS_ONE
        self.ser.bytesize = serial.EIGHTBITS
        self.ser.timeout = 1
        self.observers = []

    def attach(self, observer):
        if (isinstance(observer,SerialObserver)):
            self.observers.append(observer)
        else:
            raise TypeError('Attribute observer is not a subclass of SerialObserver')

    def detach(self, observer):
        if (isinstance(observer,SerialObserver)):
            self.observers.remove(observer)
        else:
            raise TypeError('Attribute observer is not a subclass of SerialObserver')

    def _notify(self, receivedMessage):
        for observer in self.observers:
            observer.update(receivedMessage)

    