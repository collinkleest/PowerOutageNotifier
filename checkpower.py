from lib import *


i=[13,19,26,16,20,21]
lib={
'13':' Power Lead 1',
'19':' Power Lead 2',
'26':' Power Lead 3', 
'16':' Generator Lead 1',
'20':' Generator Lead 2', 
'21':' Generator Lead 3'}


def sendMessage(pin):
  print("The Power is out on:", pin) 
  

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
     
if  __name__=="__main__":
    t1 = threading.Thread(target=checkPinOff, args=(i[0],))
    t2 = threading.Thread(target=checkPinOff, args=(i[1],))
    t3 = threading.Thread(target=checkPinOff, args=(i[2],))
    t4 = threading.Thread(target=checkPinOff, args=(i[3],))
    t5 = threading.Thread(target=checkPinOff, args=(i[4],))
    t6 = threading.Thread(target=checkPinOff, args=(i[5],))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    
