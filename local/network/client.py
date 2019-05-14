import socket
import threading
import sys

data = ""

def connection(host, portEnvoi):
    global connection1, connection2
    portReception = portEnvoi + 1
    connEnvoi = socket.socket()
    connReception = socket.socket()

    connection1 = connEnvoi.connect((host, portEnvoi))
    connection2 = connReception.connect((host, portReception))

    data = ""

def processMessages(connReception, connEnvoi):
    while True:
        try:
            data = connReception.recv(1024)
            if not data:
                connReception.close()
            print(data.decode("utf-8"))
        except:
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


def initialise(connEnvoi, connReception):
    listener = threading.Thread(target=processMessages, args=(connReception, connEnvoi))
    listener.start()

    send = threading.Thread(target=sender, args=(connEnvoi,data))
    send.start()

connection("192.168.0.12", 12345)
initialise(connection1, connection2)
