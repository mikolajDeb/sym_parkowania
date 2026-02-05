from const import veh_lenght, veh_width, max_steering_angle, axel_spacing, masa_pojazdu, sila_napedowa, sila_oporu
from stany import *
from sensory import *


import pygame

test_time = 10

class Pojazd:
    def __init__(self, x, y, theta, v, can_move):
        # Parametry ruchu pojazdu wzg tyl osi
        
        
        self.can_move = can_move
        self.x = x
        self.y = y
        self.theta = theta
        

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

        self.os_tylna = pygame.math.Vector2(0,0)
        self.srodek_tylu = pygame.math.Vector2(0,0)
        self.srodek_przodu = pygame.math.Vector2(0,0)
        self.fl = pygame.math.Vector2(0,0)
        self.fr = pygame.math.Vector2(0,0)
        self.br = pygame.math.Vector2(0,0)
        self.bl = pygame.math.Vector2(0,0)
        self.rogi = [self.fl, self.fr, self.br, self.bl]


        #Słowniki do aktywowania funkcji stanu
        self.hitbox = {
            "os tylna":self.os_tylna,
            "sr przodu": self.srodek_przodu,
            "sr tylu": self.srodek_tylu,
            "rogi": self.rogi
        }

        self.state = {
            "acc": self.a,
            "vel": self.v,
            "pos": self.pos
        }

        #Test case stuff

        self.Brake_phase = None
        pass
    def step(self):

        #Test case
        
        self.lidar.cast_rays(self.pos.x,self.pos.y)
        
        
        self.lidar.render_LIDAR()
        
        
        if self.v.length() >= 50:
           self.Brake_phase = True 

        if self.Brake_phase == True:
            if self.v.length() > 0:
                self.state = brake(self.a, self.v, self.pos, self.forward_vector, self.can_move)
            else:
                self.state = idle(self.a, self.v, self.pos, self.forward_vector, self.can_move)
        else:
            self.state = accelerate(self.a, self.v, self.pos, self.forward_vector, False,    self.can_move)
        

        #aktualizacja ruchu poajzdu
        self.a = self.state["a"]
        self.v = self.state["v"]
        self.pos = self.state["pos"]
        
        self.hitbox = self.define_vehicle()

        #aktualizacja pozycji pojazdu
        self.os_tylna = self.hitbox["os tylna"]
        self.srodek_przodu = self.hitbox["sr przodu"]
        self.srodek_tylu = self.hitbox["sr tylu"]
        self.rogi = self.hitbox["rogi"]
        
        
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
    