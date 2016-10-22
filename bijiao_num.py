# -*- coding:utf-8 -*-

# 冒泡排序  时间排序
li = [13, 22, 6, 99, 11]
print li

for n in range(1,len(li)-1):
    for m in range(len(li)-n):
        num1 = li[m]
        num2 = li[m+1]
        if num1 > num2:
            temp = li[m]
            li[m] = num2
            li[m+1] = temp
print li