from calendar import c
from re import S
import mpu6050
import time
import os
import math
import pilot

imuSensor = None

roll = None
pitch = None
speed = None

def setup():
    global imuSensor, roll, pitch, speed
    # Initialize the MPU6050 sensor
    imuSensor = mpu6050.mpu6050(0x68)
    
    roll = 0
    pitch = 0
    speed = 0
    
    print("IMU sensor initialized")

def run():
    global imuSensor, roll, pitch, speed
    if imuSensor is None:
        print("MPU6050 not initialized. Call setup() first.")
        return
    
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
        # print("Accelerometer data: x={:.2f}, y={:.2f}, z={:.2f}".format(ax, ay, az))
        # print("Gyroscope data: x={:.2f}, y={:.2f}, z={:.2f}".format(
        #     gyroscope_data['x'], gyroscope_data['y'], gyroscope_data['z']))
        # print("Temp: {:.2f}°C".format(temperature))
        # print("Pitch: {:.2f}°, Roll: {:.2f}°".format(pitch, roll))
        # print("Relative speed (|a|): {:.2f} m/s²".format(speed))
        # print("-" * 40)
        
        data = None
        #calculate roll input axis
        data = {
            "axis": "eleron",
            "value": roll / -180
        }
        
        if data:
            pilot.setVInput(data)
        
        
        time.sleep(0.1)

def read_sensor_data():
    global imuSensor
    if imuSensor is None:
        print("MPU6050 not initialized. Call setup() first.")
        return None, None, None
    accelerometer_data = imuSensor.get_accel_data()
    gyroscope_data = imuSensor.get_gyro_data()
    temperature = imuSensor.get_temp()
    return accelerometer_data, gyroscope_data, temperature


