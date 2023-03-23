import socket

myIP = 'localhost'
myPort = 12345
print('SERVER START')

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print('SERVER CONFIG')

listener.bind((myIP, myPort))
listener.listen(0)
print('SERVER LISTEN port and addr')

clients = []
i = 0
while i < 3:
    clients.append(listener.accept())
    print('SERVER GET CLIENT')
    print(clients)
    for item in clients:
        item[0].send("Hello all clients".encode('utf8'))
    i += 1

for item in clients:
    item[0].send("Connection closed".encode('utf8'))
    item[0].close()
    print("Connection closed")
    
print('SERVER CLOSE')
listener.close()
