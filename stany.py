from const import sila_napedowa, sila_oporu, masa_pojazdu
import math

class stany:
    def __init__(self ,x, y, theta, v, a):
        self.x = x
        self.y = y
        self.theta = theta
        self.v = v
        self.a = a
        pass

    def idle(self):
        self.a = (0 - sila_oporu) / masa_pojazdu
        self.v += self.a
        self.x = self.x + self.v * math.cos(math.radians(self.theta))
        self.y = self.y + self.v * math.sin(math.radians(self.theta))
        return self.v, self.x, self.y

    def const_forward(self):
        self.x = self.x + self.v * math.cos(math.radians(self.theta))
        self.y = self.y + self.v * math.sin(math.radians(self.theta))
        return  self.x, self.y
        

    def const_backward(self):
        self.v -= self.a
        self.x = self.x - self.v * math.cos(math.radians(self.theta))       
        self.y = self.y - self.v * math.sin(math.radians(self.theta))
        return self.v, self.x, self.y

    def steering_left(self):
        self.theta -= 10
        return self.theta

    def steering_right(self):
        self.theta += 10
        return self.theta

    def accelerate(self):
        self.v += self.a
        self.x = self.x + self.v * math.cos(math.radians(self.theta))
        self.y = self.y + self.v * math.sin(math.radians(self.theta))
        return self.v, self.x, self.y

    def brake(self):
        self.v -= 2 * self.a
        self.x = self.x + self.v * math.cos(math.radians(self.theta))
        self.y = self.y + self.v * math.sin(math.radians(self.theta))
        return self.v, self.x, self.y
