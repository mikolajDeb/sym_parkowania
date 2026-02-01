from const import veh_lenght, veh_width, max_steering_angle, axel_spacing, masa_pojazdu, sila_napedowa, sila_oporu
from stany import *
from sensory import *

import pygame

test_time = 10

class Pojazd:
    def __init__(self, x, y, theta, v, can_move):
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

        

        #parametry renderu pojazdu

        self.color_movable = "green"
        self.color_immovable = "red"
        #self.render_instancja = pygame.Rect(self.x, self.y, self.veh_lenght, self.veh_width)    

        #Obiekty sensoryki
        
        #centre_point = self.render_instancja.center
        self.lidar = Lidar(self.x, self.y)
        
        #Parametry zapisu stanu

        self.State_log = []
        self.current_state = ""

        #Vectory

        self.pos = pygame.math.Vector2(self.x, self.y)
        self.a = pygame.math.Vector2(0,0)
        self.v = pygame.math.Vector2(0,0)
        self.forward_vector = pygame.math.Vector2(1,0)
        self.right_vector = pygame.math.Vector2(0,1)

        pass
    def step(self):

        # Old Test case
        # Will re write the lidar secuence couse it's probably wrong for a use case 
        
        #if self.v >= 10:
            #self.v,  self.x, self.y = brake(self.a, self.v, self.x, self.y, self.theta)
            #self.current_state = "braking"
        #else:
            #self.v, self.x, self.y = accelerate(self.a, self.v, self.x, self.y, self.theta)
            #self.current_state = "accelerating"

        self.lidar.cast_rays()
        self.lidar.render()

        #self.render_instancja.x = self.x
        #self.render_instancja.y = self.y

        self.lidar.s_x = self.x + (axel_spacing / 2)
        self.lidar.s_y = self.y 

        self.State_log.append(self.current_state)
        pass
    def log(self):
        pass
    def reset(self):
        pass
    
    def define_vehicle(self):
        
        
            
        forward = self.forward_vector.rotate(self.theta)
        right = self.right_vector.rotate(self.theta)
            
        centre_back_axel_pos = self.pos
            
            
        mid_front_pos = centre_back_axel_pos + (self.L + 50) * forward

        mid_back_pos = centre_back_axel_pos - 50 * forward

        fr = mid_front_pos + right * (veh_width / 2)
        fl = mid_front_pos - right * (veh_width / 2)

        br = mid_back_pos + right * (veh_width / 2)
        bl = mid_back_pos - right * (veh_width / 2)
            
        return{
            "os tylna": centre_back_axel_pos,
            "sr przodu": mid_front_pos,
            "sr tylu": mid_back_pos,
            "rogi": [fl, fr, br, bl]
        }
        
    pass

    def render(self):
        car = self.define_vehicle()
        if self.can_move == True:
            pygame.draw.polygon(pygame.display.get_surface(), self.color_movable, car["rogi"])

        else: 
            pygame.draw.polygon(pygame.display.get_surface(), self.color_immovable, car["rogi"])

    pass

    def collision_detection(self):
        
        pass
    