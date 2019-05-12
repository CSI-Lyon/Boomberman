import socket
import threading
import sys


host = "192.168.0.12"
portEnvoi = 12346
portRecoit = 12345

connEnvoi = socket.socket()
connRecoit = socket.socket()

connRecoit.bind((host, portRecoit))
connEnvoi.bind((host, portEnvoi))
connRecoit.listen(5)
connEnvoi.listen(5)

def processMessages(connRecoit, addr, connEnvoi, addr2):
    while True:
        try:
            data = connRecoit.recv(1024)
            if not data:
                connRecoit.close()
            print(addr1, data.decode("utf-8"))
            connEnvoi.sendall(bytes(data.decode("utf-8"), "utf-8"))
        except:
            connRecoit.close()
            print("Connection closed by", addr1, addr2)
            # Quit the thread.
            sys.exit()

while True:
    connection1, addr1 = connRecoit.accept()
    connection2, addr2 = connEnvoi.accept()
    print('Got connection from ', addr1[0], '(', addr1[1], ')')
    # Listen for messages on this connection
    listener = threading.Thread(target=processMessages, args=(connection1, addr1, connection2, addr2))
    listener.start()
