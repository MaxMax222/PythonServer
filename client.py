import socket
import os

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 1234

client.connect(('localhost', port))

finished = False

def send_files(client):
    done = False
    while not done:
        file_path = input('Enter path to a file that you want to upload: -> ')
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                client.send(file.name.encode())
                client.sendfile(file)
            done = input('Do you wish to upload any other files? [y/n]: -> ') == 'n'
        else:
            print("File doesn't exist. Please enter a valid file path.")

def download_files(client):
    done = False
    while not done:
        file_name = input('Enter file name that you want to download: -> ')
        client.send(file_name.encode())
        data = client.recv(2048)
        if data:
            with open(file_name, 'wb') as file:
                file.write(data)
                os.rename(file.name, r'c:\Users\97254\Downloads')
            print(f"{file_name} downloaded successfully.")
        else:
            print("File not found on the server.")
        done = input('Do you wish to download any other files? [y/n]: -> ') == 'n'

while not finished:
    operation = int(input('Would you like to upload or download a file from the server? [1 - upload / 2 - download] -> '))
    client.send(str(operation).encode())
    if operation == 1:
        send_files(client)
    else:
        download_files(client)
    finished = input('Do you wish to finish? [y/n]: -> ') == 'y'
    
client.close()
