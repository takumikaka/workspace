# coding:UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import sys
sys.path.append("..")
from config.config import *

def send_email():
    with open(report_file, "rb") as f:
        email_body = f.read()

    msg = MIMEMultipart()
    msg.attach(MIMEText(email_body, "html", "utf-8"))
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = Header(subject, "utf-8")

    att1 = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
    att1["Content-Type"] = "application/octet-stream"
    att1["Content-Disposition"] = "attachment; filename = {0}".format(report_file)
    msg.attach(att1)

    try:
        smtp = smtplib.SMTP_SSL(smtp_server)
        smtp.login(smtp_user, smtp_passwd)
        smtp.sendmail(sender, receiver, msg.as_string())
        logging.info("邮件发送成功!")
    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.close()
