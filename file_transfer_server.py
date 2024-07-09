import socket

HEADERSIZE = 10

IP = 65432

def load_file(filename):
    data_text = ''
    try:
        with open(filename, 'r') as file_handle:
            data_text = file_handle.read()
    except FileNotFoundError:
        print(f"Could not find {filename}.")

    return data_text

def reciece_file_request(client_socket):
    try:
        file_request_header = client_socket.recv(HEADERSIZE)

        if not len(file_request_header):
            return False
        
        file_request_length = int(file_request_header.decode("utf-8").strip())
        return {"header": file_request_header, "data": client_socket.recv(file_request_length)}

    except:
        return False


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((socket.gethostname(), IP))
    server_socket.listen()

    sockets_list = [server_socket]

    while True:
        client_socket, client_address = server_socket.accept()
        user_file = reciece_file_request(client_socket)
        if user_file is False:
            break

        print(f"Connection from {client_address} has been established!")
        # print(f'{user_file}')
        # print(user_file['data'])

        user_file_data = user_file['data'].decode("utf-8")

        if user_file_data == 'cities':
            print("Client entered 'cities'.")
            filename = 'cities.json'
        if user_file_data == 'states':
            print("Client entered 'states'.")
            filename = 'states.json'
        if user_file_data == 'languages':
            print("Client entered 'languages'.")
            filename = 'languages.json'
        
        file_data = load_file(filename)
        file_data = f'{len(file_data):<{HEADERSIZE}}' + file_data

        client_socket.send(bytes(file_data, "utf-8"))
        client_socket.close()