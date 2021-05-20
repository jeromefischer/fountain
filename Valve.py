import RPi.GPIO as GPIO

from Logger import logger


class Valve:

    def __init__(self, pin, name='Valve'):
        self.pin = pin
        self.name = name

        self.init_gpio()

    def init_gpio(self):
        logger.info('initialize: {} pin: {}'.format(self.name, self.pin))

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def get_valve_status(self):
        pass

    def set_valve_on(self):
        GPIO.output(self.pin, GPIO.HIGH)  # Turn valve on
        logger.info('valve switched on')
        pass

    def set_valve_off(self):
        GPIO.output(self.pin, GPIO.LOW)  # Turn valve off
        logger.info('valve switched off')
        pass

