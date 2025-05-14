import pigpio
import time

class MotorControl:
    def __init__(self, gpio_pin):
        self.pin = gpio_pin
        self.pi = pigpio.pi()
        self.max_speed = 100
        self.armed = False
        print(f"ESC initialized on GPIO {self.pin}")
    
    def setup(self):
        if not self.pi.connected:
            raise RuntimeError("Could not connect to pigpio daemon.")
        self.pi.set_servo_pulsewidth(self.pin, 0)
        print("ESC ready to arm.")

    def arm(self):
        print("Arming ESC...")
        self.pi.set_servo_pulsewidth(self.pin, 1000)
        time.sleep(2)
        self.pi.set_servo_pulsewidth(self.pin, 2000)
        time.sleep(2)
        self.pi.set_servo_pulsewidth(self.pin, 1000)
        time.sleep(2)
        self.armed = True
        print("ESC armed.")

    def setSpeed(self, value):
        if not self.armed:
            print("ESC not armed. Call arm() first.")
            return
        
        speed = int(((-value+1) * self.max_speed)/2)
        
        pulse_width = 1000 + (speed * 10)
        self.pi.set_servo_pulsewidth(self.pin, pulse_width)
    
    def cleanup(self):
        print("Cleaning up ESC...")
        self.pi.set_servo_pulsewidth(self.pin, 0)
        self.pi.stop()
        print("ESC cleaned up.")
