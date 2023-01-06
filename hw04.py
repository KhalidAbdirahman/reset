#problem A
def sum_odd_digits(a_number):
    '''
Purpose: finding the sum of all odd digits in a number
Parameter: a random positive integer
Return Value: the sum of all odd digits in a number 
'''

    odd = 0
    total = 0
    while a_number > 0:
        x = a_number % 10   
        if x % 2 != 0:
            odd = odd + x
        else:
            odd = 0
        total = total + odd
        odd = 0
        a_number = a_number // 10
    return total

#problem B
def next_divisor(n, lower_bound):
    '''
Purpose: searching for a divisor bigger than the lower_bound 
Parameters: a number and a minimum value
Return Value: the lowest divisor for n that is greater than lower_bound
'''
    if (n < lower_bound):
            return -1 
    for i in range (lower_bound + 1, n + 1): 
        if n % i == 0:
            return i
        elif (n > lower_bound) and (n % i != 0):
            i += 1

#problem C
def play_nim(winning_number):
    '''
Purpose: to find the first player who gets to the 'winning number'.  
Parameters: the number that the players want to reach
Return Value: first player to get to the 'winning number'.
'''

    print(f'The goal is {winning_number}. Pick a number between 1 and 3')
    total = 0
    while total < winning_number:
        
        player_one = int(input(f'Current score {total} Player 1 enter a number: '))
        if (0 > player_one) or (player_one > 3):
            print('Invalid number, try again.')
        elif (0 < player_one) and (player_one <= 3):
            total = total + player_one
            if total >= winning_number:
                return 1
            
        player_two = int(input(f'Current score {total} Player 2 enter a number: '))
        if (0 > player_two) or (player_two > 3):
            print('Invalid number, try again.')
        elif (0 < player_two) and (player_two <= 3):
            total = total + player_two
            if total >= winning_number:
                return 2
    total = total + player_two
                   
print(play_nim(10))

