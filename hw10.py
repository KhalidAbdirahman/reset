
def loop_sum_digits(str):
    '''
Purpose: to add all numbers found in the string inputted
Parameter(s): a string that contains numbers
Return Value: the sum of all numbers in the string provided 
'''

    count = 0
    for i in str:
        if i.isdigit():
            i = int(i)
            count += i
    return count

#print(loop_sum_digits("The Sum of 3 and 17 is 20"))

def rec_sum_digits(str):
    '''
Purpose: to add all numbers found in the string inputted
Parameter(s): a string that contains numbers
Return Value: the sum of all numbers in the string provided 
'''

    if str == '':
        return 0
    else:
        if str[0].isdigit():
            return int(str[0]) + rec_sum_digits(str[1:])
        else:
            return rec_sum_digits(str[1:])

#print(rec_sum_digits("The Sum of 3 and 17 is 20"))

def collatz(num):
    '''
Purpose: divides even numbers by 2 and multiplies odd nubers by 3 and adds 1 
Parameter(s): a number
Return Value: a list containing numbers
'''

    if num == 1:
        return 1
    else:
        if num % 2 == 0:
            if num//2 != 1:
                return [num] + collatz(num//2)
            else:
                return [num] + [collatz(num//2)]
        elif num % 2 != 0:
            num = (num * 3) + 1
            return [(num-1)//3] + collatz(num)

#print(collatz(6))

def collect_words(collection):
    '''
Purpose: to make the nested list inputted into a flat list
Parameter(s): a nested list
Return Value: a flat list
'''

    if isinstance(collection, (int,float)):
        return []
    elif isinstance(collection, str):
        return [collection]
    else:
        if len(collection) == 1:
            return collect_words(collection[0])
        else:
            return collect_words(collection[0]) + collect_words(collection[1:]) 



#print(collect_words(["Hello", ("Alice", ["how"]), [(["are"])], "you"]))

