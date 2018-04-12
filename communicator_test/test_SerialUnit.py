from communicator.CommunicationInterfaceObserver import CommunicationInterfaceObserver
from communicator.ArduinoSerialCommunicationInterfaceListener import ArduinoSerialCommunicationInterfaceListener
import unittest


class TestSerialListener(unittest.TestCase):
    def setUp(self):
        self.listener = ArduinoSerialCommunicationInterfaceListener()
        self.observer = TestObserver()

    def testAttach(self):
        self.listener.attach(self.observer)
        test_result = False
        for observer in self.listener.observers:
            if observer == self.observer:
                test_result = True
        assert test_result

    def testAttachFalse(self):
        self.listener.attach(TestObserver())
        test_result = False
        for observer in self.listener.observers:
            if observer == self.observer:
                test_result = True
        if test_result:
            self.fail()

    def testDetach(self):
        self.listener.attach(self.observer)
        test_result = True
        self.listener.detach(self.observer)
        for observer in self.listener.observers:
            if observer == self.observer:
                test_result = False
        assert test_result

    def tearDown(self):
        pass


class TestObserver(CommunicationInterfaceObserver):
    def __init__(self):
        super(TestObserver, self).__init__()
        pass

    def update(self, received_message):
        print received_message


if __name__ == '__main__':
    unittest.main()
