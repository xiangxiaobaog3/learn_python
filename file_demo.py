# -*- coding:utf-8 -*-

# obj = file('') 从3.0废弃了

obj = open('email_test.py', 'r+U')
obj.seek(5)
obj.write("dfasdf\r\n")
print obj.tell()
obj.read()
print obj.tell()
obj.truncate() #截断数据,根据当前指针的位置
obj.close()