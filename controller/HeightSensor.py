import RPi.GPIO as GPIO
import time


class HeightSensor(object):
    def __init__(self):
        # GPIO Mode (BOARD / BCM)
        GPIO.setmode(GPIO.BCM)

        # define GPIO pins
        self.__GPIO_TRIGGER = 23
        self.__GPIO_ECHO = 24

        GPIO.cleanup()
        # define direction of GPIO pins(IN / OUT)
        GPIO.setup(self.__GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.__GPIO_ECHO, GPIO.IN)

    def get_height(self):
        height = 0.0
        return height
