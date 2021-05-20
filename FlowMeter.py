#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import sys

from Logger import logger

flow = 0
count = 0


class FlowMeter:

    def __init__(self, pin, name):
        self.pin = pin
        self.name = name

        self.init_gpio()

    def init_gpio(self):
        logger.info('initialize: {} pin: {}'.format(self.name, self.pin))
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def count_pulse(self, channel):
        global count
        count = count + 1

    def get_flow_rate(self):
        global count
        print(count)
        flow = count / 6  # pulse frequency = 6*Q, Q is the flow rate in L/min
        logger.info("Flow {}: {} Liter/min".format(self.name, flow))
        count = 0


