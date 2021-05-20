#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import sys

from Logger import logger


class FlowMeter:
    flow = 0
    count = 0

    def __init__(self, pin, name):

        self.pin = pin
        self.name = name

        self.init_gpio()

    def init_gpio(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def count_pulse(self, channel):
        global count
        if start_counter:
            count = count+1
            flow = count / 6  # pulse frequency = 6*Q, Q is the flow rate in L/min
            logger("Flow {}: {} Liter/min".format(self.name, flow))
            time.sleep(1)
            count = 0


while True:
    try:
        start_counter = 1
        time.sleep(1)
        start_counter = 0
        count = 0
    except KeyboardInterrupt:
        print('\ncaught keyboard interrupt!, bye')
        GPIO.cleanup()
        sys.exit()
