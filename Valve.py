import RPi.GPIO as GPIO

from Logger import logger


class Valve:

    def __init__(self, pin):
        self.pin = pin

        self.init_gpio()

    def init_gpio(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def get_valve_status(self):
        pass

    def set_valve_on(self):
        logger.info('valve switched on')
        pass

    def set_valve_off(self):
        logger.info('valve switched on')
        pass

