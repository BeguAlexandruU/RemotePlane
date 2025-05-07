from drone.pilot import Pilot
from server import Server

if __name__ == "__main__":
    pilot = Pilot()

    server = Server(pilot)
    # server.run()