# Import libraries
import RPi.GPIO as GPIO
import threading
import time


class EleronControl:
    def __init__(self, left_pin, right_pin):
        self.left_pin = left_pin
        self.right_pin = right_pin

        self.last_update_time = 0
        self.update_interval = 0.05
        self.last_value = 0
        
        self.max_angle = 60
        self.min_angle = -45
        print(f"Eleron servos initialized on pins {self.left_pin} and {self.right_pin}")
    
        
    def setup(self):
        # Set GPIO numbering mode
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.left_pin, GPIO.OUT)
        GPIO.setup(self.right_pin, GPIO.OUT)
        self.left_servo = GPIO.PWM(self.left_pin, 50)
        self.right_servo = GPIO.PWM(self.right_pin, 50)
        self.left_servo.start(0)
        self.right_servo.start(0)
        
        print(f"Eleron servos initialized on pins {self.left_pin} and {self.right_pin}")
    
    def arm(self):
        print("Arming eleron servos...")
        # Arm the servos by setting them to neutral position
        self.setAxis(-1)
        time.sleep(1)
        self.setAxis(1)
        time.sleep(1)
        self.setAxis(0)
        
        print("Eleron servos armed.")


    def setAxis(self, value):
        if abs(value - self.last_value) < 0.05:  # Ignore small changes
            return
        
        self.last_value = value

        # Process the input as usual
        if value >= 0:
            right_eleron = -value * self.max_angle
            left_eleron = value * self.min_angle
        else:
            right_eleron = value * self.min_angle
            left_eleron = -value * self.max_angle

        print(f"Left eleron: {left_eleron} \t Right eleron: {right_eleron}")
        self.set_left_angle(left_eleron)
        self.set_right_angle(right_eleron)

    # def setAxis(self, value):
    #     # input value is between -1 and 1
    #     # -1 is full left, 0 is neutral, 1 is full right

    #     if value >= 0:  # Stick right
    #         print(f"{value} to {value%1}")
    #         value = value % 1
    #         right_eleron = -value * self.max_angle  # 0 to max
    #         left_eleron = value * self.min_angle  # 0 to min
    #     else:  # Stick left
    #         print(f"{value} to {value%-1}")
    #         value = value % -1
    #         right_eleron = value * self.min_angle  # min to 0
    #         left_eleron = -value * self.max_angle  # max to 0
            
    #     print(f"Left eleron: {left_eleron} \t Right eleron: {right_eleron}")
        
    #     self.set_left_angle(left_eleron)
    #     self.set_right_angle(right_eleron)
    
    def set_left_angle(self, angle):
        angle = angle + 90
        duty_cycle = 2+(angle/18)
        self.left_servo.ChangeDutyCycle(duty_cycle)
        time.sleep(0.01)
        self.left_servo.ChangeDutyCycle(0)
        
    def set_right_angle(self, angle):
        angle = angle + 90
        duty_cycle = 2+(angle/18)
        self.right_servo.ChangeDutyCycle(duty_cycle)
        # time.sleep(0.1)  # Allow servo time to receive and process the signal
        # self.right_servo.ChangeDutyCycle(0)  # Stop the signal to prevent jitter
    
    def cleanup(self):
        self.left_servo.stop()
        self.right_servo.stop()
        GPIO.cleanup()
        print("Eleron servos cleaned up")
        
