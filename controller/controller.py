import pygame
import threading

class Controller:
    def __init__(self, send_data_callback=None):
        self.joystick = None
        self.pygame = pygame  # Store pygame reference for event handling
        self.running = True
        self.send_data_callback = send_data_callback
        


    def setup(self):
        pygame.init()
        pygame.joystick.init()
        if pygame.joystick.get_count() > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
            print(f"Joystick initialized: {self.joystick.get_name()}")
        else:
            print("No joystick found.")
    
    def run(self):
        while self.running:
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    self.running = False
                else:
                    self.handle_event(event)

        self.pygame.quit()

    def handle_event(self, event):
        data = None
        
        if event.type == pygame.JOYAXISMOTION:
            print(f"Axis {event.axis} moved to {event.value}")
            data = {"type": "axis", "axis": event.axis, "value": event.value}
            # filtered_value = self.filter_axis(event.axis, event.value)
            
        elif event.type == pygame.JOYBUTTONDOWN:
            print(f"Button {event.button} pressed")
        elif event.type == pygame.JOYBUTTONUP:
            print(f"Button {event.button} released")
        elif event.type == pygame.JOYHATMOTION:
            print(f"Hat {event.hat} moved to {event.value}")
            
        if data:
            threading.Thread(target=self.send_data_callback, args=(data,), daemon=True).start()
    
    def filter_axis(self, axis, value):
        # Implement any filtering logic here
        trim_pitch = 10
        trim_roll = 10
        
        elevator_max = 45
        elevator_min = -70
        
        eleron_max = 45
        eleron_min = -70
        
        if axis == 0:
            # Horizontal axis (roll)
            
            if value >= 0:  # Stick right
                right_eleron = value * eleron_max  # 0 to max
                left_eleron = value * eleron_min  # 0 to min
            else:  # Stick left
                right_eleron = -value * eleron_min  # min to 0
                left_eleron = -value * eleron_max  # max to 0
            
            print(f"Left eleron: {left_eleron} \t Right eleron: {right_eleron}")
        
        if axis == 1:
            # Vertical axis (pitch)
            
            if value >= 0:  # Stick right
                elevator = (value) * elevator_min 
            else:  # Stick left
                elevator = -value * elevator_max  
            
            # Apply trim to adjust neutral position
            elevator = elevator + (trim_pitch)
            
            # Ensure value stays within allowed range
            elevator = max(elevator_min, min(elevator_max, elevator))
            
            print(f"Elevator: {elevator}")
            
    