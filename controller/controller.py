import pygame
import threading

class Controller:
    def __init__(self, send_data_callback=None):
        self.pygame = pygame
        self.joystick = None
        self.running = True
        self.send_data_callback = send_data_callback

        # Mapping for joystick axes and buttons
        self.eleronAxis = 0
        self.elevatorAxis = 1
        self.motorAxis = 3

        self.manualModeButton = 0
        self.virtualModeButton = 3
        self.mixedModeButton = 1
        
        self.trimElevatorIncreaseButton = 5
        self.trimElevatorDecreaseButton = 4
    
    # initialize the joystick
    def setup(self): 
        pygame.init()
        pygame.joystick.init()
        if pygame.joystick.get_count() > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
            print(f"Joystick initialized: {self.joystick.get_name()}")
        else:
            print("No joystick found.")
            
    # read the joystick input
    def run(self):
        while self.running:
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    self.running = False
                else:
                    self.handle_event(event)

        self.pygame.quit()

    # handle the joystick events
    def handle_event(self, event):
        data = None
        
        if event.type == pygame.JOYAXISMOTION:
            print(f"Axis {event.axis} moved to {event.value}")
            if event.axis == self.eleronAxis:
                data = {
                    "type": "axis",
                    "axis": "eleron",
                    "value": event.value
                }
            elif event.axis == self.elevatorAxis:
                data = {
                    "type": "axis",
                    "axis": "elevator",
                    "value": event.value
                }
            elif event.axis == self.motorAxis:
                data = {
                    "type": "axis",
                    "axis": "motor",
                    "value": event.value
                }
            
        elif event.type == pygame.JOYBUTTONDOWN:
            print(f"Button {event.button} pressed")
            if event.button == self.manualModeButton:
                data = {
                    "type": "button",
                    "button": "mode",
                    "value": "manual",
                }
            elif event.button == self.virtualModeButton:
                data = {
                    "type": "button",
                    "button": "mode",
                    "value": "virtual",
                }
            elif event.button == self.mixedModeButton:
                data = {
                    "type": "button",
                    "button": "mode",
                    "value": "mixed",
                }
            elif event.button == self.trimElevatorIncreaseButton:
                data = {
                    "type": "button",
                    "button": "trimElevator",
                    "value": 10,
                }
            elif event.button == self.trimElevatorIncreaseButton:
                data = {
                    "type": "button",
                    "button": "trimElevator",
                    "value": -10,
                }
        # elif event.type == pygame.JOYBUTTONUP:
        #     print(f"Button {event.button} released")
        # elif event.type == pygame.JOYHATMOTION:
        #     print(f"Hat {event.hat} moved to {event.value}")
            
        if data:
            threading.Thread(target=self.send_data_callback, args=(data,), daemon=True).start()
    