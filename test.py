# -*- coding:utf-8 -*-

li = [11, 22, 33]
sl = [1, 2, 3]

new_list = map(lambda a, b: a + b, li, sl)
print new_list

for i in range(10):
    print i

def mrange(arg):
    seed = 0
    while True:
        seed = seed + 1
        if seed >= arg:
            return
        else:
            yield seed

for i in mrange(10):
    print i