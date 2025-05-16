import socket
import json
import pilot

host = None
port = None
sock = None

def setup(host_param='0.0.0.0', port_param=65432):
    global sock, host, port
    host = host_param
    port = port_param
    
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    print(f"Server started on {host}:{port}") 

def run():
    global sock, host, port
    if sock is None:
        print("Server not initialized. Call setup() first.")
        return
    
    print(f"Server listen on {host}:{port}")
    while True:
        data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
        try:
            message = json.loads(data.decode())
            # print(f"Received from {addr}: {message}")
            if message["type"] == "axis":
                pilot.setInput(message)
            elif message["type"] == "button":
                pilot.setButton(message)

            # elif message["type"] == "hat":
            #     hat = message["hat"]
            #     value = message["value"]
            #     print(f"Hat {hat} moved to {value}")
        except json.JSONDecodeError:
            print("Received malformed data")
