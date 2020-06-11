import socket

HOST = ''
PORT = 50007
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    s.settimeout(5.0)
    # s.setblocking(False)
    # s.setblocking(False)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        conn.settimeout(1.0)
        data = bytes()
        while conn:
            try:
                data += conn.recv(2)
                if not data:
                    break
                print(data)
                conn.sendall(data)
            except Exception as ex:
                print('ex')
                break