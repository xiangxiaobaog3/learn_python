# -*- coding:utf-8 -*-

import socket

obj_server = socket.socket()
obj_server .bind(('localhost', 8341))
obj_server.listen(5)

while True:
    print 'waiting....'
    conn, addr = obj_server.accept()
    client_data = conn.recv(1024)
    conn.sned("HTTP/1.1 200 OK\r\n\r\n")
    conn.close()