#! /usr/bin/python3
# -*- coding: utf-8 -*-
from logging.handlers import RotatingFileHandler

import RPi.GPIO as GPIO
import time
import logging
import threading

from FlowMeter import FlowMeter
from Logger import logger
from TemperatureSensor import TemperatureSensor
from Valve import Valve


GPIO_VALVE = 23


def flow_threading():
    while True:
        f1.get_flow_rate()
        time.sleep(1)
    

if __name__ == '__main__':
    
    logger.info('started...')

    v1 = Valve(pin=GPIO_VALVE)
     
# 
    t1 = TemperatureSensor(location='water', sensor_type='DS18B20', sensor_name='/sys/bus/w1/devices/28-01131a6b6e1c/w1_slave')
    temperature = t1.read_temp()['sensor_measurement']
    logger.info('{} measured temperature: {} °C'.format(t1.location, temperature))

    f1 = FlowMeter(pin=5, name='circulating')
    x = threading.Thread(target=flow_threading)
    x.start()

    while True:
        try:
            v1.set_valve_on()
            time.sleep(1)
            v1.set_valve_off()
            time.sleep(1)
        except KeyboardInterrupt:
            GPIO.cleanup()




