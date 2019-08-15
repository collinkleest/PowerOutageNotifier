import os
import sys
import RPi.GPIO as GPIO
import time
import datetime
import logging

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def CheckWater():
  while True:
    if GPIO.input(17):
      dt = datetime.datetime.now()
      command = ('sudo echo '+str(dt)+' DANGER, Water Detected!! | sudo python3 alert.py')
      os.system(command)
      logging.critical("%s DANGER, Water Detected!!", dt)
      reset()
  time.sleep(5)

def reset():
  while True:
    if not GPIO.input(17):
      time.sleep(10)
      if not GPIO.input(17):
        CheckWater()

if  __name__=="__main__":
  CheckWater()

