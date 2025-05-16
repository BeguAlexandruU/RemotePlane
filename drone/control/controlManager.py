from . import motorControl
from . import eleronControl
from . import elevatorControl

def setup():
    eleronControl.setup(23,24)
    elevatorControl.setup(25)
    motorControl.setup(12)
    arm()
    
def arm():
    eleronControl.arm()
    elevatorControl.arm()
    motorControl.arm()

def cleanup():
    eleronControl.cleanup()
    elevatorControl.cleanup()
    motorControl.cleanup()

