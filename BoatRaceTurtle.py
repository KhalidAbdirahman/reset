import random
import turtle

class Boat:

    def __init__(self, boat_name,top_speed = 3,current_progress = 0):
        self.boat_name = boat_name
        self.top_speed = top_speed
        self.current_progress = current_progress 
    def set_top_speed(self, new_top_speed):
        self.top_speed = new_top_speed
        return self.top_speed
    def set_boat_name(self, string):
        self.boat_name = string
        return self.boat_name
    def set_current_progress(self, new_progress):
        self.current_progress = new_progress
        return self.current_progress
    def get_boat_name(self):
        return self.boat_name
    def get_top_speed(self):
        return self.top_speed
    def get_current_progress(self):
        return self.current_progress
    def __str__(self):
        return f'{self.boat_name}: {self.current_progress}'
    def move(self):
        random_value = random.randint(0, self.top_speed)
        self.current_progress += random_value
        return random_value

class BoatRace:
    def __init__(self, csv):
        fp = open(csv)
        fp_2 = fp.readlines()
        self.race_name = (fp_2[0][5:]).strip()
        self.race_id = int(fp_2[1][3:])
        self.distance = int(fp_2[2][9:])
        self.racers = []
        boats = fp_2[3:]
        for i in range(len(boats)):
            boats[i] = (boats[i]).split(',')
            self.racers.append(Boat(boats[i][0], int(boats[i][1].strip('\n'))))
    def get_race_name(self):
        return self.race_name
    def get_race_id(self):
        return self.race_id
    def get_distance(self):
        return self.distance
    def get_racers(self):
        return self.racers
    def add_racer(self, boat_object):
        self.boat_object = boat_object
        self.racers.append(self.boat_object)
    def print_racers(self):
        for boat in self.racers:
            print(boat)
    def count(self):
        count = 0 
        for i in range(len(self.racers)):
            count += 1
        return count
    def race(self):
        final = []
        while final == []:
            for boat in self.racers:
                boat.move()
                if boat.current_progress >= self.distance:
                    final.append(boat)
            self.print_racers()
        return final  
