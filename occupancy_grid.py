from const import grid_square_side_length, screen_height, screen_width

import pygame, math

class Recognized_Car:
    def __init__(self):
        self.horizontal_squares = []
        self.vertial_squares = []
        pass

class Grid_square:
    def __init__(self, x, y):
        #stale

        self.__grid_square_side_length = grid_square_side_length
        

        self.right_v = pygame.math.Vector2(1, 0)
        self.down_v = pygame.math.Vector2(0, 1)

        #Parametry gridu

        self.start_x = x
        self.start_y = y

        self.square_start_pos = pygame.math.Vector2(self.start_x, self.start_y)

        #Lists of lidar hits

        self.hits_in_squares = []

        #Hitbox

        self.tr = pygame.math.Vector2(0,0)
        self.dr = pygame.math.Vector2(0,0)
        self.dl = pygame.math.Vector2(0,0)
        self.tl = pygame.math.Vector2(0,0)
        self.corners = [self.tr, self.dr, self.dl, self.tl]

        #grid color

        self.free_colour = "grey"
        self.occupied_colour = "blue"
        self.is_free = True

    def create_grid_square(self):

        start_pos = pygame.math.Vector2(self.square_start_pos.x, self.square_start_pos.y)

        top_l = start_pos
        top_r = start_pos + (self.right_v * self.__grid_square_side_length)
        down_l = start_pos + (self.down_v * self.__grid_square_side_length)
        down_r = top_r + (self.down_v * self.__grid_square_side_length)

        self.corners = [top_r, down_r, down_l, top_l]

        return self.corners
        

class Occupancy_grid:
    def __init__(self):

        #stale

        self.__grid_square_side_length = grid_square_side_length
        self.__number_horizontal_squares = int(screen_width / self.__grid_square_side_length)
        self.__number_vertical_squares = int(screen_height / self.__grid_square_side_length)

        self.right_v = pygame.math.Vector2(1, 0)
        self.down_v = pygame.math.Vector2(0, 1)

        #Parametry gridu

        self.start_x = 0
        self.start_y = 0

        self.square_start_pos = pygame.math.Vector2(self.start_x, self.start_y)
        
        #Grid lists

        self.grid = []
        self.occupied_squares = []

        

    

        #for hit in lidar_hits:
            #if hit.x >= top_l.x and hit.x <= top_r.x and hit.y >= top_l.y and hit.y <= down_l.y:
                #self.hits_in_squares.append(hit)
            #else:
                #continue

            #if self.hits_in_squares.len == 0:
                #self.hits_in_squares = []

        

    def counstruct_grid(self):
        original_x = self.square_start_pos.x
        for row in range(self.__number_vertical_squares):
            current_row = []

            for square in range(self.__number_horizontal_squares):
                
                square = Grid_square(self.square_start_pos.x, self.square_start_pos.y)
                square.create_grid_square()
                
                current_row.append(square)

                self.square_start_pos.x += self.__grid_square_side_length

                #self.square_start_pos.x = self.square_start_pos.x + (self.right_v * self.__grid_square_side_length)
            
            self.grid.append(current_row)

            self.square_start_pos.x = original_x
            #self.square_start_pos.y = self.square_start_pos.y + (self.down_v + self.__grid_square_side_length)
            self.square_start_pos.y += self.__grid_square_side_length

        pass

    def find_occupied_grid_squares(self, hit_points: list):
        for hit in hit_points:
            current_point = hit
            grid_pos_x = int(current_point.x // self.__grid_square_side_length)
            grid_pos_y = int(current_point.y // self.__grid_square_side_length)


            current_square = self.grid[grid_pos_y][grid_pos_x]

            if current_square is False:
                continue
            else:
                current_square.is_free = False

            current_square.hits_in_squares.append(current_point)
            self.occupied_squares.append(current_square)

            pass
        pass
    
    def recognize_cars(self):
        recognized_cars = []

        pass 
    
    def find_verticals(self):
        pass

    def find_horizontals(self):
        #sortowanie na kwadraty na dole ekranu i gorze ekranu
        upper_squares = []
        lower_squares = []

        for square in self.occupied_squares:
            if square.tl.y > (screen_height / 2):
                lower_squares.append(square)
            else:
                upper_squares.append(square)
        
        #separowanie kwadratow ktore sa w linii poziomej

        max_tl = float('-inf')
        min_tl = float('inf')
        lower_inline_squares = []
        upper_inline_squares = []

        for square in lower_squares:
            if square.tl.y < min_tl:
                min_tl = square.tl.y
            
            if square.tl.y == min_tl:
                lower_inline_squares.append(square)

        for square in upper_squares:
            if square.tl.y > max_tl:
                max_tl = square.tl.y
            
            if square.tl.y == max_tl:
                upper_inline_squares.append(square)

        #rozdzielanie listy wspoliniowych kwadratow na te nalezace do oddzielnych pojazdow

        single_car = Recognized_Car()

        for i in range(1, len(lower_inline_squares)):
            distance = lower_inline_squares[i].tl.x - lower_inline_squares[i-1].tl.x
            if distance < (4 * self.__grid_square_side_length):
                single_car.horizontal_squares.append(lower_inline_squares[i-1])

        for i in range(1, len(upper_inline_squares)):
            distance = upper_inline_squares[i].tl.x - upper_inline_squares[i-1].tl.x
            if distance < (4 * self.__grid_square_side_length):
                single_car.horizontal_squares.append(upper_inline_squares[i-1])
                
        pass


    def render_grid(self):
        surface = pygame.display.get_surface()

        for row in self.grid:
            for square in row: 
                
                
                if square.is_free:
                    color = square.free_colour
                    width = 1 
                else:
                    color = square.occupied_colour
                    width = 3 

                
                pygame.draw.polygon(surface, color, square.corners, width)