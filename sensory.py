from const import lidar_range

import pygame, math

class Sensory:
    def __init__(self, x, y):
        # Parametry podstawowe
        self.range = 0
        
        # Parametry prcesowe
        self.x = x
        self.y = y  

        pass
class Lidar(Sensory):
    def __init__(self, start_x, start_y):
        super().__init__(start_x, start_y)
        self.lidar_num_of_rays = 72
        self.range = lidar_range

        self.s_x = start_x
        self.s_y = start_y
        self.s_pos = (0,0)
        self.end_pos = (0,0)
        
        self.rays = []

        self.angle = 0
        self.angle_between_rays = 360 / self.lidar_num_of_rays

        pass
    def cast_rays(self):
        # Cast rays from the lidar 
        self.rays = []

        end_x = self.s_x + self.range * math.cos(math.radians(self.angle))
        end_y = self.s_y + self.range * math.sin(math.radians(self.angle))

        self.s_pos = (self.s_x, self.s_y)
        self.end_pos = (end_x, end_y)

        self.angle += self.angle_between_rays

        if self.angle >= 360:
            self.angle = 0

        self.rays.append((self.s_pos, self.end_pos))
        pass

    def check_obstacle(self):
        pass

    def render(self):
        for ray in self.rays:
            pygame.draw.line(pygame.display.get_surface(), "blue", ray[0], ray[1], 2)
        pass
class Ultra_sonic(Sensory):
    def __init__(self):
        super().__init__()
        pass