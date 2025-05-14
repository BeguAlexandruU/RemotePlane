import socket
import json

class Server:
    def __init__(self, pilot, host='0.0.0.0', port=65432):
        self.pilot = pilot
        
        self.host = host
        self.port = port

        # Create a UDP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.host, self.port))
        print(f"Server started on {self.host}:{self.port}") 
    
    def run(self):
        print(f"Server listen on {self.host}:{self.port}")
        while True:
            data, addr = self.sock.recvfrom(1024)  # Buffer size is 1024 bytes
            try:
                message = json.loads(data.decode())
                # print(f"Received from {addr}: {message}")
                if message["type"] == "axis":
                    self.pilot.setInput(message)

                elif message["type"] == "button":
                    self.pilot.setButton(message)

                # elif message["type"] == "hat":
                #     hat = message["hat"]
                #     value = message["value"]
                #     print(f"Hat {hat} moved to {value}")
            except json.JSONDecodeError:
                print("Received malformed data")
