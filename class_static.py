# -*- coding:utf-8 -*-

# 静态方法可以被类直接调用,可以被所有的实例化对象共享,静态方法并没有和类的实例进行名称绑定,相当于全局函数

class Fruit:
    price = 0

    def __init__(self):
        self.__color = "red"

    def getColor(self):     # 类的方法,至少有一个参数self
        print self.__color

    @staticmethod
    def getPrice():
        print Fruit.price

    def __getPrice():
        Fruit.price += 10
        # print Fruit.price

    count = staticmethod(__getPrice)

if __name__ == '__main__':
    apple = Fruit()
    apple.getColor()
    Fruit.count()
    Fruit.getPrice()