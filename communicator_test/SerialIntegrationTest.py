from communicator.SerialObserver import SerialObserver
from communicator.SerialListener import SerialListener
from communicator.SerialSender import SerialSender
import unittest


class TestSerialListener(unittest.TestCase):
    def setUp(self):
        self.listener = SerialListener()
        self.observer = TestObserver()

    def tearDown(self):
        pass


class TestObserver(SerialObserver):
    def __init__(self):
        super(TestObserver, self).__init__()
        pass

    def update(self, received_message):
        print received_message


if __name__ == '__main__':
    unittest.main()
