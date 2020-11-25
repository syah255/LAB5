import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port = 8888

s.connect(('192.168.1.14', port))

data = s.recv(1024)

s.send(b'Hi, saya client. Terima Kasih!');

print (data)

s.close()
