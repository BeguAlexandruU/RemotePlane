from pilot import Pilot
from sensor import Sensor
from server import Server
from concurrent.futures import ThreadPoolExecutor

if __name__ == "__main__":
    pilot = Pilot()
    sensor = Sensor(pilot)
    server = Server(pilot)

    # Use ThreadPoolExecutor to manage threads
    with ThreadPoolExecutor(max_workers=2) as executor:
        # Submit tasks to the executor
        # executor.submit(sensor.run)
        executor.submit(server.run)

    print("Program terminated.")
