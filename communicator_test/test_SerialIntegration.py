from communicator.CommunicationInterfaceObserver import CommunicationInterfaceObserver
from communicator.SerialCommunicationInterfaceListener import SerialCommunicationInterfaceListener
from communicator.SerialInterfaceSender import SerialInterfaceSender
import unittest
import time


class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.observer1 = TestObserver()
        self.observer2 = TestObserver()
        self.observer3 = TestObserver()

        self.sender = SerialInterfaceSender()

        self.listener = SerialCommunicationInterfaceListener()
        self.listener.attach(self.observer1)
        self.listener.attach(self.observer2)
        self.listener.attach(self.observer3)

        self.listener.start()

    def testSend(self):
        test_message = 'This is a Test123'
        test_result = False
        self.sender.send_message(test_message)
        time.sleep(2)
        if test_message == self.observer1.get_stored_message() and test_message == self.observer2.get_stored_message()\
                and test_message == self.observer3.get_stored_message():
            test_result = True
        assert test_result

    def tearDown(self):
        self.listener.stop()


class TestObserver(CommunicationInterfaceObserver):

    def __init__(self):
        super(TestObserver, self).__init__()
        self.stored_message = ''

    def update(self, received_message):
        print str(self) + str(received_message)
        self.stored_message = received_message

    def get_stored_message(self):
        return self.stored_message


if __name__ == '__main__':
    unittest.main()
