


#Part A
import string


def starting_string(str_one, str_two):

    '''
Purpose:  the common substring that begins each string
Parameter(s): takes in two strings
Return Value: returns the common substring that begins each string
'''
    tru = True
    final = ''

    if len(str_one) > len(str_two):
        max = len(str_two)
    
    else:
        max = len(str_one)

    for i in range(max):
        if str_one[i] == str_two[i] and tru:
            final += str_one[i]
        else:
            tru = False



    return final




#Part B
def find_substring(string, substring):
    '''
Purpose: The function must return a list of all the locations where the substring is found in string
Parameter(s): takes in two strings
Return Value: the index of the first character of substring in string
'''

    sub_location = 0
    answer = []
    starting_point = 0
    while sub_location != -1:
        
        sub_location = string.find(substring)
        
        if sub_location != -1:
            if starting_point == 0:
                answer.append(sub_location)
                starting_point = sub_location + 1 
                string = string[sub_location + 1:]
            else:
                starting_point += sub_location  
                answer.append(starting_point)
                string = string[sub_location + 1:]
                
    answer[-1] = answer[-1] + 1      
            
    return answer

#Part C
def build_csv_string(data):
    '''
Purpose: The function should return a valid csv string where each sublist is a record in the string.
Parameter(s): takes in a list data
Return Value: a valid csv string where each sublist is a record in the string
'''
    final = 'name,assignment,grade\n'
    for i in data:
        for j in i:
            final = final + str(j) + ","
        if len(i) == 1:
            final = final + "N/A,0,"
        elif len(i) == 2:
            final = final + "0,"
        
        final = final[:-1]
        final += "\n"
    return final[:-1]

    
                

file = ['who','is','that']
print(len(file))