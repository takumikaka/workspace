# coding:UTF-8 -*-

import smtplib
from email.mime.text import MIMEText

msg = MIMEText("This is test text!", "plain", "utf-8")
msg["From"] = "发送邮箱"
msg["To"] = "接收邮箱"
msg["Subject"] = "API Test Report!"

smtp = smtplib.SMTP_SSL("smtp.163.com")
smtp.login("账号", "密码")
smtp.sendmail("发送邮箱", "接收邮箱", msg.as_string())
smtp.quit()
