from communicator.CommunicationInterfaceObserver import CommunicationInterfaceObserver

class ControllerSerialInterfaceObserver(CommunicationInterfaceObserver):
    def update(self, received_message):
        print received_message

    def __init__(self):
        pass
