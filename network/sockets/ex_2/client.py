import socket

HOST = 'localhost'
PORT = 50007
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    i = 0
    while s:
        try:
            data = s.recv(1024)
            if not data:
                break
            print(data)
            s.sendall(data)
            i += 1
            if i == 10:
                break
        except Exception as ex:
            print('ex')
            break
print('Received', repr(data))