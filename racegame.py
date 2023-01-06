# import random
# import turtle

# class Animal(turtle.Turtle):
#     def __init__(self, color, xcord, ycord, shape = 'turtle'):
#         turtle.Turtle.__init__(self)
#         self.speed(0)
#         self.penup()
#         self.color(color)
#         self.shape = shape
#         self.setpos(xcord,ycord)
    
#     def move(self):
#         newx = self.xcor() + self.vx
#         newy = self.ycor() + self.vy




class Building:
    '''
    Purpose: Represents a public building in St. Paul
    Instance variables:
        self.name: string - the building's name
        self.lat: float - the latitude of the building's location
        self.long: float - the longitude of the building's location
        self.open: float - the building's opening time
        self.close: float - the building's closing time
        self.meeting: boolean - whether building has a meeting room
        self.fields: int - # of softball fields attached to building
    Methods:
        __init__(self, line): Takes in a line from a CSV file 
            representing a building and splits it up to get the data 
            required for each instance variable
        __str__(self): Returns the string representation of this        
            object.  The name of the building is used for this.
        distance(self, other): Takes in two Building objects 
            (self, other) and returns the approximate distance 
            between the two in miles
    '''
    def __init__(self, line):
        data = line.split(',')
        self.name = data[1]
        self.lat = float(data[2])
        self.long = float(data[3])
        self.open = float(data[4])
        self.close = float(data[5])
        self.meeting = (data[6] == 'Yes')
        self.fields = int(data[7])
    def __str__(self):
        return f'{self.name}'
    def distance(self, other):
        dx = (self.long - other.long) * 48.91
        dy  = (self.lat - other.lat) * 69.17
        distance = (dx**2 + dy**2)**0.5 
        return distance

    
class Firehouse(Building):
    def is_open(self, time, day):
        return False

class Library(Building):
    def __init__(self, line):
        Building.__init__(self, line)
        self.events = []

    def is_open(self, time, day):
        if (time >= self.open) and (time < self.close) and (day not in self.events):
            return True
        else:
            return False

class Rec(Building):
    def __init__(self, line):
        Building.__init__(self, line)
        self.teams = []

    def is_open(self, time, day):
        if (time >= self.open) and (time < self.close) and (day != 'Su'):
            return True
        else:
            return False


if __name__ == '__main__':
    with open('buildings.csv') as fp:
        lines = fp.readlines()
        station19 = Firehouse(lines[6])
        rondo = Library(lines[11])
        hazel = Rec(lines[25])
        print(rondo.is_open(12.00, 'Mon')) #Should be about 4.3 miles
        print(hazel.is_open(15.00, 'Su')) #Should be about 8.9 miles

class City:
    def __init__(self, name, filename):
        self.name = name
        self.public = []
        f = open(filename)
        lines = f.readlines()
        for line in lines[1:]:
            if line[0] == "F":
                self.public.append(Firehouse(line))
            elif line[0] == "L":
                self.public.append(Library(lines))
            else:
                self.public.append(Rec(lines))

stpaul = City('St. Paul', 'buildings.csv')
stpaul.name
len(stpaul.public)
stpaul.public[0:10]