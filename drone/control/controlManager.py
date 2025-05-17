from . import motorControl
from . import eleronControl
from . import elevatorControl

def setup():
    eleronControl.setup(20,21)
    elevatorControl.setup(16)
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

