import socket


# sock = socket.create_connection(('localhost', 5050))
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(('localhost', 5050))

    sock.send(b'my first try')
    print(sock.recv(1024))
print('OK')