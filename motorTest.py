import time
import pigpio

ESC_GPIO = 12  # GPIO pin connected to ESC's signal wire
pi = pigpio.pi()

# Set the ESC to accept servo pulses
pi.set_servo_pulsewidth(ESC_GPIO, 0)

# Function to arm the ESC
def arm_esc():
    pi.set_servo_pulsewidth(ESC_GPIO, 1000)
    time.sleep(2)
    pi.set_servo_pulsewidth(ESC_GPIO, 2000)
    time.sleep(2)
    pi.set_servo_pulsewidth(ESC_GPIO, 1000)
    time.sleep(2)

# Function to set motor speed
def set_speed(speed):
    pulse_width = 1000 + (speed * 10)
    pi.set_servo_pulsewidth(ESC_GPIO, pulse_width)

try:
    arm_esc()
    while True:
        speed = int(input("Enter speed (0-100): "))
        if 0 <= speed <= 100:
            set_speed(speed)
        else:
            print("Invalid speed. Enter a value between 0 and 100.")
except KeyboardInterrupt:
    pi.set_servo_pulsewidth(ESC_GPIO, 0)
    pi.stop()