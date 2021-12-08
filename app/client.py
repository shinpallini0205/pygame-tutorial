import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((os.environ.get("PYGAME_SERVER_IP"), 5555))
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

full_msg = b''
while True:
    msg = s.recv(1024)
    if len(msg) <= 0:
        break
    full_msg += msg
    print(full_msg.decode("utf-8"))