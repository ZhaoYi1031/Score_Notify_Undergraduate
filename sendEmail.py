#-*- coding：utf-8 -*-
import smtplib
from email.mime.text import MIMEText

def send_email(user, pwd, recipient, subject, body):
    gmail_user = user#"zhaoyi1031@gmail.com"
    gmail_pwd = pwd#"zy12345678"
    FROM = user#"zhaoyi1031@gmail.com"
    TO = recipient if type(recipient) is list else [recipient]#["291045048@qq.com"]
    SUBJECT = subject#"Hi~I'm ohazyi"
    TEXT = body#"I love u, ma sichun"
    # Prepare actual message
    #message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    #""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
    msg = MIMEText(body, _subtype = 'plain', _charset = 'utf-8')
    msg['Subject'] = SUBJECT
    msg['From'] = FROM
    msg['To'] = ";".join(TO)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, msg.as_string())#message
        server.close()
        print("successfully sent the mail")
    except Exception as e:
        print("failed to send mail,%s"%e)


