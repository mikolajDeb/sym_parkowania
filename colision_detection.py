import pygame, math

def colision_detection(moving_car, static_upper_car: list, static_lower_car: list):
    mobile_car = moving_car.define_vehicle()

    mobile_corners = mobile_car["rogi"]

    mobile_A = []   #kolejnosc scian: przod prawa tyl lewa
    mobile_B = []
    mobile_C = []

    for i in range(len(mobile_corners)):
        p1 = mobile_corners[i]
        p2 = mobile_corners[(i + 1) % len(mobile_corners)] #ciekawy trick z modulo aby zamknac ksztalt 3+1 = 4 % 4 = 0 wiec wraca do wierzcholka listy cool
        
        A, B, C = get_line_eqation(p1, p2)

        mobile_A.append(A)
        mobile_B.append(B)
        mobile_C.append(C)
    pass

def get_line_eqation(p_1, p_2):
    
    # Wzor ogolny prostej: Ax + By + C = 0

    A = p_2.y - p_1.y
    B = p_2.x - p_1.x
    C = -(A * p_1.x) - (B * p_1.y)

    return A, B, C