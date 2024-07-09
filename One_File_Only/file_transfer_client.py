import socket
import json

HEADERSIZE = 10

FILENAME = '/Users/ethan_/Documents/git/CSE_310-Applied_Programming/File_Transfer/new_file.json'

def save_file(filename, file_data):
    try:
        with open(filename, 'w') as file_handle:
            file_handle.write(file_data)
    except FileNotFoundError:
        print(f"Could not find {filename}.")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((socket.gethostname(), 65432))

    #while True: 

    full_data = ''
    new_file_data = True
    while True:
        file_data = s.recv(16)
        if new_file_data:
            print(f"New message length: {file_data[:HEADERSIZE]}.")
            file_data_len = int(file_data[:HEADERSIZE])
            new_file_data = False

        full_data += file_data.decode("utf-8")

        if len(full_data) - HEADERSIZE == file_data_len:
            print("Full file_data revied.")
            print(full_data[HEADERSIZE:])
            new_file_data = True
            save_file(FILENAME, full_data[HEADERSIZE:])
            break