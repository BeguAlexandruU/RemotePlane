from mpu9250_jmdev.registers import *
from mpu9250_jmdev.mpu_9250 import MPU9250
import time
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

mpu = MPU9250(
    address_mpu_master=MPU9050_ADDRESS_68,
    bus=1,
    gfs=GFS_1000,
    afs=AFS_8G
)
mpu.configure()

while True:
    accel_data = mpu.readAccelerometerMaster()
    gyro_data = mpu.readGyroscopeMaster()
    print("Accelerometer:", accel_data)
    print("Gyroscope:", gyro_data)
    time.sleep(0.5)

# mpu = MPU9250(
#     address_ak=AK8963_ADDRESS,
#     address=MPU9050_ADDRESS_68,
#     # address_mpu_master=MPU9050_ADDRESS_68,  # In case the MPU9250 is connected to another I2C device
#     # address_mpu_slave=None,
#     bus=1,
#     gfs=GFS_1000,
#     afs=AFS_8G,
#     mfs=AK8963_BIT_16,
#     mode=AK8963_MODE_C100HZ
# )

# try:
#     mpu.calibrate()
# except ZeroDivisionError:
#     print("Calibration failed: Magnetometer not detected or not returning data.")
#     # Optionally, skip calibration or exit
# mpu.configure()       # Aplică setările

# while True:
    
#     # Read the accelerometer, gyroscope, and magnetometer values
#     accel_data = mpu.readAccelerometerMaster()
#     gyro_data = mpu.readGyroscopeMaster()
#     mag_data = mpu.readMagnetometerMaster()

#     # Print the sensor values
#     # clear_terminal()
#     print("Accelerometer:", accel_data)
#     print("Gyroscope:", gyro_data)
#     print("Magnetometer:", mag_data)

#     # ax, ay, az = mpu.readAccelerometerMaster()
#     # gx, gy, gz = mpu.readGyroscopeMaster()
#     # mx, my, mz = mpu.readMagnetometerMaster()

#     # clear_terminal()
#     # print(f"Accel: {ax:.2f}, {ay:.2f}, {az:.2f} g")
#     # print(f"Gyro : {gx:.2f}, {gy:.2f}, {gz:.2f} °/s")
#     # print(f"Mag  : {mx:.2f}, {my:.2f}, {mz:.2f} uT")
#     # print("-----------")
#     time.sleep(0.5)
