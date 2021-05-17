# https://www.tutorialspoint.com/python/python_networking.htm
# https://docs.python.org/3/library/socket.html

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 5050))
s.listen(1)
# s = socket.create_server(("localhost", 5050))
print(socket.gethostname())

for _ in range(2):
    sock, addr_info = s.accept()
    with sock:
        print(addr_info)
        print(sock.recv(2).decode(encoding='utf-8'))
        print(sock.recv(2).decode(encoding='utf-8'))
        print(sock.recv(2).decode(encoding='utf-8'))
        sock.sendall(b"okay")
# sock.close()
# or
# sock.shutdown(socket.SHUT_RDWR)
