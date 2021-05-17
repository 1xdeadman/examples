import socket


# sock = socket.create_connection(('localhost', 5050))
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(('localhost', 5050))

    data: bytes = input('input data: ').encode(encoding='utf-8')
    sock.send(data)
    print(sock.recv(1024).decode(encoding='utf-8'))
print('OK')
# sock.shutdown(socket.SHUT_RDWR)
