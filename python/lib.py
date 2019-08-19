#imports for scripts 
import os
import sys
import RPi.GPIO as GPIO
import time
import threading
import logging
import syslog 
import datetime

# GPIO mode set to BCM, value can also be BOARD
# i2 array can have mutiple GPIO pins
GPIO.setmode(GPIO.BCM)
i2=[13]

#setting up GPIO pins
for x in i2: GPIO.setup(x, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)