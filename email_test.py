# -*- coding:utf-8 -*-

# 函数式编程之发送邮件
# def 定义函数的关键字
# 函数名,日后通过函数名调用该函数
# 函数声明,不自动执行; 调用后才执行
# 函数的参数
# 函数的返回值

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def email(arg,receiver,subject="主题"): # 形参
    msg = MIMEText(arg, 'plain', 'utf-8')

    msg['From'] = formataddr(["xiangxiaobao", 'wptawy@126.com'])
    msg['To'] = formataddr(["走人", '943300866@qq.com'])
    msg['Subject'] = subject

    server = smtplib.SMTP("smtp.126.com", 25)
    server.login("wptawy@126.com", "WW.3945.59")
    server.sendmail('wptawy@126.com', [receiver,], msg.as_string())
    server.quit()

if __name__ == '__main__':
    cpu = 100
    disk = 500
    ram = 50
    for i in range(1):
        if cpu > 90:
            alert = u'CPU出问题'
            ret = email(alert,"943300866@qq.com")  # 实参
            if ret == False:
                email(alert,"943300866@qq.com")
        if disk > 90:
            alert = u'硬盘出问题'
            email(alert,"943300866@qq.com")
        if ram > 80:
            alert = u'内存出问题'
            email(alert,"943300866@qq.com")