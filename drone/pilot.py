import time

from control.controlManager import controlManager
from inputAxis import inputAxis

class Pilot:
    def __init__(self):
        self.inputAxis = inputAxis()
        self.vInputAxis = inputAxis()

        self.inputPriority = 0
        self.vInputPriority = 1

        self.controlManager = controlManager()
        
        print("Pilot initialized")

        self.setup()

    def setup(self):
        self.controlManager.setup()
    
    def cleanup(self):
        self.controlManager.cleanup()

    def updateEleron(self):
        self.controlManager.eleronControl.setAxis((self.inputAxis.roll * self.inputPriority) + (self.vInputAxis.roll * self.vInputPriority))
    
    def setInput(self, data):
        if data["axis"] == "eleron":
            self.inputAxis.setRoll(data["value"])
            self.updateEleron()
        elif data["axis"] == "elevator":
            self.inputAxis.setPitch(data["value"])
        elif data["axis"] == "motor":
            self.inputAxis.setThrottle(data["value"])
        
        # print("-- Pilot ---------------------")
        # print("Pilot: ", self.inputAxis.pitch, self.inputAxis.roll, self.inputAxis.throttle)
        # print("_______________________________________")
    
    def setVInput(self, data):
        if data["axis"] == "eleron":
            self.vInputAxis.setRoll(data["value"])
            self.updateEleron()
            # self.controlManager.eleronControl.setAxis(data["value"])
            # self.controlManager.eleronControl.setAxis((self.inputAxis.roll * self.inputPriority) + (self.vInputAxis.roll * self.vInputPriority))
            
        elif data["axis"] == "elevator":
            self.vInputAxis.setPitch(data["value"])
        elif data["axis"] == "motor":
            self.vInputAxis.setThrottle(data["value"])
        
        # print("-- VPilot ---------------------")
        # print("VPilot: ", self.vInputAxis.pitch, self.vInputAxis.roll, self.vInputAxis.throttle)
        # print("_______________________________________")

    def setButton(self, data):
        # if data["button"] == "arm":
        #     self.controlManager.motorControl.arm()
        #     self.controlManager.eleronControl.arm()
        # elif data["button"] == "disarm":
        #     self.controlManager.motorControl.disarm()
        #     self.controlManager.eleronControl.disarm()
        if data["button"] == "mode":
            self.changeMode(data["value"])

    def changeMode(self, mode):
        if mode == "manual":
            self.inputPriority = 1
            self.vInputPriority = 0
        elif mode == "virtual":
            self.inputPriority = 0
            self.vInputPriority = 1
        elif mode == "mixed":
            self.inputPriority = 1
            self.vInputPriority = 1
        
        print(f"Pilot mode changed to {mode}")
