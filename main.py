#! /usr/bin/python3
# -*- coding: utf-8 -*-
from logging.handlers import RotatingFileHandler

import RPi.GPIO as GPIO
import time
import logging

from Logger import logger
from TemperatureSensor import TemperatureSensor
from Valve import Valve


GPIO_VALVE = 2


if __name__ == '__main__':

    TS = TemperatureSensor(sensor_type='DS18B20', sensor_name='/sys/bus/w1/devices/28-01131a6b6e1c/w1_slave')
    temperature = TS.read_temp()
    logger.info('Temperature: {0}'.format(temperature))

    try:
        v1 = Valve(pin=GPIO_VALVE)
        v1.set_valve_on()
        time.sleep(1)
        v1.set_valve_off()
        time.sleep(1)
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()




