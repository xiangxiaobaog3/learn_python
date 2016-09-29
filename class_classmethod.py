# -*- coding:utf-8 -*-

# 类方法需要被其他实例共享,同时又需要使用当前实例的属性,则将其定义为类方法

class Fruit:
    price = 0

    def __init__(self):
        self.__color = "red"

    def getColor(self):     # 类的方法,至少有一个参数self
        print self.__color

    @classmethod
    def getPrice(self):
        print self.price

    def __getPrice(self):
        self.price += 10
        # print Fruit.price

    count = classmethod(__getPrice)

if __name__ == '__main__':
    apple = Fruit()
    apple.getColor()
    Fruit.count()
    Fruit.getPrice()