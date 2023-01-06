import csv

#problem A
def new_cases(date, state):
    '''
Purpose: to get the amount of COVID cases in a given state
Parameter(s): two strings representing a date and a two-letter state abbreviation
Return Value: an integer representing the number of new cases reported by the given state on that date
'''

    
    with open('covid_data.csv') as fp:
        for row in fp:
            row = row.split(',')

            if (date == row[0]) and (state == row[1]):
                if row[5].isnumeric():
                    fp.close()
                    return int(row[5])
                else:
                    fp.close()
                    return -1
    fp.close()               
    return -1
    

#problem B

def length_correct(fname, length):
    '''
Purpose: Modifying the maximum amount of letters allowed in one line
Parameter(s): takes in a string and an integer
Return Value: returns None
'''

    fn = open(fname, 'r')
    final = open('mod-' + fname, 'a')
    for i in fn:
        fp = len(i)
        while fp > length:
    
            fname_length = i[:length - 1]
            fname_length_2 = fname_length + '\n'
            final.write(fname_length_2)
            i = i[length - 1:]
            fp = len(i)
            
        final.write(i)
        
    fn.close()
    final.close()


#problem C
def stretch_model(fname_in, fname_out):
    '''
Purpose: Stretching given files (images)
Parameter(s): original file to be stretched, and the output file that is stretched
Return Value: returns how many times it is stretched
'''

    try:
        fp = open(fname_in)
    except:
        return -1

    fn = open(fname_out, 'w')
    count = 0
    for listName in fp:
        listName_2 = listName.split(' ')
        if listName_2[0] == 'v':

            first = ''.join(listName_2[0]) + ' '
            second = ''.join(listName_2[1]) + ' '
            third = ''.join(str((float(listName_2[2])) * 2))+ ' '
            fourth = ''.join(listName_2[3])
            count += 1
            
            fn.write(first)
            fn.write(second)
            fn.write(third)
            fn.write(fourth)

        elif listName_2[0] == 'f':
            stringName = ' '.join(listName_2)
            fn.write(stringName)
    
    fp.close()
    fn.close()
    return count

