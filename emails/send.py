from email.message import EmailMessage
from app import password
import ssl
import smtplib


email_sender = "khamcynthia@gmail.com"
email_password = password

email_receiver ='yonodi2742@crtsec.com'
subject = 'dont forget to attend the meeting'
body= """
watch the video and dont forget to attend the meeting
"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP('smtp.gmail.com', 465) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())



