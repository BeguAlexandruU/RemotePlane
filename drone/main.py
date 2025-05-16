import pilot
import server
# from sensor import Sensor
from concurrent.futures import ThreadPoolExecutor

if __name__ == "__main__":
    
    pilot.setup()
    server.setup()
    
    # sensor = Sensor(pilot)
    

    # Use ThreadPoolExecutor to manage threads
    with ThreadPoolExecutor(max_workers=2) as executor:
        # Submit tasks to the executor
        # executor.submit(sensor.run)
        executor.submit(server.run)

    print("Program terminated.")
