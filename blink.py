#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

#GPIO.setmode(GPIO.BCM) Usado para la nomenclatura Broadcom
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(8, GPIO.OUT) #Board Pin 8 fisico como arduino, BCM sería 14 por GPIO14

while True:
    GPIO.output(8, True)
    time.sleep (1)
    GPIO.output (8, False)
    time.sleep (1)
