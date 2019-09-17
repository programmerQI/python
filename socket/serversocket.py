import socket

s = socket.socket()
print("socket created.")

port = 12345

s.bind(("", 12345))
print("bind socket to port 123456")

s.listen()
print("listening...")

while True:
    c, addr = s.accept()
    print("Got connection from: ", addr)
    msg = "Thanks for connection."
    byt = msg.encode()
    c.send(byt)
    c.close()
