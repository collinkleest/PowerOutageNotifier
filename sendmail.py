#imports
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def getPhones():
    with open('phones.csv') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        for row in csvReader:
            phone = row[0]
            carrier = row[1]
            name = row[2]
            sendEmail(phone, carrier)
            

def getCarrierAddr(carrier):
    carriers = {
        'verizon':'vtext.com',
        'att':'txt.att.net',
        'metro':'mymetropcs.com',
        'sprint':'messaging.sprintpcs.com',
        'virgin':'vmobl.com',
        'tmobile':'tmomail.net',
        'boost':'myboostmobile.com'
    }
    return carriers.get(carrier.lower())


def sendEmail(phone, carrier):
    s = smtplib.SMTP(host=mailServer, port=587)
    s.starttls()
    s.login(loginEmail, loginPW) 
    email = (str(phone)+'@')+(getCarrierAddr(carrier))
    message = "Malvern Office Power is Out"
    msg = MIMEMultipart()
    msg['From']='rajant-alerts@rajant.com'
    print(str(email))
    msg['To']=str(email)
    msg['Subject']="Power Outage"
    msg.attach(MIMEText(message, 'plain'))
    s.send_message(msg)


if __name__=="__main__":
    mailServer = "smtp.gmail.com"
    loginEmail = "collinkleest@gmail.com"
    loginPW = "0809N@n@ruth"
    getPhones()
