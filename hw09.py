import random
import csv
def weighted_choice(dictionary):
    '''
Purpose: counts how many times the key in the dictionary is randomly generated
Parameter(s): a dictionary
Return Value: number of times the inputted key is generated
'''

    lists = []
    for i in dictionary:
        lists = lists + [i] * dictionary[i]
    
    return random.choice(lists)

results = [weighted_choice({'green': 1, 'eggs': 3, 'ham':2}) for i in range(600)]
#print(results.count('green'))


#_____________________________________________________________________________________________________________
def count_votes(district, office):
    '''
Purpose: finding how many times the parameter office is found in the file district
Parameter(s): a string in the file and a file
Return Value: how many times the parameter office is found in the file district
'''

    empty = {}

    with open(district) as csvfile:
        fp2 = csv.DictReader(csvfile)
        for i in fp2:
            if i[office] in empty:
                empty[i[office]] += 1
                #adds one every cycle
            else:
                empty[i[office]] = 1
                #if it does not enter the if statement, it is set to 1
        csvfile.close()

    return empty

#print(count_votes('district_0z.csv', 'County Sheriff'))

#_____________________________________________________________________________________________________________
def random_sent(source_file, length):
    '''
Purpose: randomly generating 'length' amount of words in which the words are gotten from 'source_file'
Parameter(s): a number and a file
Return Value: a randomly generated sentence of length 'length'
'''
    with open(source_file) as csvfile:
        number = {}
        for line in csvfile:
            words = line.split()
            for word in words:
                if word not in number:
                    number[word] = 0
                number[word] += 1

        csvfile.close()

        final = ''
        for each in range(length):
            final += weighted_choice(number)
            final += ' '
        
    return final

#print(random_sent('short1.txt', 10))


num =2 
print(num//2)