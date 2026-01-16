from const import veh_lenght, veh_width, max_steering_angle, axel_spacing, masa_pojazdu, sila_napedowa, sila_oporu
from stany import stany
class Pojazd:
    def __init__(self, dt, x, y, theta, v, can_move):
        # Parametry ruchu pojazdu wzg tyl osi
        
        self.a = (sila_napedowa - sila_oporu)/masa_pojazdu
        self.can_move = can_move
        self.x = x
        self.y = y
        self.theta = theta
        self.v = v

        # Parametry fizyczne pojazdu

        self.L = axel_spacing
        self.max_steering_angle = max_steering_angle  # stopnie
        self.veh_lenght = veh_lenght
        self.veh_width = veh_width

        #Parametry procesowe

        self.dt = dt   

        pass
    def step(self):
        pass
    def log(self):
        pass
    def reset(self):
        pass
    def render(self):
        pass