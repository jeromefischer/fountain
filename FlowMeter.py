#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import sys

FLOW_SENSOR = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP)


class FlowMeter:
    flow = 0
    count = 0

    def __init__(self):
        pass

    def countPulse(channel):
       global count
       if start_counter:
           count = count+1
           flow = count / 6  # pulse frequency = 6*Q, Q is the flow rate in L/min
           print("\nFlow: %.2f Liter/min" %(flow))

    GPIO.add_event_detect(FLOW_SENSOR, GPIO.FALLING, callback=countPulse)


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
