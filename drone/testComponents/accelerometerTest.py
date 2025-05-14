import mpu6050
import time
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


# Create a new Mpu6050 object
mpu6050 = mpu6050.mpu6050(0x68)

# Define a function to read the sensor data
def read_sensor_data():
    # Read the accelerometer values
    accelerometer_data = mpu6050.get_accel_data()

    # Read the gyroscope values
    gyroscope_data = mpu6050.get_gyro_data()

    # Read temp
    temperature = mpu6050.get_temp()

    return accelerometer_data, gyroscope_data, temperature

# Start a while loop to continuously read the sensor data
while True:

    # Read the sensor data
    accelerometer_data, gyroscope_data, temperature = read_sensor_data()

    # Print the sensor data
    print("Accelerometer data: x={:.2f}, y={:.2f}, z={:.2f}".format(
    accelerometer_data['x'], accelerometer_data['y'], accelerometer_data['z']))
    print("Gyroscope data: x={:.2f}, y={:.2f}, z={:.2f}".format(
        gyroscope_data['x'], gyroscope_data['y'], gyroscope_data['z']))
    print("Temp: {:.2f}°C".format(temperature))

    # print("Accelerometer data:", accelerometer_data)
    # print("Gyroscope data:", gyroscope_data)
    # print("Temp:", temperature)

    # Wait for 1 second
    time.sleep(0.1)

