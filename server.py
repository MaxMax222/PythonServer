import socket

s = socket.socket()
print('socket created')

port = 1234

s.bind(('',port))

print(f'socket binded to port {port}')

s.listen(10)
print('socket listening')

while True:

    c, addr = s.accept()

    print(f'connected to {addr}')

    c.send(b'thanks for connecting')

    c.close()