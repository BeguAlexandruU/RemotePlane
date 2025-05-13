import array
import threading
import time

class Sensor:
    def __init__(self, pilot):
        self.pilot = pilot
        
        self.roll = 0
        self.pitch = 0

        print("Sensor initialized")
    
    def run(self):
        print("Sensor running")
        roll_degree = 0

        while True:
            # Simulate sensor data reading
            # ----------------------------------------------------
            time.sleep(0.5)
            print("Plane roll: ", roll_degree) 
            # ----------------------------------------------------

            data = None
            #calculate roll input axis
            if roll_degree >= 0 and roll_degree < 180:
                data = {
                    "axis": "eleron",
                    "value": roll_degree/180
                } 
            elif roll_degree >= 180 and roll_degree < 360:
                data = {
                    "axis": "eleron",
                    "value": (roll_degree - 180) / 180 - 1
                } 
            
            if data:
                self.pilot.setVInput(data)
                # threading.Thread(target=self.send_data_callback, args=(data,), daemon=True).start()
    

            # ----------------------------------------------------
            roll_degree += 10
            if roll_degree >= 360:
                roll_degree = 0
            # ----------------------------------------------------

    def setup(self):
        pass
    
    def cleanup(self):
        pass
    
    def setInput(self):
        
        pass


    
    
