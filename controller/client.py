import socket
import json
import threading

from controller import Controller

class Client:
    def __init__(self, server_ip='100.77.62.12', port=65432):
    # def __init__(self, server_ip='localhost', port=65432):
        self.server_ip = server_ip
        self.port = port
        
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        self.controller = Controller(send_data_callback=self.send_data)
        self.controller.setup()
    
    # Function to run the controller
    def run(self):
        self.controller.run()

    # Function to send data asynchronously
    def send_data(self, data):
        message = json.dumps(data).encode()
        self.client.sendto(message, (self.server_ip, self.port))  # Fixed variable name

