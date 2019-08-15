#imports
import os
import sys
import RPi.GPIO as GPIO
import time
import threading
import logging
import syslog 
import datetime

GPIO.setmode(GPIO.BCM)
i2=[13,19,26,16,20,21]

for x in i2:
        GPIO.setup(x, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#icp=[13,19,26,16,20,21]
#lib=['power lead 1', 'power lead 2', 'power lead 3', 'generator lead 1', 'generator lead 2', 'generator lead 3']

