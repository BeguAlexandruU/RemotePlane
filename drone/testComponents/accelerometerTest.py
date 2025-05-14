from calendar import c
import mpu6050
import time
import os
import math

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Create a new Mpu6050 object
mpu6050 = mpu6050.mpu6050(0x68)

def read_sensor_data():
    accelerometer_data = mpu6050.get_accel_data()
    gyroscope_data = mpu6050.get_gyro_data()
    temperature = mpu6050.get_temp()
    return accelerometer_data, gyroscope_data, temperature

while True:
    accelerometer_data, gyroscope_data, temperature = read_sensor_data()

    # Calculate pitch and roll in degrees
    ax = accelerometer_data['x']
    ay = accelerometer_data['y']
    az = accelerometer_data['z']

    pitch = math.degrees(math.atan2(ay, math.sqrt(ax**2 + az**2)))
    roll = math.degrees(math.atan2(-ax, az))

    # Calculate "speed" as the magnitude of acceleration vector
    speed = math.sqrt(ax**2 + ay**2 + az**2)
    clear_terminal()
    print("Accelerometer data: x={:.2f}, y={:.2f}, z={:.2f}".format(ax, ay, az))
    print("Gyroscope data: x={:.2f}, y={:.2f}, z={:.2f}".format(
        gyroscope_data['x'], gyroscope_data['y'], gyroscope_data['z']))
    print("Temp: {:.2f}°C".format(temperature))
    print("Pitch: {:.2f}°, Roll: {:.2f}°".format(pitch, roll))
    print("Relative speed (|a|): {:.2f} m/s²".format(speed))
    print("-" * 40)

    time.sleep(0.1)