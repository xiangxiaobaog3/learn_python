# -*- coding:utf-8 -*-
import json
import os

def fetch(backend):
    fetch_list = []
    with open('haporxy.conf') as obj:
        flag = False
        for line in obj:
            if line.strip() == "backend %s" % backend:
                flag = True
                continue
            # 判断，如果当前是backend开头，不再放
            if flag and line.strip().startswith('backend'):
                print flag
                #flag = False
                break
            if flag and line.strip():
                fetch_list.append(line.strip())
    return fetch_list

def add(dict_info):
    backend_title = dict_info.get('backend')
    crrent_title = "backend %s" % backend_title
    crrent_record = "server %s %s weight %s maxconn %s" % (dict_info['record']['server'],dict_info['record']['server'],dict_info['record']['weight'],dict_info['record']['maxconn'])
    fetch_list = fetch(backend_title)
    if fetch_list:
        #pass #存在backend,则只需添加记录
        #要插入的记录存在
        #要插入的记录不存在
        if crrent_record in fetch_list:
            pass
        else:
            fetch_list.append(crrent_record)
            # fetch_list,处理完的新列表
        with open('haporxy.conf','r') as read_obj, open('ha.new', 'w') as write_obj:
            flag = False
            has_write = False
            for line in read_obj:
                if line.strip() == crrent_title:
                    write_obj.write(line)
                    flag = True
                    continue
                if flag and line.strip().startswith('backend'):
                    flag = False
                if flag:
                    # 中,把列表所有数据写入
                    if not has_write:
                        for new_line in fetch_list:
                            temp = "%s %s \n" %(" "*8, new_line)
                            write_obj.write(temp)
                        has_write = True
                else:
                    # 上，下
                    write_obj.write(line)
    else:
        #pass #不存在backend,添加记录和backend
        #crrent_title,crrent_record
        with open('haporxy.conf') as read_obj, open('ha.new', 'w') as write_obj:
            for line in read_obj:
                write_obj.write(line)
            write_obj.write(crrent_title+'\n')
            temp = "%s %s \n" %(" "*8, crrent_record)
            write_obj.write(temp)

    os.rename('haporxy.conf', 'ha.bak')
    os.rename('ha.new', 'ha')

s = '{"bakend": "haha.oldboy.org","record":{"server": "192.168.177.12","weight": 20,"maxconn": 30}}'
data_dict = json.loads(s)
add(data_dict)
