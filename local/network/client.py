import socket

host = "192.168.0.12"
portEnvoi = 12345
portRecoit = 12346
connEnvoi = socket.socket()
connRecoit = socket.socket()

connEnvoi.connect((host, portEnvoi))
connRecoit.connect((host, portRecoit))

data = ""

while data != "quit":
    data = input("message a envoyer : ")
    connEnvoi.sendall(bytes(data, "utf-8"))
    data = connRecoit.recv(1024)
    print(str(data.decode("utf-8")))

connEnvoi.close()
connRecoit.close()
