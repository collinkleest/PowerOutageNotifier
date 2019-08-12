import os
import sys
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
i=0

while True:
    if not GPIO.input(21):
        i+=1
    if not GPIO.input(20):
        i+=1
    if not GPIO.input(16):
        i+=1
    if i == 3:
        time.sleep(20)
        poweroutage=True
        if GPIO.input(21):
            poweroutage=False
        elif GPIO.input(20):
            poweroutage=False
        elif GPIO.input(16):
            poweroutage=False
        if poweroutage:
            print('Power Outage!')
            os.system('sudo echo Rajant power is out | sudo python3 /home/pi/github_text/PowerOutageNotifier/rajant-alert.py')
            sys.exit()
    i=0
    time.sleep(0.1)
GPIO.cleanup()



