import socket

HEADERSIZE = 10

IP = 65432

def load_file(filename):
    '''
    Load a json file with a filename.
    filename: str
    '''
    data_text = ''
    try:
        with open(filename, 'r') as file_handle:
            data_text = file_handle.read()
    except FileNotFoundError:
        print(f"Could not find {filename}.")

    return data_text

def reciece_file_request(client_socket):
    '''
    Get a request from the client for a file to send. Split the header from the data and return both in a dictionary. If the client disconects then return false.
    '''
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

    while True:
        client_socket, client_address = server_socket.accept()
        user_file = reciece_file_request(client_socket)
        if user_file is False:
            continue

        print(f"Connection from {client_address} has been established!")
        # print(f'{user_file}')
        # print(user_file['data'])

        user_file_data = user_file['data'].decode("utf-8")

        # If the keyword for the file was sent then set the filename to that file and send the file.
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
        # Add a header to the data.
        file_data = f'{len(file_data):<{HEADERSIZE}}' + file_data

        client_socket.send(bytes(file_data, "utf-8"))
        client_socket.close()