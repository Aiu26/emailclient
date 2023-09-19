import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template
from dotenv import load_dotenv
import os
load_dotenv()

html= Template(Path('index.html').read_text())
email= EmailMessage()
email['from']=os.environ.get('EMAIL_FROM')
email['to']=os.environ.get('EMAIL_TO')
email['subject']='Google'
email.set_content(html.substitute({'name': 'Aiushi'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(os.environ.get('EMAIL_USERNAME'), os.environ.get('EMAIL_PASSWORD'))
    smtp.send_message(email)
    print('ALL GREATT') 



