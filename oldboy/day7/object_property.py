# -*- coding:utf-8 -*-
# 只支持新式类

class Goods(object):

    @property
    def price(self):
        print '@property'

    @price.setter
    def price(self, value):
        print '@price.setter'

    @price.deleter
    def price(self):
        print '@price.deleter'


obj = Goods()

obj.price

obj.price = 123

del obj.price