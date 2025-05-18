# Import libraries
import RPi.GPIO as GPIO
import time

left_pin = None
right_pin = None

left_servo = None
right_servo = None

# last_update_time = 0
# update_interval = 0.05
last_value = 0

max_angle = 60
min_angle = -45
    
def setup(left_pin_param, right_pin_param):
    global left_servo, right_servo, left_pin, right_pin
    left_pin = left_pin_param
    right_pin = right_pin_param
    
    # Set GPIO numbering mode
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(left_pin, GPIO.OUT)
    GPIO.setup(right_pin, GPIO.OUT)
    left_servo = GPIO.PWM(left_pin, 50)
    right_servo = GPIO.PWM(right_pin, 50)
    left_servo.start(0)
    right_servo.start(0)
    
    print(f"Eleron servos initialized on pins {left_pin} and {right_pin}")

def arm():
    print("Arming eleron servos...")
    # Arm the servos and setting them to neutral position
    setAxis(-1)
    time.sleep(1)
    setAxis(1)
    time.sleep(1)
    setAxis(0)
    
    print("Eleron servos armed.")


def setAxis(value):
    global last_value
    global max_angle
    global min_angle
    
    # input value is between -1 and 1
    # -1 is full left, 0 is neutral, 1 is full right
    value = max(-1, min(1, value))  # Clamp value to be between -1 and 1

    # Ignore small changes
    if abs(value - last_value) < 0.01:  
        return
    last_value = value

    # Process the input
    if value >= 0:  # Stick right
        right_eleron_angle = -value * max_angle
        left_eleron_angle = value * min_angle
    else:           # Stick left
        right_eleron_angle = value * min_angle
        left_eleron_angle = -value * max_angle

    # print(f"Left eleron: {left_eleron_angle} \t Right eleron: {right_eleron_angle}")
    set_left_angle(left_eleron_angle)
    set_right_angle(right_eleron_angle)

def set_left_angle(angle):
    global left_servo
    
    # Convert angle to duty cycle
    angle = angle + 90
    duty_cycle = 2+(angle/18)
    left_servo.ChangeDutyCycle(duty_cycle)
    time.sleep(0.01)
    left_servo.ChangeDutyCycle(0)
    
def set_right_angle(angle):
    global right_servo
    
    # Convert angle to duty cycle
    angle = angle + 90
    duty_cycle = 2+(angle/18)
    right_servo.ChangeDutyCycle(duty_cycle)
    # time.sleep(0.1)  # Allow servo time to receive and process the signal
    # right_servo.ChangeDutyCycle(0)  # Stop the signal to prevent jitter

def cleanup():
    global left_servo, right_servo
    
    print("Cleaning up eleron servos...")
    left_servo.stop()
    right_servo.stop()
    GPIO.cleanup()
    print("Eleron servos cleaned up")
        
