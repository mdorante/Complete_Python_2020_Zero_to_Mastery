import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Manuel Dorante'
email['to'] = 'mdorante10@gmail.com'
email['subject'] = 'Trying this out'

email.set_content(html.substitute({'name': 'Manu'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('py.sender.md01@gmail.com', 'e%Rj4!RJ5#rXZa')
    smtp.send_message(email)
