from const import veh_lenght, veh_width, max_steering_angle, axel_spacing, masa_pojazdu, sila_napedowa, sila_oporu
from stany import *
from sensory import *

import pygame

test_time = 10

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

        #Obiekty sensoryki
        
        centre_point = self.render_instancja.center
        self.lidar = Lidar(centre_point[0], centre_point[1])
        
        #Parametry zapisu stanu

        self.State_log = []
        self.current_state = ""
        pass
    def step(self):

        # Test case
        
        if self.v >= 10:
            self.v,  self.x, self.y = brake(self.a, self.v, self.x, self.y, self.theta)
            self.current_state = "braking"
        else:
            self.v, self.x, self.y = accelerate(self.a, self.v, self.x, self.y, self.theta)
            self.current_state = "accelerating"

        self.lidar.cast_rays()
        self.lidar.render()

        self.render_instancja.x = self.x
        self.render_instancja.y = self.y

        self.lidar.s_x = self.render_instancja.center[0]
        self.lidar.s_y = self.render_instancja.center[1]

        self.State_log.append(self.current_state)
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

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_theta(self):    
        return self.theta
    
    def get_velocity(self):
        return self.v
    