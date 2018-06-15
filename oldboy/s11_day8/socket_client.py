# -*- coding:utf-8 -*-

import socket

obj = socket.socket()
obj.connect(['localhost', 8341])
obj.send("Hello, World")
server_data = obj.recv(1024)
print server_data
obj.close()