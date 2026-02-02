from const import screen_height, screen_width, szerokosc_miejsca_parkingowego, dlugosc_miejsca_parkingowego, szerokosc_alei, axel_spacing
from obiekt_fiz import Pojazd
import pygame, random

vector = pygame.math.Vector2(0, 0)

class Map:
    def __init__(self, typ_parkingu):
        self.szerokosc = screen_width
        self.wysokosc = screen_height
        self.cel = None
        self.przeszkody = []

        self.szerokosc_miejsca_parkingowego = szerokosc_miejsca_parkingowego
        self.dlugosc_miejsca_parkingowego = dlugosc_miejsca_parkingowego

        self.szerokosc_alei = szerokosc_alei  

        self.typ_parkingu = typ_parkingu

        self.alley = None
        self.upper_spot = []
        self.lower_spot = []

        self.upper_parked_cars = []
        self.lower_parked_cars = []

        self.start_up = vector
        self.end_up = vector

        self.start_down = vector
        self.end_down = vector

        self.start_left = vector
        self.end_left = vector

        self.start_right = vector
        self.end_right = vector
        pass
    def generuj_mape(self):
        
        # Tworzenie granic mapy

        #gora
        self.start_up = pygame.math.Vector2(0,0)
        self.end_up = pygame.math.Vector2(self.szerokosc,0)

        #dol
        self.start_down = pygame.math.Vector2(0,self.wysokosc)
        self.end_down = pygame.math.Vector2(self.szerokosc,self.wysokosc)

        #lewa
        self.start_left = pygame.math.Vector2(0,0)
        self.end_left = pygame.math.Vector2(0,self.wysokosc)

        #prawa
        self.start_right = pygame.math.Vector2(self.szerokosc,0)
        self.end_right = pygame.math.Vector2(self.szerokosc,self.wysokosc)

        #self.przeszkody.append(pygame.Rect(0,0,self.szerokosc,1))                           #sufit
        #self.przeszkody.append(pygame.Rect(0,self.wysokosc,self.szerokosc,self.wysokosc))   #podłoga
        #self.przeszkody.append(pygame.Rect(0,0,1,self.wysokosc))                            #lewa ściana
        #self.przeszkody.append(pygame.Rect(self.szerokosc,0,1,self.wysokosc))               #prawa ściana

        #tworzenie miejsc parkingowych i alei


        match self.typ_parkingu:
            case 1:
                #parking równoległy
                x_start = -self.dlugosc_miejsca_parkingowego
                y_start = 0
                

                self.alley = pygame.Rect(x_start + self.dlugosc_miejsca_parkingowego, y_start + self.szerokosc_miejsca_parkingowego, self.szerokosc, y_start + self.szerokosc_alei)
                for i in range(3):
                    self.upper_spot.append(pygame.Rect(x_start + self.dlugosc_miejsca_parkingowego, y_start, self.dlugosc_miejsca_parkingowego, self.szerokosc_miejsca_parkingowego))
                    self.lower_spot.append(pygame.Rect(x_start + self.dlugosc_miejsca_parkingowego, y_start + self.szerokosc_miejsca_parkingowego + self.szerokosc_alei, self.dlugosc_miejsca_parkingowego, self.szerokosc_miejsca_parkingowego))

                    x_start += self.dlugosc_miejsca_parkingowego
                pass

                for spot in self.upper_spot:

                    is_occupied = random.randint(0, 1)
                    spot_center_x, spot_center_y = spot.center

                    if is_occupied == 1:

                        car = Pojazd(spot_center_x - (axel_spacing/2), spot_center_y, 0, 0, False)
                        car.define_vehicle()
                        self.upper_parked_cars.append(car)
                    elif is_occupied == 0:
                        pass
                    
                for spot in self.lower_spot:

                    is_occupied = random.randint(0, 1)
                    spot_center_x, spot_center_y = spot.center

                    if is_occupied == 1:

                        car = Pojazd(spot_center_x - (axel_spacing/2), spot_center_y, 0, 0, False)
                        self.lower_parked_cars.append(car)
                    elif is_occupied == 0:
                        pass
                    
            
            case 2:
                #parking prostopadły
                pass
    def rysuj_mape(self):
        #generowanie granic mapy
        
        pygame.draw.line(pygame.display.get_surface(), "red", self.start_up, self.end_up, 20)
        pygame.draw.line(pygame.display.get_surface(), "red", self.start_down, self.end_down, 20)
        pygame.draw.line(pygame.display.get_surface(), "red", self.start_left, self.end_left, 20)
        pygame.draw.line(pygame.display.get_surface(), "red", self.start_right, self.end_right, 20)

        for przeszkoda in self.przeszkody:
            pygame.draw.rect(pygame.display.get_surface(), "red", przeszkoda, 1)
        if self.typ_parkingu == 1:
            for spot in self.upper_spot:
                pygame.draw.rect(pygame.display.get_surface(), "white", spot, 1)
            

            for spot in self.lower_spot:
                pygame.draw.rect(pygame.display.get_surface(), "white", spot, 1)
                

            pygame.draw.rect(pygame.display.get_surface(), "white", self.alley, 1)

            for car in self.upper_parked_cars:
                    car.render()
            
            for car in self.lower_parked_cars:
                    car.render()
        elif self.typ_parkingu == 2:
            pass
        
        
    