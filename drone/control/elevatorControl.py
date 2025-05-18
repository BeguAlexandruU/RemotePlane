import RPi.GPIO as GPIO
import time

pin = None
servo = None

max_angle = 40
min_angle = -45
trim = 0
    
def setup(pin_param):
    global servo, pin
    pin = pin_param
    
    # Set GPIO numbering mode
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    servo = GPIO.PWM(pin, 50)
    servo.start(0)
    
    print(f"Elevator servo initialized on pin {pin}")

def arm():
    print("Arming elevator servos...")
    setAxis(-1)
    time.sleep(1)
    setAxis(1)
    time.sleep(1)
    setAxis(0)
    
    print("Elevator servos armed.")

def setAxis(value):
    global max_angle
    global min_angle
    global servo
    global trim
    
    if value >= 0:  # to me
        elevator_angle = value * max_angle 
    else:           # from me
        elevator_angle = -value * min_angle  
        
    # Apply trim to adjust neutral position
    elevator_angle = elevator_angle + (trim)
                    
    # Ensure value stays within allowed range
    elevator_angle = max(min_angle, min(max_angle, elevator_angle))
    
    # print(f"Elevator: {elevator_angle}")
    
    # Use daemon threads to set servo angles
    set_angle(elevator_angle)

def set_angle(angle):
    global servo
    
    # Convert angle to duty cycle
    angle = angle + 90
    duty_cycle = 2+(angle/18)
    servo.ChangeDutyCycle(duty_cycle)
    # time.sleep(0.1)  # Allow servo time to receive and process the signal
    # servo.ChangeDutyCycle(0)  # Stop the signal to prevent jitter
    
def setTrim(value):
    global trim
    # Set trim value to adjust neutral position
    trim = max(min_angle, min(max_angle, trim + value))
    print(f"Trim elevator: {trim}")


def cleanup():
    global servo
    if servo is None:
        print("Servo not initialized.")
        return
    servo.stop()
    GPIO.cleanup()
    print("Elevator servo cleaned up")
    
