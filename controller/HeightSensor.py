import RPi.GPIO as GPIO
import time

from controller.UltraSonicSensor import UltraSonicSensor


class HeightSensor(UltraSonicSensor):
    def __init__(self):
        super(HeightSensor, self).__init__(23, 24)

    def measure(self):
        return super(HeightSensor, self).measure()

    def get_height(self):
        measurement1 = self.measure()
        measurement2 = self.measure()
        measurement3 = self.measure()
        if measurement1 is None or measurement2 is None or measurement3 is None:
            average = None
        else:
            average = (measurement1 + measurement2 + measurement3) / 3
        return average

    def close(self):
        super(HeightSensor, self).close()
