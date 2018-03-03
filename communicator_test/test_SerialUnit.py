from communicator.SerialInterfaceObserver import SerialInterfaceObserver
from communicator.SerialInterfaceListener import SerialInterfaceListener
import unittest


class TestSerialListener(unittest.TestCase):
    def setUp(self):
        self.listener = SerialInterfaceListener()
        self.observer = TestObserver()

    def testAttach(self):
        self.listener.attach(self.observer)
        test_result = False
        for observer in self.listener.observers:
            if observer == self.observer:
                test_result = True
        assert test_result

    @unittest.expectedFailure
    def testAttachFalse(self):
        self.listener.attach(TestObserver())
        test_result = False
        for observer in self.listener.observers:
            if observer == self.observer:
                test_result = True
        assert test_result

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


class TestObserver(SerialInterfaceObserver):
    def __init__(self):
        super(TestObserver, self).__init__()
        pass

    def update(self, received_message):
        print received_message


if __name__ == '__main__':
    unittest.main()
