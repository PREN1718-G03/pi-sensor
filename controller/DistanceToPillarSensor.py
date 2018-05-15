import RPi.GPIO as GPIO
import time


class DistanceToPillarSensor(object):
    def __init__(self):
        # GPIO Mode (BOARD / BCM)
        GPIO.setmode(GPIO.BCM)

        # define GPIO pins
        self.__GPIO_TRIGGER = 5
        self.__GPIO_ECHO = 6

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
        time_delta = 0.0
        while GPIO.input(self.__GPIO_ECHO) == 0 and time_delta < 2:
            time_start = time.time()
            time_delta = time_start - time_start_measurement

        time_stop_measurement = time.time()
        time_delta = 0.0
        while GPIO.input(self.__GPIO_ECHO) == 1 and time_delta < 2:
            time_stop = time.time()
            time_delta = time_stop - time_stop_measurement

        time_elapsed = time_stop - time_start
        distance = (time_elapsed * 34300) / 2

        time.sleep(0.005)
        return distance

    def get_distance(self):
        measurement1 = self.measure()
        measurement2 = self.measure()
        measurement3 = self.measure()
        average = (measurement1 + measurement2 + measurement3) / 3
        return average

    def close(self):
        GPIO.cleanup()
