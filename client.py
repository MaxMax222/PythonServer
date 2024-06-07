import socket
import os

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 1234

client.connect(('localhost', port))

file_path = input('Enter path to a file that you want to upload: ')
file_name = os.path.basename(file_path)
file_size = os.path.getsize(file_path)

client.send(file_name.encode())
client.send(str(file_size).encode())

with open(file_path, 'rb') as file:
    data = file.read(2048)
    while data:
        client.send(data)
        data = file.read(2048)

client.close()