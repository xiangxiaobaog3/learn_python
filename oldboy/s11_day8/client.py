# -*- coding:utf-8 -*-

import socket

client = socket.socket()

ip_port = ('127.0.0.1',9999)

client.connect(ip_port)
client.settimeout(5)

while True:
	data = client.recv(1024)
	print 'receive:',data
	inp = raw_input('client:')
	client.sendall(inp)
	if inp == 'exit':
		break

client.close()