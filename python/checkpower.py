# Written by Rahul Emani & Collin Kleest
# Contact: collinkleest@gmail.com

#import library file 
from lib import *

# these lists can be extended if more GPIO ports are being utilized 
# simply add the GPIO number in the 'i' varibale and in the lib array add a message associate with your new number
i=[13]
lib={
'13':' Power Lead 1',
}
  
# Checks if the GPIO pin is not recieving voltage (5V or 3.3)
# A message will generate if the if statements evaluate false
# Prints message to python console along with syslog  
def checkPinOff(pin):
  while True:
    if GPIO.input(pin) == 0:
      time.sleep(15)
      if not GPIO.input(pin):
        initmessage = (str(datetime.datetime.now())+lib.get(str(pin))+' is out')
        logging.critical(initmessage)
        syslog.syslog(initmessage)
        os.system('sudo echo ' + initmessage + ' | sudo python3 alert.py' )
        checkPinOn(pin)

# Checks if the pin is recieveing volts (5V or 3.3V)
# A message will be sent if the first if statement evaluates True && the check pin off function for that specific pin evaultates false
# Prints message to python console along with syslog
def checkPinOn(pin):
  while True:
    if GPIO.input(pin):
      time.sleep(15)
      if GPIO.input(pin):
        initmessage = (str(datetime.datetime.now())+lib.get(str(pin))+' is back on again')
        logging.info(initmessage)
        syslog.syslog(initmessage)
        os.system('sudo echo ' + initmessage + ' | sudo python3 alert.py' )
        checkPinOff(pin)
     
# runs the program and threads for the GPIO pin function
# Threading is only implemented for multiple GPIO pins, in this example it isn't required
if  __name__=="__main__":
    t1 = threading.Thread(target=checkPinOff, args=(i[0],))
    t1.start()
    t1.join()
