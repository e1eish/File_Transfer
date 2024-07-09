import socket

HEADERSIZE = 10

IP = 65432

FILENAME = '/Users/ethan_/Documents/git/CSE_310-Applied_Programming/File_Transfer/new_file.json'

desired_file = input("Enter the desired file (languages, states, cities): ")

def save_file(filename, file_data):
    '''
    Save json data to the file specified.
    '''
    try:
        with open(filename, 'w') as file_handle:
            file_handle.write(file_data)
    except FileNotFoundError:
        print(f"Could not find {filename}.")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((socket.gethostname(), IP))

    # Send the desired file with a header to the server.
    filename = desired_file.encode("utf-8")
    filename_header = f"{len(filename):<{HEADERSIZE}}".encode("utf-8")
    client_socket.send(filename_header + filename)

    full_data = ''
    new_file_data = True
    while True:
        file_data = client_socket.recv(16)
        if new_file_data:
            # Get the length of the incoming data.
            print(f"New message length: {file_data[:HEADERSIZE]}.")
            file_data_len = int(file_data[:HEADERSIZE])
            new_file_data = False

        # Add incoming data.
        full_data += file_data.decode("utf-8")

        if len(full_data) - HEADERSIZE == file_data_len:
            # Once the incoming data is finished save the file.
            print("Full file_data revied.")
            print(full_data[HEADERSIZE:])
            new_file_data = True
            save_file(FILENAME, full_data[HEADERSIZE:])
            break