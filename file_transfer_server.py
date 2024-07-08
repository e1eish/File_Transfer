import socket
import json

HEADERSIZE = 10

FILENAME = 'saved_file.json'

def load_file(filename):
    data_text = ''
    try:
        with open(filename, 'r') as file_handle:
            data_text = file_handle.read()
    except FileNotFoundError:
        print(f"Could not find {filename}.")

    return data_text


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((socket.gethostname(), 65432))
    s.listen(5)

    while True:
        client_socket, address = s.accept()
        print(f"Connection from {address} has been established!")

        file_data = load_file(FILENAME)
        file_data = f'{len(file_data):<{HEADERSIZE}}' + file_data

        client_socket.send(bytes(file_data, "utf-8"))
        client_socket.close()