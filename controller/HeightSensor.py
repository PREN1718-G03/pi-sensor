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
        GPIO.output(self.__GPIO_TRIGGER, True)

        # set trigger to LOW after 0.00001 seconds
        time.sleep(0.00001)
        GPIO.output(self.__GPIO_TRIGGER, False)

        time_start = time.time()
        time_stop = time.time()

        while GPIO.input(self.__GPIO_ECHO) == 0:
            time_start = time.time()

        while GPIO.input(self.__GPIO_ECHO) == 1:
            time_stop = time.time()

        time_elapsed = time_stop - time_start
        height = (time_elapsed * 34300) / 2
        return height
