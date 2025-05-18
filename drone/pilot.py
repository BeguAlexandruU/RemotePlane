import control.controlManager as controlManager
from control.controlManager import eleronControl
from control.controlManager import elevatorControl
from control.controlManager import motorControl

inputAxis = {
        "pitch": 0,
        "roll": 0,
        "throttle": 0
    }
vInputAxis = {
        "pitch": 0,
        "roll": 0,
        "throttle": 0
    }

inputPriority = 1
vInputPriority = 1

print("Pilot initialized")

def setup():
    controlManager.setup()
    
def cleanup():
    controlManager.cleanup()

def updateEleron():
    global inputAxis, vInputAxis, inputPriority, vInputPriority
    eleronControl.setAxis((inputAxis["roll"] * inputPriority) + (vInputAxis["roll"] * vInputPriority))

def updateElevator():
    elevatorControl.setAxis(inputAxis["pitch"] * inputPriority + vInputAxis["pitch"] * vInputPriority)

def updateMotor():
    motorControl.setAxis(inputAxis["throttle"])

def setInput(data):
    global inputAxis
    if data["axis"] == "eleron":
        inputAxis["roll"] = data["value"]
        updateEleron()
    elif data["axis"] == "elevator":
        inputAxis["pitch"] = data["value"]
        updateElevator()
    elif data["axis"] == "motor":
        inputAxis["throttle"] = data["value"]
        updateMotor()
        
    # print("-- Pilot ---------------------")
    # print("Pilot: ", inputAxis.pitch, inputAxis.roll, inputAxis.throttle)
    # print("_______________________________________")
    
def setVInput(data):
    global vInputAxis
    
    if data["axis"] == "eleron":
        vInputAxis["roll"] = data["value"]
        updateEleron()
    elif data["axis"] == "elevator":
        vInputAxis["pitch"] = data["value"]
        updateElevator()
    elif data["axis"] == "motor":
        vInputAxis["throttle"] = data["value"]
        updateMotor()
    
    # print("-- VPilot ---------------------")
    # print("VPilot: ", vInputAxis.pitch, vInputAxis.roll, vInputAxis.throttle)
    # print("_______________________________________")

def setButton(data):
    # if data["button"] == "arm":
    #     controlManager.motorControl.arm()
    #     controlManager.eleronControl.arm()
    # elif data["button"] == "disarm":
    #     controlManager.motorControl.disarm()
    #     controlManager.eleronControl.disarm()
    if data["button"] == "mode":
        changeMode(data["value"])
    elif data["button"] == "trimElevator":
        # changeMode(data["value"])
        elevatorControl.setTrim(data["value"])
        updateElevator()

def changeMode(mode):
    global inputPriority, vInputPriority
    if mode == "manual":
        inputPriority = 1
        vInputPriority = 0
    elif mode == "virtual":
        inputPriority = 0
        vInputPriority = 1
    elif mode == "mixed":
        inputPriority = 1
        vInputPriority = 1
    
    print(f"Pilot mode changed to {mode}")