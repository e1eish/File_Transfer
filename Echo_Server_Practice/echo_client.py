import socket

HOST = socket.gethostname()

PORT = 65432

# Client connection initialization
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

# Exchange data
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received {data}")