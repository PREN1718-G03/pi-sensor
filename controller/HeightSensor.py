import RPi.GPIO as GPIO
import time

from controller.UltraSonicSensor import UltraSonicSensor


class HeightSensor(UltraSonicSensor):
    def __init__(self):
        super(HeightSensor, self).__init__(23, 24)

    def get_height(self):
        measurement1 = self.measure()
        measurement2 = self.measure()
        measurement3 = self.measure()
        average = (measurement1 + measurement2 + measurement3) / 3
        return average

    def close(self):
        super(HeightSensor, self).close()
