import socket
import threading
import sys

host = "192.168.0.12"
portEnvoi = 12345
portReception = 12346
connEnvoi = socket.socket()
connReception = socket.socket()

connEnvoi.connect((host, portEnvoi))
connReception.connect((host, portReception))

data = ""

def processMessages(connReception, connEnvoi):
    while True:
        try:
            data = connReception.recv(1024)
            if not data:
                connReception.close()
            print(data.decode("utf-8"))
        except:
            connEnvoi.close()
            connReception.close()
            print("Connection closed by")
            # Quit the thread.
            sys.exit()
    if data=="quit":
        sys.exit()

def sender(connEnvoi,data):
    while data != "quit":
        data = input("message a envoyer : ")
        try:
            connEnvoi.sendall(bytes(data, "utf-8"))
        except:
            data = "quit"
            sys.exit()
        #data = connReception.recv(1024)
        #print(str(data.decode("utf-8")))



listener = threading.Thread(target=processMessages, args=(connReception, connEnvoi))
listener.start()

send = threading.Thread(target=sender, args=(connEnvoi,data))
send.start()
