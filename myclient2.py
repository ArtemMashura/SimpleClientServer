import socket

myIP = 'localhost'
myPort = 12345
print('CLIENT START')

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('CLIENT CONFIG')

connection.connect((myIP, myPort))
print('CLIENT CONNECT TO SERVER')

while True:
    content = connection.recv(1024).decode('utf8')
    if content == "Connection closed":
        break
    else:
        print(content)

connection.close()
print('CLIENT CLOSE')