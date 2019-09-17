import socket

s = socket.socket()
port = 12345

s.connect(("127.0.0.1", port))

byt = s.recv(1024)
msg = byt.decode()
print(msg)
