import datetime
import time


class LogFileWriter(object):
    def __init__(self):
        file = '/home/pi/logs/PiController' + str(datetime.date.today()) + '-' + str(time.time()) + '.log'
        with open(file, 'w') as logfile:
            logfile.write(str(datetime.datetime.now()) + '\n')
        self.__file = open(file, 'a')

    def info(self, message):
        if message is not str:
            message = str(message)
        message = 'INFO: ' + message
        self.__write(message)

    def warn(self, message):
        if message is not str:
            message = str(message)
        message = 'WARNING: ' + message
        self.__write(message)

    def __write(self, message):
        message = str(time.time()) + ' - ' + message
        self.__file.write(message + '\n')

    def close(self):
        self.__file.close()
