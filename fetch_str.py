# -*- coding:utf-8 -*-

def fetch(backend):
    fetch_list = []

    with open('ha') as obj:
        flag = False
        for line in obj:
            if line.strip() == "backend %s" % backend
                flag = True
                continue
            if line.strip().startswith('backend'):
                #flag = False
                break;
            if flag and line.strip():
                fetch_list.append(line.strip())

fetch("buy.oldboy.org")