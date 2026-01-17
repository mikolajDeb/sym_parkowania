from const import screen_width, screen_height
from map import Map
from obiekt_fiz import Pojazd

import pygame, sys

typ = 1


def main():
    print("Startuje symulator parkowania pojazdów.")
    
    

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    
    
    
    Clock = pygame.time.Clock()
    dt = 0
    Poj = Pojazd(dt, 0, screen_height/2, 0, 0, True)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        screen.fill("black")

        Mapa = Map(typ)
        Mapa.generuj_mape()
        Mapa.rysuj_mape()   

        
        Poj.step()
        Poj.render()

        pygame.display.flip()

        Time_Tick = Clock.tick(60)
        dt = Time_Tick / 1000


if __name__ == "__main__":
       
    main()
