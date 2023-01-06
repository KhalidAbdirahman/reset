import random
#Problem A
class Boat:
    '''
Purpose: (What does an object of this class represent?) A boat
Instance variables: (What are the instance variables for this class, and what does each represent in a few words?) the boat name, the top speed and the current progress.
Methods: (What methods does this class have, and what does each do in a few words? You don’t have to include getters, setters, or __init__.) the function called move and the string function
'''

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

#Problem B
class BoatRace:
    '''
Purpose: (What does an object of this class represent?) randomly generate race between boats
Instance variables: (What are the instance variables for this class,
and what does each represent in a few words?) it gets its instance variables from Boat along with a csv file. 
Methods: (What methods does this class have, and what does each do in a few words? You don’t have to include getters, setters, or __init__.) count and race 
'''

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


if __name__ == '__main__':
    the_race = BoatRace('the_big_one.csv')
    print(the_race.get_race_name()) #The Big One 
    print(the_race.get_race_id()) #11
    print(type(the_race.race_id)) #<class 'int'>
    print(the_race.get_distance()) #120
    print(type(the_race.distance)) #<class 'int'>
    print(the_race.get_racers()) #[<__main__.Boat object at 0x03A2E4C0>, <__main__.Boat object at 0x03A2E4F0>]
    print(type(the_race.get_racers()[0].top_speed)) #<class 'int'>
    
if __name__ == '__main__':
    the_race = BoatRace('the_big_one.csv')
    the_race.add_racer(Boat("Late", 2))
    the_race.print_racers() #The Fire Ball: 0
                            #The Leaf: 0
                            #Late: 0
    print(the_race.count()) #3
    result = the_race.race() #The Fire Ball: 5
                             #The Leaf: 39
                             #Late: 2
                             #The Fire Ball: 17
                             #The Leaf: 56
                             #Late: 4
                             #The Fire Ball: 19
                             #The Leaf: 145
                             #Late: 4
    print(result) #[<__main__.Boat object at 0x03A2E4F0>]
    print(result[0].get_boat_name()) #The Leaf
    print(result[0].get_current_progress()) #145

    second_race = BoatRace('very_short.csv')
    second_result = second_race.race() #Runner: 84
                                       #Whirlwind: 10
                                       #Boaty McBoatFace: 4
                                       #Greased Lightning: 78
                                       #Much Speed: 43
    print(len(second_result)) #4



