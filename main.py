#! /usr/bin/python3
# -*- coding: utf-8 -*-
from logging.handlers import RotatingFileHandler

import RPi.GPIO as GPIO
import time
import logging
from TemperatureSensor import TemperatureSensor

log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logFile = 'fountain.log'
my_handler = RotatingFileHandler(logFile, mode='a', maxBytes=50*1024*1024,
                                 backupCount=2, encoding=None, delay=0)
my_handler.setFormatter(log_formatter)
my_handler.setLevel(logging.INFO)

logger = logging.getLogger('Fountain Logger')
logger.setLevel(logging.INFO)
logger.addHandler(my_handler)

GPIO_VALVE = 2

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_VALVE, GPIO.OUT)


def valve_on(pin):
    GPIO.output(pin, GPIO.HIGH)  # Turn motor on
    logger.info('valve switched on')


def valve_off(pin):
    GPIO.output(pin, GPIO.LOW)  # Turn motor off
    logger.info('valve switched off')


if __name__ == '__main__':

    TS = TemperatureSensor(sensor_type='DS18B20', sensor_name='/sys/bus/w1/devices/28-01131a6b6e1c/w1_slave')
    temperature = TS.read_temp()
    logger.info('Temperature: {0}'.format(temperature))

    try:
        valve_on(GPIO_VALVE)
        time.sleep(1)
        valve_off(GPIO_VALVE)
        time.sleep(1)
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()




