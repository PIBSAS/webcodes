#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

#Nomenclatura Broadcom
#GPIO.setmode(GPIO.BCM)
#Nomenclatura Board
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(8, GPIO.OUT)
#Broadcom = 14 por GPIO 14
#Board = 8 Pin 8
while True:
    GPIO.output(8, True)
    time.sleep (1)
    GPIO.output (8, False)
    time.sleep (1)
