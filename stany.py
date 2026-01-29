from const import sila_napedowa, sila_oporu, masa_pojazdu
import math, pygame



def idle(a: pygame.math.Vector2, v: pygame.math.Vector2, pos: pygame.math.Vector2, direction: pygame.math.Vector2):
    veh_acc = a
    const_acc = (0-sila_oporu)/masa_pojazdu
    if v.length() > 0:
        dir = v.normalize()
        veh_acc += dir * const_acc
    else:
        veh_acc = pygame.math.Vector2(0,0)
    
    stare_v = pygame.math.Vector2(v.x, v.y)
    v += veh_acc

    if v.length() < 0.1 or v.dot(stare_v) < 0:
        v = pygame.math.Vector2(0,0)
        veh_acc = pygame.math.Vector2(0,0)

    pos.x = pos.x + v.x 
    pos.y = pos.y + v.y 

    return {
        "a": veh_acc,
        "v": v,
        "pos": pos
    }

def const_vel(a: pygame.math.Vector2, v: pygame.math.Vector2, pos: pygame.math.Vector2, direction: pygame.math.Vector2, forward):
    veh_acc = a
    is_forward = forward
    if is_forward == True:
        const_acc = (sila_napedowa - sila_oporu) / masa_pojazdu
    else:
        const_acc = ((-sila_napedowa) - sila_oporu) / masa_pojazdu

    if veh_acc.length() > 0:
        dir = veh_acc.normalize()
        veh_acc -= dir * (0.2 * abs(const_acc))
        if veh_acc.length() < 0.5:
            veh_acc = pygame.math.Vector2(0,0)
    else:
        veh_acc = pygame.math.Vector2(0,0)
    
    v += veh_acc
    pos.x = pos.x + v.x
    pos.y = pos.y + v.y   
    return {
        "a": veh_acc,
        "v": v,
        "pos": pos
    }

#niepotrzebne funkcja const_vel() załatwia ruch od tyłu
#def const_backward(a: pygame.math.Vector2, v: pygame.math.Vector2, pos: pygame.math.Vector2, theta):
    veh_acc = a
    const_acc = (sila_napedowa - sila_oporu) / masa_pojazdu

    if veh_acc.length() > 0:
        dir = veh_acc.normalize()
        veh_acc -= dir * (0.2 * const_acc)
        if veh_acc.length() < 0.5:
            veh_acc = pygame.math.Vector2(0,0)
    else:
        veh_acc = pygame.math.Vector2(0,0)

    v += veh_acc
    pos.x = pos.x - v.x
    pos.y = pos.y - v.y   
    return {
        "a": a,
        "v": v,
        "pos": pos
    }

def steering(v: pygame.math.Vector, direction: pygame.math.Vector2, dir: int):
    #kierunek -1 lewo, 0 prosto, 1 prawo
    rot_speed = 5

    if v.length() < 0.5:
        return{
            "v": v,
            "dir": direction
        }
    else:
        #zmiania skretu przy cofaniu
        if v.dot(direction) < 0:
            dir = -dir
            rot_angle = dir * rot_speed

            v = v.rotate(rot_angle)
            direction = direction.rotate(rot_angle)
        #normalne skrecanie
        else:
            rot_angle = dir * rot_speed

            v = v.rotate(rot_angle)
            direction = direction.rotate(rot_angle)
    
    return {
        "v": v,
        "dir": direction
    }


def accelerate(a: pygame.math.Vector2, v: pygame.math.Vector2, pos: pygame.math.Vector2, direction: pygame.math.Vector2):
    #Przeliczanie fizyki

    current_v = v.length()

    fall_off_coef = 0.2
    torque = 1 / math.sqrt((current_v * fall_off_coef) + 1)

    dyn_acc_const = (sila_napedowa - sila_oporu) / masa_pojazdu

    acc_val = torque * dyn_acc_const

    if direction.length() > 0:
        dir = direction.normalize()
    else:
        dir = pygame.math.Vector2(0,0)
    
    veh_acc = dir * acc_val

    #aktualizacja fizyki

    a += veh_acc

    v += a

    pos.x += v.x
    pos.y += v.y

    return {
        "a": a,
        "v": v,
        "pos": pos
        }

def brake(a: pygame.math.Vector2, v: pygame.math.Vector2, pos: pygame.math.Vector2, direction: pygame.math.Vector2):
    veh_acc = a
    

    brake_acc = abs(2 * (0 - sila_oporu) / masa_pojazdu)

    if v.length() > 0:
        dir = v.normalize()
        veh_acc -= dir * brake_acc
    else:
        v = pygame.math.Vector2(0,0)
    
    stare_v = pygame.math.Vector2(v.x, v.y)
    v += veh_acc

    if v.length() < 0.1 or v.dot(stare_v) < 0:
        veh_acc = pygame.math.Vector2(0,0)
        v = pygame.math.Vector2(0,0)

    pos.x += v.x
    pos.y += v.y
    return {
        "a": veh_acc,
        "v": v,
        "pos": pos
        }