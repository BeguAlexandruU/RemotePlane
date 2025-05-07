import time

from drone.control.controlManager import controlManager
from drone.inputAxis import inputAxis

class Pilot:
    def __init__(self):
        self.inputAxis = inputAxis()
        self.vInputAxis = inputAxis()

        self.controlManager = controlManager()
    
    def setup(self):
        self.controlManager.setup()
    
    def cleanup(self):
        self.controlManager.cleanup()
    
    def setInput(self):
        
        pass
    
