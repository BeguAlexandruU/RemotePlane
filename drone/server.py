import socket
import json

HOST = "0.0.0.0"  # Listen on all network interfaces
PORT = 65432

# Setup UDP Socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print(f"Server listening on {HOST}:{PORT}...")

while True:
    data, addr = server.recvfrom(1024)  # Receive data (max 1024 bytes)
    try:
        message = json.loads(data.decode())
        print(f"Received from {addr}: {message}")
    except json.JSONDecodeError:
        print("Received malformed data")
