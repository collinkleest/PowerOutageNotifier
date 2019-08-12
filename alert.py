# imports
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Reads and opens csv file with contacts and calls the sendEmail function
def getPhones():
    with open('/home/pi/github_text/PowerOutageNotifier/phones.csv') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        for row in csvReader:
            phone = row[0]
            carrier = row[1]
            name = row[2]
            sendEmail(phone, carrier, name)

#Gets specific carrier input from csv file and outputs the sms gateway for that carrier
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

#calls email  class with the inputs phone, carrier, and name
#gets the 's' variable from the main function
def sendEmail(phone, carrier, name):
    msg = Email(phone, carrier, name)
    s.send_message(msg.constructEmail())


class Email:
    # constucts email object
    def __init__(self, phone, carrier, name):
        self.phone = phone
        self.carrier = carrier
        self.name = name
    
    # builds the email
    def constructEmail(self):
        email = (str(self.phone) + '@') + (getCarrierAddr(self.carrier))
        finalmessage = (self.name+': \n'+message)
        msg = MIMEMultipart()
        msg['From'] = 'rajant-alerts@rajant.com'
        msg['To'] = str(email)
        msg.attach(MIMEText(str(finalmessage), 'plain'))
        return msg

#main function
if __name__=="__main__":
    mailServer = "localhost"
    message = input()
    s = smtplib.SMTP(host=mailServer, port=1025)
    getPhones()