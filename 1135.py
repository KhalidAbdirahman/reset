def build_csv_string(data):
    '''
Purpose: The function should return a valid csv string where each sublist is a record in the string.
Parameter(s): takes in a list data
Return Value: a valid csv string where each sublist is a record in the string
'''
    final = 'name,assignment,grade'

    for lst in data:
        final = final + '\n'
        if len(lst) == 1:
            final = final + lst[0] + ',N/A,0'
        elif len(lst) == 2:
            final = final + lst[0] + '0'
        
        else:
            final = final + lst[0] + ',' + lst[1] + ',' + str(lst[2])
        

    return final
    


#print(build_csv_string([["Sam", "Lab 01", 5.4], ["Zoe"], ["Amanda", "Quiz 04", 100]]))



def build_csv_string(data):
    '''
Purpose: The function should return a valid csv string where each sublist is a record in the string.
Parameter(s): takes in a list data
Return Value: a valid csv string where each sublist is a record in the string
'''
    final = 'name,assignment,grade\\n'
    for i in data:
        for j in i:
            final += str(j) + ','
        if len(i) == 1:
            final += 'N/A,0'
        elif len(i) == 2:
            final += '0'
        final += '\\' + final[:1]

    final_2 = ''
    final_2 += "'" + final[:-1] + "'"
    

    for i in data:
        if len(i) == 1:
            final_3 = final_2[0:-2] + "'"
        if len(i) == 2:
            final_3 = final_2[0:-1] + "'"
        if len(i) == 3:
            final_3 = final_2[0:-3] + "'"
    



class Duration:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __add__(self, other):
        if not isinstance(other, Duration):
            return None # Outputs 'None'
        total_hours = self.hours + other.hours
        total_minutes = self.minutes + other.minutes
        if total_minutes >= 60:
            total_hours += 1
            total_minutes -= 60
        return Duration(total_hours, total_minutes)

    def __int__(self):
        return self.hours * 60 + self.minutes

flight_time = Duration(5, 33)
drive_time = Duration(3, 29)

print(int(flight_time) + int(drive_time))
print(int(flight_time + drive_time))