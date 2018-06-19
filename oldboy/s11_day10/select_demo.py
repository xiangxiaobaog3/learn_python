# -*- coding:utf-8 -*-

import select
import sys

while True:
    # f = file(), obj = socket(), sys.stdin = 终端输入
    # 监听用户输入
    # 如果用户输入内容， select 感知 sys.stdin 改变
    # 将改变的文件句柄保存至列表，并将列表作为select第一个参数返回
    # 如果用户未输入内容，select 第一个参数 = []
    readable, writeable, error = select.select([sys.stdin,sys.stdout,],[],[],1)

    if sys.stdin in readable:
        print 'select get stdin', sys.stdin.readline()