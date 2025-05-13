import time

from control.controlManager import controlManager
from inputAxis import inputAxis

class Pilot:
    def __init__(self):
        self.inputAxis = inputAxis()
        self.vInputAxis = inputAxis()

        self.controlManager = controlManager()
        
        print("Pilot initialized")

        self.setup()

    def setup(self):
        self.controlManager.setup()
    
    def cleanup(self):
        self.controlManager.cleanup()
    
    def setInput(self, data):
        if data["axis"] == "eleron":
            self.inputAxis.setRoll(data["value"])
            self.controlManager.eleronControl.setAxis(data["value"])
        elif data["axis"] == "elevator":
            self.inputAxis.setPitch(data["value"])
        elif data["axis"] == "motor":
            self.inputAxis.setThrottle(data["value"])
        
        print("-- Pilot ---------------------")
        print("Pilot: ", self.inputAxis.pitch, self.inputAxis.roll, self.inputAxis.throttle)
        print("_______________________________________")
    
    def setVInput(self, data):
        if data["axis"] == "eleron":
            self.vInputAxis.setRoll(data["value"])
            self.controlManager.eleronControl.setAxis(data["value"])
        elif data["axis"] == "elevator":
            self.vInputAxis.setPitch(data["value"])
        elif data["axis"] == "motor":
            self.vInputAxis.setThrottle(data["value"])
        
        print("-- VPilot ---------------------")
        print("VPilot: ", self.vInputAxis.pitch, self.vInputAxis.roll, self.vInputAxis.throttle)
        print("_______________________________________")

        
