import time
import pigpio

ESC_GPIO = 12  # GPIO pin connected to ESC's signal wire
pi = pigpio.pi()

print("Disconnect ESC power, then press Enter.")
input()
print("Setting max throttle. Now connect ESC power!")
pi.set_servo_pulsewidth(ESC_GPIO, 2000)
input("After ESC beeps for max throttle, press Enter to set min throttle...")

pi.set_servo_pulsewidth(ESC_GPIO, 1000)
print("Min throttle set. Wait for ESC to finish beeping.")
time.sleep(3)

pi.set_servo_pulsewidth(ESC_GPIO, 0)
print("Calibration done. You can now arm and use the ESC.")

pi.stop()
