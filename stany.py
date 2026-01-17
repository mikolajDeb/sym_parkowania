from const import sila_napedowa, sila_oporu, masa_pojazdu
import math



def idle(a , v, x, y, theta):
    a = (0 - sila_oporu) / masa_pojazdu
    v += a
    x = x + v * math.cos(math.radians(theta))
    y = y + v * math.sin(math.radians(theta))
    return v ,x ,y

def const_forward(a, x, y, v, theta):
    x = x + v * math.cos(math.radians(theta))
    y = y + v * math.sin(math.radians(theta))
    return  x, y
        

def const_backward(a, v, x, y, theta):
    v -= a
    x = x + v * math.cos(math.radians(theta))
    y = y + v * math.sin(math.radians(theta))
    return v, x, y

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