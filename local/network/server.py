import socket
import threading
import sys


host = "192.168.0.12"
portEnvoi = 12346
portReception = 12345

connEnvoi = socket.socket()
connReception = socket.socket()

connReception.bind((host, portReception))
connEnvoi.bind((host, portEnvoi))
connReception.listen(5)
connEnvoi.listen(5)

connections = []

def processMessages(connReception, addr, connEnvoi, addr2):
    while True:
        try:
            data = connReception.recv(1024)
            if not data:
                connReception.close()
            print(addr1, data.decode("utf-8"))
            for i in connections:
                i.sendall(bytes(data.decode("utf-8"), "utf-8"))
        except:
            connReception.close()
            print("Connection closed by", addr1, addr2)
            # Quit the thread.
            sys.exit()

while True:
    connection1, addr1 = connReception.accept()
    connection2, addr2 = connEnvoi.accept()
    connections.append(connection2)
    print('Got connection from ', addr1[0], '(', addr1[1], ')')
    # Listen for messages on this connection
    listener = threading.Thread(target=processMessages, args=(connection1, addr1, connection2, addr2))
    listener.start()
