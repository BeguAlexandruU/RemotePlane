from mpu9250_jmdev.registers import *
from mpu9250_jmdev.mpu_9250 import MPU9250
import time
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

mpu = MPU9250(
    address_ak=AK8963_ADDRESS,
    address_mpu=MPU9050_ADDRESS_68,  # sau MPU9050_ADDRESS_69 dacă AD0 e conectat la 3.3V
    bus=1,
    gfs=GFS_250, afs=AFS_2G, mfs=AK8963_BIT_16, mode=AK8963_MODE_C100HZ
)

mpu.calibrate()       # Calibrare (necesară o singură dată)
mpu.configure()       # Aplică setările

while True:
    ax, ay, az = mpu.readAccelerometerMaster()
    gx, gy, gz = mpu.readGyroscopeMaster()
    mx, my, mz = mpu.readMagnetometerMaster()
    
    clear_terminal()
    print(f"Accel: {ax:.2f}, {ay:.2f}, {az:.2f} g")
    print(f"Gyro : {gx:.2f}, {gy:.2f}, {gz:.2f} °/s")
    print(f"Mag  : {mx:.2f}, {my:.2f}, {mz:.2f} uT")
    print("-----------")
    time.sleep(0.5)
