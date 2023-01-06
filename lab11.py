
import turtle
import random

class Rational:
    def __init__(self,num=0,den=1):
        self.numerator = num
        if den == 0:
            self.denominator = 1
        else:
            self.denominator = den
    def __str__(self):
        if (self.denominator == 1) and (self.numerator != 0):
            return str(self.numerator)
        if (self.numerator == 0):
            return str(0)
        return str(self.numerator) + '/' + str(self.denominator)

class Vec2:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return str(f'<{self.x},{self.y}>')
    def get_values(self):
        return [float(self.x), float(self.y)]
    def set_values(self, lst):
        self.x = lst[0]
        self.y = lst[1]
        return Vec2(self.x,self.y)
    def __add__(self, vector):
        return Vec2(vector.x + self.x, vector.y + self.y)
    def __mul__(self, scaller):
        return Vec2(self.x * scaller, self.y * scaller)

class Particle:
    def __init__(self, mass, pos, vel):
        self.mass = mass #this is a float or int
        self.pos = pos #this is a Vec2 object
        self.vel = vel #this is a Vec2 object
        self.t = turtle.Turtle()    #don’t forget to import turtle!
        self.t.shape("circle")
        self.t.speed(0)
        self.t.penup()
        self.move()  #uncomment this after you implement move()
        self.t.pendown()
    def __str__(self):
        return f'mass:{self.mass}, pos:{str(Vec2(self.pos))}, vel:{str(Vec2(self.vel))}'
    def move(self):
        self.t.setpos(self.pos.x, self.pos.y)
    def accelerate(self, a, t):
        self.time = t
        self.a = a
        self.pos = self.pos + (self.vel * self.time) + (self.a*.5*(self.time**2))
        self.vel = self.vel + self.a*self.time
        self.move()


if __name__ == '__main__':
    p1 = Particle(50,Vec2(-200,-50),Vec2(30,30))
    p2 = Particle(20,Vec2(100,50),Vec2(-20,0))
    print(p2) #should output mass:20, pos:<100, 50>, vel:<-20, 0>
    p2.accelerate(Vec2(0,-10),2)
    print(p2) #should output mass:20, pos:<60.0, 30.0>, vel:<-20, -20>
    p2.accelerate(Vec2(20,20),3)
    print(p2) #should output mass:20, pos:<90.0, 60.0>, vel:<40, 40>
    for i in range(100):
        p1.accelerate(Vec2(0,-10),0.1)
        p2.accelerate(Vec2(0,-10),0.1)
    print(p1) #should output mass:50, pos:<100.0, -250.0>, vel:<30.0, -70.0>
    print(p2) #should output mass:20, pos:<490.0, -40.0>, vel:<40.0, -60.0>


if __name__ == '__main__':
    for i in range(20):
        i = Particle(1,Vec2(random.uniform(-200,200),random.uniform(-200,200)), (Vec2(random.uniform(-50,50),random.uniform(-50,50))))
        for j in range(100):
            i.accelerate(Vec2(0,-9.8),.1)
        turtle.update