# -*- coding:utf-8 -*-

# 函数式编程之发送邮件

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def email(arg):
    msg = MIMEText(arg, 'plain', 'utf-8')

    msg['From'] = formataddr(["xiangxiaobao", 'wptawy@126.com'])
    msg['To'] = formataddr(["走人", '943300866@qq.com'])
    msg['Subject'] = "主题"

    server = smtplib.SMTP("smtp.126.com", 25)
    server.login("wptawy@126.com", "WW.3945.59")
    server.sendmail('wptawy@126.com', ['943300866@qq.com',], msg.as_string())
    server.quit()

if __name__ == '__main__':
    cpu = 100
    disk = 500
    ram = 50
    for i in range(1):
        if cpu > 90:
            alert = u'CPU出问题'
            email(alert)
        if disk > 90:
            alert = u'硬盘出问题'
            email(alert)
        if ram > 80:
            alert = u'内存出问题'
            email(alert)