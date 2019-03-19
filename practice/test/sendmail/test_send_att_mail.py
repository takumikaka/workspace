# coding:UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

with open("report.html", "rb") as f:
    email_body = f.read()

msg = MIMEMultipart()
msg.attach(MIMEText(email_body, "html", "utf-8"))

msg["From"] = "发送邮箱"
msg["To"] = "接收邮箱"
msg["Subject"] = Header("接口测试报告", "utf-8")

att1 = MIMEText(open("report.html", "rb").read(), "base64", "utf-8")
att1["Content-Type"] = "application/octet-stream"
att1["Content-Dispoistion"] = "attachment; filename = 'report.html'"
msg.attach(att1)

smtp = smtplib.SMTP_SSL("smtp.163.com")
smtp.login("账号", "密码")
smtp.sendmail("发送邮箱", "接收邮箱", msg.as_string())
smtp.quit()
