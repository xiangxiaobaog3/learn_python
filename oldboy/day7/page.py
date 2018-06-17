# -*- coding:utf-8 -*-

class Pager:

    def __init__(self, current_page):
        self.current_page = current_page
        # 每页默认显示10条数据
        self.per_items = 10

    @property
    def start(self):
        val = (self.current_page - 1) * self.per_items
        return val

    @property
    def end(self):
        val = self.current_page * self.per_items
        return val

p = Pager(3)
p.start
p.end
