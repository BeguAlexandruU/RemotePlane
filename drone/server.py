import socket
import json

from motorControl import MotorControl
from elevatorControl import ElevatorControl
from eleronControl import EleronControl


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
                    axis = message["axis"]
                    value = message["value"]
                    if axis == 0:
                        self.eleronControl.setAxis(value)
                    elif axis == 1:
                        self.elevatorControl.setAxis(value)
                    elif axis == 3:
                        self.motorControl.setSpeed(value)
                # elif message["type"] == "button":
                #     button = message["button"]
                #     print(f"Button {button} pressed")
                # elif message["type"] == "hat":
                #     hat = message["hat"]
                #     value = message["value"]
                #     print(f"Hat {hat} moved to {value}")
            except json.JSONDecodeError:
                print("Received malformed data")
