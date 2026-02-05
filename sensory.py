from const import lidar_range, axel_spacing

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

        self.rays = []

        self.num_of_rays = 144
        self.range = lidar_range

        self.start_vector = pygame.math.Vector2(start_x + (axel_spacing/2), start_y)

        self.base_vector =  pygame.math.Vector2(self.range, 0)

        self.rotaded_vector = pygame.math.Vector2(0,0)
        self.lidar_vector = pygame.math.Vector2(0,0)

        self.angle = 0
        self.angle_between_rays = 360 / self.num_of_rays

        self.intersection_points = []

        #Old implementation

        #self.lidar_num_of_rays = 72
        #self.range = lidar_range

        #self.s_x = start_x
        #self.s_y = start_y
        #self.s_pos = (0,0)
        #self.end_pos = (0,0)
        
        #self.rays = []

        #self.angle = 0
        #self.angle_between_rays = 360 / self.lidar_num_of_rays

        pass
    def cast_rays(self, current_x, current_y):
        self.rays = []

        self.start_vector = pygame.math.Vector2(current_x + (axel_spacing/2), current_y)

        self.rotaded_vector = self.base_vector.rotate(self.angle)

        self.final_lidar_vector = self.start_vector + self.rotaded_vector

        self.angle += self.angle_between_rays

        if self.angle >= 360:
            self.angle = 0

        self.rays.append(self.final_lidar_vector)
        #old implementation
        # Cast rays from the lidar 
        #self.rays = []

        #end_x = self.s_x + self.range * math.cos(math.radians(self.angle))
        #end_y = self.s_y + self.range * math.sin(math.radians(self.angle))

        #self.s_pos = (self.s_x, self.s_y)
        #self.end_pos = (end_x, end_y)

        #self.angle += self.angle_between_rays

        #if self.angle >= 360:
            #self.angle = 0

        #self.rays.append((self.s_pos, self.end_pos))
        pass
    def render_LIDAR(self):
        for ray in self.rays:
            pygame.draw.line(pygame.display.get_surface(), "blue", self.start_vector, ray, 2)
        pass

# Chceck for obstacle for lidar

    

    def check_intersection_LIDAR(self, ray_start, ray_end, obstacle):
        #rozpakowanie wsporzednych
        intersections_in_this_obstacle = []

        x1, y1 = ray_start
        x2, y2 = ray_end

        for i in range(len(obstacle["rogi"])):
            x3, y3 = obstacle["rogi"][i]
            x4, y4 = obstacle["rogi"][(i + 1) % len(obstacle["rogi"])]

            denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
            
            if denom == 0:
                continue  # Linie sa rownolegle
            
            t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denom
            u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / denom

            if 0 <= t <= 1 and 0 <= u <= 1:
                intersection_x = x1 + t * (x2 - x1)
                intersection_y = y1 + t * (y2 - y1)
                point =  pygame.math.Vector2(intersection_x, intersection_y)
                intersections_in_this_obstacle.append(point)
        
        return intersections_in_this_obstacle
    
    def check_all_obstacle_intersections_LIDAR(self, upper_obstacles: list, lower_obstacles: list):
        all_obstacles = upper_obstacles + lower_obstacles

        intersection_point = pygame.math.Vector2(0,0)

        current_ray_hits = []

        #self.intersection_points = []

        for obstacle in all_obstacles:
            intersection_point = self.check_intersection_LIDAR(self.start_vector, self.final_lidar_vector, obstacle)
            
            if intersection_point:
                current_ray_hits.extend(intersection_point)
        
        if current_ray_hits:
            closest_point = None
            min_distance = float('inf')

            for point in current_ray_hits:
                distance = self.start_vector.distance_to(point)

                if distance < min_distance:
                    min_distance = distance
                    closest_point = point
            
            if closest_point is not None:
                self.intersection_points.append(closest_point)

                #zabezpieczenie pamieci «eby lista za duza sie nie zrobila
                if len(self.intersection_points) > 1000:
                    self.intersection_points.pop(0)
        
        pass

    def render_intersections(self):
        for point in self.intersection_points:
            
                pygame.draw.circle(pygame.display.get_surface(), "yellow", (point.x, point.y), 5)
        pass
class Ultra_sonic(Sensory):
    def __init__(self):
        super().__init__()
        pass