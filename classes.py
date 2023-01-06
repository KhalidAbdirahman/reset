import turtle
import random

class Vec2:
    def __init__(self, x=0 , y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f'<{self.x},{self.y}>'
    def get_values(self):
        return [float(self.x),float(self.y)]
    def set_values(self,lst):
        self.x = lst[0]
        self.y = lst[1]
        return Vec2(self.x,self.y)
    def __add__(self,new_vector):
        return Vec2(new_vector.x + self.x, new_vector.y + self.y)
    def __mul__(self, scalar):
        return Vec2(self.x * scalar, self.y * scalar)

class Particle:
    def __init__(self, mass, pos, vel):
        self.mass = mass #this is a float or int
        self.pos = pos #this is a Vec2 object
        self.vel = vel #this is a Vec2 object
        self.t = turtle.Turtle()	#don’t forget to import turtle!
        self.t.shape("circle")
        self.t.speed(0)
        self.t.penup()
        #self.move()  #uncomment this after you implement move()
        self.t.pendown()
    def __str__(self, mass, pos, vel):
        return f'mass:{self.mass}, pos:{str(Vec2(self.pos))}, vel:{str(Vec2(self.vel))}'
















# if __name__ == '__main__':
#     mass = 0.5
#     accel1 = Vec2(1, 2)
#     print(accel1) #should output <1, 2>
#     accel2 = Vec2(2, -2)
#     total_accel = accel1 + accel2
#     print(total_accel) #should output <3, 0>
#     force = total_accel * mass
#     flist = force.get_values()
#     print(flist) #should output [1.5, 0.0]
#     accel1.set_values(flist)
#     print(accel1) #should output <1.5, 0.0>
