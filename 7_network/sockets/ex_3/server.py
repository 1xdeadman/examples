import socket
import threading

def handle_client(conn:socket.socket):
    with conn:
        # conn.settimeout(1.0)
        data = bytes()
        while conn:
            try:
                data = conn.recv(1024)
                if not data:
                    break
                print(data)
                conn.sendall(data)
            except Exception as ex:
                print('ex')
                break
        print("data: ", data)


HOST = ''
PORT = 6666
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen(10)
    server.settimeout(10.0)
    while True:
        try:
            client, addr = server.accept()
            print("[*] Accepted connection from: {0}:{1}".format(addr[0],addr[1]))
            # spin up our client thread to handle incoming data
            threading.Thread(target=handle_client,args=(client,)).start()
        except Exception as ex:
            print(ex)