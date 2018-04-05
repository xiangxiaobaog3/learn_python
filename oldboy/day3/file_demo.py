# -*- coding:utf-8 -*-


obj = open('log1', 'r+')
print obj.tell()
print obj.read()
print obj.tell()
obj.write("555")
print obj.readlines()
#obj.truncate() #截断数据,根据当前指针的位置
obj.close()

