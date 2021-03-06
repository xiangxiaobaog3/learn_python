# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def email(arg, receiver, subject="主题"):
    msg = MIMEText('邮件内容', 'plain', 'utf-8')
    msg['From'] = formataddr(["相谦", 'xiangqian@beescm.cn'])
    msg['To'] = formataddr(["走人",'943300866@qq.com'])
    msg['Subject'] = subject

    server = smtplib.SMTP("smtp.exmail.qq.com", 25)
    server.login("xiangqian@beescm.cn", "Xiu99ying@")
    server.sendmail('xiangqian@beescm.cn', [receiver,], msg.as_string())
    server.quit()

if __name__ == '__main__':
    cpu = 100
    disk = 500
    ram = 50
    for i in range(1):
        if cpu > 90:
            alert = u"CPU出问题了"
            li = ["943300866@qq.com", "xiangxiaobaog3@163.com"]
            for item in li:
                email(alert, item, '主题1')
        if disk > 90:
            alert = u"硬盘出问题了"
            li = ["943300866@qq.com", "xiangxiaobaog3@163.com"]
            for item in li:
                email(alert, item)
        if ram > 80:
            alert = "内存出问题了"
            li = ["943300866@qq.com", "xiangxiaobaog3@163.com"]
            for item in li:
                email(alert, item)
