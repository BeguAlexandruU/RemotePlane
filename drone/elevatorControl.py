# Import libraries
import RPi.GPIO as GPIO
import threading
import time

class ElevatorControl:
    def __init__(self, pin):
        self.pin = pin
        
        self.max_angle = 45
        self.min_angle = -70
        self.trim = 0
        print(f"Elevator servo initialized on pin {self.pin}")
    
        
    def setup(self):
        # Set GPIO numbering mode
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.servo = GPIO.PWM(self.pin, 50)
        self.servo.start(0)
        
        print(f"Elevator servo initialized on pin {self.pin}")
        
    def setAxis(self, value):
        
        if value >= 0:  # Stick right
            elevator_angle = (value) * self.min_angle 
        else:  # Stick left
            elevator_angle = -value * self.max_angle  
            
        # Apply trim to adjust neutral position
        elevator_angle = elevator_angle + (self.trim)
                      
        # Ensure value stays within allowed range
        elevator_angle = max(self.min_angle, min(self.max_angle, elevator_angle))
        
        print(f"Elevator: {elevator_angle}")
        
        # Use daemon threads to set servo angles
        self.set_angle(elevator_angle)
    
    def set_angle(self, angle):
        angle = angle + 90
        duty_cycle = 2+(angle/18)
        self.servo.ChangeDutyCycle(duty_cycle)
        # time.sleep(0.1)  # Allow servo time to receive and process the signal
        self.servo.ChangeDutyCycle(0)  # Stop the signal to prevent jitter
      
    def cleanup(self):
        self.servo.stop()
        GPIO.cleanup()
        print("Elevator servo cleaned up")
        