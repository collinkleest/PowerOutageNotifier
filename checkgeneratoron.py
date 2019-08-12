import os
import sys
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
i=0

while True:
    if not GPIO.input(26):
        i+=1
    if not GPIO.input(13):
        i+=1
    if not GPIO.input(19):
        i+=1
    if i == 3:
        time.sleep(20)
        GeneratorOn=False
        if GPIO.input(26) and GPIO.input(19) and GPIO.input(13):
            GeneratorOn=True
        if GeneratorOn:
            os.system('sudo echo Rajant generator is active | sudo python3 /home/pi/github_text/PowerOutageNotifier/rajant-alert.py')
            sys.exit()
    i=0
    time.sleep(0.1)
GPIO.cleanup()



