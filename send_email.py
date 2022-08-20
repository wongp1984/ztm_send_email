import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

from_email_acc = 'ssk_8003@hotmail.com'
from_email_pwd = 'password167'

email = EmailMessage()
email['from'] = from_email_acc
email['to'] = 'wongp.1984@gmail.com'
email['subject'] = 'Hello Peter'

email.set_content(html.substitute({'name': 'LamLam'}), 'html')

with smtplib.SMTP(host='smtp-mail.outlook.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('ssk_8003@hotmail.com', from_email_pwd)
    smtp.send_message(email)
    print('Email sent...')