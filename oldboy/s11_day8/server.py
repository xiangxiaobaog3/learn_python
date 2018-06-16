import socket

sk = socket.socket()
ip_port = ('127.0.0.1',9999)
sk.bind(ip_port)
sk.listen(5)

while True:
    conn,address = sk.accept()
    conn.send('hello.')
    flag = True
    while flag:
        data = conn.recv(1024)
        print data
        if data == 'exit':
            flag = False
        elif data == '0':
            conn.sendall('dafdsfsdf')
        else:
            conn.sendall('sb')
    conn.close()