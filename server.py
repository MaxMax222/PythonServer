import socket
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 1234

server.bind(('', port))
print(f'Socket bound to port {port}')

server.listen(10)
print('Socket listening')

def recieve_file(client):
    file_name = client.recv(2048).decode()  
    file_path = os.path.join(r'c:\Users\97254\Desktop\PythonServerData', file_name)

    with open(file_path, 'wb') as file:
        while True:
            data = client.recv(1024)
            if not data:
                break
            file.write(data)

def send_file(client):
    file_name = client.recv(2048).decode()
    if os.path.exists(file_name):
        with open(file_name, 'rb') as file:
            data = file.read()
            client.send(data)
    else:
        client.send(b'File not found on server.')

while True:
    client, addr = server.accept()

    operation = client.recv(2048).decode()
    if int(operation) == 1:
        recieve_file(client)
    else:
        send_file(client)

    client.close()