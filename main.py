from const import screen_width, screen_height
from map import Map
from obiekt_fiz import Pojazd
from sensory import *
from parking_place import *
from occupancy_grid import *

import pygame, sys

typ = 1
intersection_points = []

def main():
    print("Startuje symulator parkowania pojazdów.")
    
    

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    
    
    
    Clock = pygame.time.Clock()
    dt = 0
    start_x = 50
    start_y = (screen_height/2)
    Poj = Pojazd(start_x, start_y , 0, 0, True)
    

    Mapa = Map(typ)
    Mapa.generuj_mape()

    Grid = Occupancy_grid()
    Grid.counstruct_grid()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        screen.fill("black")

        #Mapa = Map(typ)
        #Mapa.generuj_mape()
        Mapa.rysuj_mape()   

        

        Poj.step()
        intersection_points = Poj.lidar.check_all_obstacle_intersections_LIDAR(Mapa.lower_parked_cars_hitbox, Mapa.upper_parked_cars_hitbox)
        Poj.render()
        Poj.lidar.render_intersections()

        #place = find_place(Poj.lidar.intersection_points, Poj)
        #parking_space_render(place)

        Grid.find_occupied_grid_squares(intersection_points)     
        Grid.render_grid()
        
        pygame.display.flip()

        Time_Tick = Clock.tick(60)
        dt = Time_Tick / 1000
    


if __name__ == "__main__":
       
    main()
