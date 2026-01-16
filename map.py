from const import screen_height, screen_width, szerokosc_miejsca_parkingowego, dlugosc_miejsca_parkingowego, szerokosc_alei 
import pygame

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
        pass
    def generuj_mape(self):
        # Tworzenie granic mapy

        self.przeszkody.append(pygame.Rect(0,0,self.szerokosc,1))                           #sufit
        self.przeszkody.append(pygame.Rect(0,self.wysokosc,self.szerokosc,self.wysokosc))   #podłoga
        self.przeszkody.append(pygame.Rect(0,0,1,self.wysokosc))                            #lewa ściana
        self.przeszkody.append(pygame.Rect(self.szerokosc,0,1,self.wysokosc))               #prawa ściana

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
            
            case 2:
                #parking prostopadły
                pass
    def rysuj_mape(self):
        for przeszkoda in self.przeszkody:
            pygame.draw.rect(pygame.display.get_surface(), "red", przeszkoda, 1)
        if self.typ_parkingu == 1:
            for spot in self.upper_spot:
                pygame.draw.rect(pygame.display.get_surface(), "white", spot, 1)

            for spot in self.lower_spot:
                pygame.draw.rect(pygame.display.get_surface(), "white", spot, 1)

            pygame.draw.rect(pygame.display.get_surface(), "white", self.alley, 1)
        elif self.typ_parkingu == 2:
            pass
        
        
    