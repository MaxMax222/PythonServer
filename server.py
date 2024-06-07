import socket
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 1234

server.bind(('', port))
print(f'Socket bound to port {port}')

server.listen(10)
print('Socket listening')
while True:
    client, addr = server.accept()

    file_name = client.recv(1042).decode()
    file_size = int(client.recv(1042).decode())

    file_path = os.path.join(r'c:\Users\97254\Desktop\PythonServerData', file_name)

    with open(file_path, 'wb') as file:
        received_data = b''
        total_received = 0
        while total_received < file_size:
            data = client.recv(1042)
            if not data:
                break
            file.write(data)
            total_received += len(data)

    client.close()