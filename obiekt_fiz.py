from const import veh_lenght, veh_width, max_steering_angle, axel_spacing, masa_pojazdu, sila_napedowa, sila_oporu
from stany import *

import pygame

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

        #parametry renderu pojazdu

        self.color_movable = "green"
        self.color_immovable = "red"
        self.render_instancja = pygame.Rect(self.x, self.y, self.veh_lenght, self.veh_width)    

        pass
    def step(self):
        # Test case
        procedury = [idle, accelerate, brake, const_forward, const_backward]
        for procedura in procedury:
            procedura(self.a, self.v, self.x, self.y, self.theta)
        pass
    def log(self):
        pass
    def reset(self):
        pass
    def render(self):
        if self.can_move:
            pygame.draw.rect(pygame.display.get_surface(), self.color_movable, self.render_instancja)
        else:
            pygame.draw.rect(pygame.display.get_surface(), self.color_immovable, self.render_instancja)
        pass