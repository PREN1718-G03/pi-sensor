import abc
import time

from RPi import GPIO


class UltraSonicSensor(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, gpio_trigger, gpio_echo):
        # define GPIO pins
        self.__GPIO_TRIGGER = gpio_trigger
        self.__GPIO_ECHO = gpio_echo
        self.__setup__()

    def __setup__(self):
        # GPIO Mode (BOARD / BCM)
        GPIO.setmode(GPIO.BCM)

        # define direction of GPIO pins(IN / OUT)
        GPIO.setup(self.__GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.__GPIO_ECHO, GPIO.IN)

        # TODO Solve RuntimeWarning: This Channel already in use
        GPIO.setwarnings(False)

    def measure(self):
        GPIO.output(self.__GPIO_TRIGGER, True)

        # set trigger to LOW after 0.00001 seconds
        time.sleep(0.00001)
        GPIO.output(self.__GPIO_TRIGGER, False)

        time_start = 0.0
        time_stop = 0.0
        time_start_measurement = time.time()
        measurement_stopped = False
        while GPIO.input(self.__GPIO_ECHO) == 0 and not measurement_stopped:
            time_start = time.time()
            time_delta = time_start - time_start_measurement
            if time_delta < 2:
                measurement_stopped = True

        time_stop_measurement = time.time()
        while GPIO.input(self.__GPIO_ECHO) == 1 and not measurement_stopped:
            time_stop = time.time()
            time_delta = time_stop - time_stop_measurement
            if time_delta < 2:
                measurement_stopped = True

        time_elapsed = time_stop - time_start
        distance = (time_elapsed * 34300) / 2

        if measurement_stopped:
            distance = None
        else:
            time.sleep(0.005)
        return distance

    def close(self):
        GPIO.cleanup()
