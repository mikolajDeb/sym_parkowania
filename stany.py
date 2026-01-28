from const import sila_napedowa, sila_oporu, masa_pojazdu
import math, pygame



def idle(a: pygame.math.Vector2, v: pygame.math.Vector2, pos: pygame.math.Vector2, theta):
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

def const_vel(a: pygame.math.Vector2, v: pygame.math.Vector2, pos: pygame.math.Vector2, theta, forward):
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
        "a": a,
        "v": v,
        "pos": pos
    }

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

def steering_left(theta):
    theta -= 10
    return theta

def steering_right(theta):
    theta += 10
    return theta

def accelerate(a , v, x, y, theta):
    v += a
    x = x + v * math.cos(math.radians(theta))
    y = y + v * math.sin(math.radians(theta))
    return v, x, y

def brake(a, v, x, y, theta):
    v -= 2 * a
    x = x + v * math.cos(math.radians(theta))
    y = y + v * math.sin(math.radians(theta))
    return v, x, y