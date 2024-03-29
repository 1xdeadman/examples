import socket
import sys
import time

HOST = 'localhost'
PORT = 6666


if len(sys.argv) == 1:
    print('need more args')
    exit(0)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.settimeout(5.0)
    for i in range(10):
        data = bytes(f"{i}: message from {sys.argv[1]}", encoding='utf-8')
        print("Send: ", data)
        s.sendall(data)
        print(s.recv(1024))
        time.sleep(1)
print("Closed")
