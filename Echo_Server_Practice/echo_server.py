import socket

HOST = socket.gethostname()

PORT = 65432

# Set up socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((socket.gethostname(), PORT))
    s.listen()
    connection, address = s.accept()

# Exchange data
    with connection:
        print(f"Connected by {address}")
        while True:
            data = connection.recv(1024)
            if not data:
                break
            connection.sendall(data)

