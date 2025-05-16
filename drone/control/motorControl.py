import pigpio
import time

pin = None
esc = None

max_speed = 100
armed = False

def setup(gpio_pin):
    global esc, pin
    pin = gpio_pin
    esc = pigpio.pi()
    if not esc.connected:
        raise RuntimeError("Could not connect to pigpio daemon.")
    esc.set_servo_pulsewidth(pin, 0)
    print(f"ESC initialized")

def arm():
    global armed, pin, esc
    if armed:
        print("ESC already armed.")
        return
    print("Arming ESC...")
    esc.set_servo_pulsewidth(pin, 1000)
    time.sleep(2)
    esc.set_servo_pulsewidth(pin, 2000)
    time.sleep(2)
    esc.set_servo_pulsewidth(pin, 1000)
    time.sleep(2)
    armed = True
    print("ESC armed")

def setAxis(value):
    global armed, pin, esc, max_speed
    if esc is None:
        print("ESC not initialized.")
        return
    if not armed:
        print("ESC not armed. Call arm() first.")
        return
    
    speed = int(((-value+1) * max_speed)/2)
    
    pulse_width = 1000 + (speed * 10)
    esc.set_servo_pulsewidth(pin, pulse_width)

def cleanup():
    global esc, pin
    if esc is None:
        print("ESC not initialized.")
        return
    print("Cleaning up ESC...")
    esc.set_servo_pulsewidth(pin, 0)
    esc.stop()
    print("ESC cleaned up.")
