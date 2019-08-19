# Written by Collin Kleest & Rahul Emani
# Contact: collinkleest@gmail.com
# imports
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# gets phone numbers from csv file
def getPhones():
    with open(str(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))+"/phones.csv") as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        for row in csvReader:
            phone = row[0]
            carrier = row[1]
            name = row[2]
            # even if connection fails, program will continue to run
            try:
                sendEmail(phone, carrier, name)
            except:
                pass

# carrier input to SMS gateway output
def getCarrierAddr(carrier):
    carriers = {
        'verizon': 'vtext.com',
        'att': 'txt.att.net',
        'metro': 'mymetropcs.com',
        'sprint': 'messaging.sprintpcs.com',
        'virgin': 'vmobl.com',
        'tmobile': 'tmomail.net',
        'boost': 'myboostmobile.com',
        'cricket': 'mms.cricketwireless.net',
        'google': 'msg.fi.google.com',
        'uscell': 'email.uscc.net'
    }
    return carriers.get(carrier.lower())

# sends email
def sendEmail(phone, carrier, name):
    msg = Email(phone, carrier, name)
    s.send_message(msg.constructEmail())

class Email:
    # contructor
    def __init__(self, phone, carrier, name):
        self.phone = phone
        self.carrier = carrier
        self.name = name
    
    # contructs the msg itself
    def constructEmail(self):
        email = (str(self.phone) + '@') + (getCarrierAddr(self.carrier))
        finalmessage = (self.name+': \n'+message)
        msg = MIMEMultipart()
        msg['From'] = 'Rajant Alert'
        msg['To'] = str(email)
        msg.attach(MIMEText(str(finalmessage), 'plain'))
        return msg

if __name__=="__main__":
    mailServer = "HOSTNAME OF SERVER / IP ADDR"
    # where the message is written
    message = input()
    s = smtplib.SMTP(host=mailServer, port=25)
    getPhones()
