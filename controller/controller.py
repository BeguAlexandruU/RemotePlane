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
            # print(f"Axis {event.axis} moved to {event.value}")
            # data = {"type": "axis", "axis": event.axis, "value": event.value}
            filtered_value = self.filter_axis(event.axis, event.value)
            
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
        trim_pitch = 0.0
        trim_roll = 0.0
        
        pitch_max = 45
        pitch_min = -45
        
        roll_max = 45
        roll_min = -45
        
        if axis == 0:
            # Left stick horizontal axis (roll)
            res_roll = roll_min + (value + 1) * (roll_max - roll_min) / 2
            print(f"Filtered roll value: {res_roll}")
            
            
            eleron_right = res_roll
            eleron_left = res_roll
        
        # return res_roll