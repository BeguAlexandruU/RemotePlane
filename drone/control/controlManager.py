from .motorControl import MotorControl
from .elevatorControl import ElevatorControl
from .eleronControl import EleronControl

class controlManager:
    def __init__(self):
        self.eleronControl = EleronControl(23, 24)
        self.elevatorControl = ElevatorControl(25)
        self.motorControl = MotorControl(12)
    
    def setup(self):

        self.eleronControl.setup()
        self.elevatorControl.setup()
        self.motorControl.setup()
        
        self.eleronControl.setAxis(0)
        self.elevatorControl.setAxis(0)
        self.motorControl.arm()
    
    def cleanup(self):
        
        self.eleronControl.cleanup()
        self.elevatorControl.cleanup()
        self.motorControl.cleanup()
