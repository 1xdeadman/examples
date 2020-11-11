# https://www.tutorialspoint.com/python/python_networking.htm
# https://docs.python.org/3/library/socket.html
# https://pypi.org/project/requests/

import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(("localhost", 5050))
# s.listen()
s = socket.create_server(("localhost", 5050))
print(socket.gethostname())

sock, addr_info = s.accept()
with sock:
    print(addr_info)
    print(sock.recv(1024).decode(encoding='utf-8'))
    sock.sendall(b"okay")
# sock.shutdown(socket.SHUT_RDWR)
