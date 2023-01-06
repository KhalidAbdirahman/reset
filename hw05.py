#part A
def longest_even(shows):
    maximum = ''
    for show in shows:
        if (len(show) % 2 == 0):
            if (len(maximum) < len(show)):
                maximum = show
    
    return maximum



#part B
def prior_to(data, key):
    target = []
    for data_1 in range(len(data)):
        if data[data_1] == key:
            target.append(data[data_1-1])
    return target



#part C
def all_three(social, grades, sleep):
    i = 0
    j = 0
    i_j = 0

    soc = len(social) 
    grad = len(grades)
    slee = len(sleep)
    otherwise = []

    while (i < soc and j < grad and i_j < slee):

        if (social[i] == grades[j] and grades[j] == sleep[i_j]):
            otherwise.append (social[i])
            i = i + 1
            j = j + 1
            i_j = i_j + 1

        elif (social[i] < grades[j]):
            i = i + 1
        elif grades[j] < sleep[i_j]:
            j = j + 1
        else:
            i_j = i_j + 1

    return (otherwise)

