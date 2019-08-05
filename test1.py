from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

s = SMTP(host="dev1.rajant.com", port=25)

#email = "6103897220@vtext.com"
message = 'rajant power outage'
msg = MIMEMultipart()
msg['From']='rajant-alerts@rajant.com'
msg['To']= '6103897220@vtext.com'
msg['Subject']="Power Outage"
msg.attach(MIMEText(message, 'plain'))

s.send_message(msg)
