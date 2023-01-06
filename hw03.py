#part a

# def bagel_costs(num_bagels, delivery):
#     '''
# Purpose: to get the cost of bagels
# Parameter(s): numbers of bagels and delivery cost
# Return Value: Bagel costs
# '''

#     cost_of_delivery = 500

#     if num_bagels <= 6:
#         bagel_cost = num_bagels * 90
            
#         if bool(delivery):
#             bagel_cost = bagel_cost + cost_of_delivery
        
#         else: 
#             bagel_cost
            

#     elif (num_bagels >= 7) and (num_bagels <= 12):
#         bagel_cost = num_bagels * 80

#         if bool(delivery):
#             bagel_cost = bagel_cost + cost_of_delivery

#         else: 
#             bagel_cost



#     elif num_bagels >= 13:
#         bagel_cost = num_bagels * 70

#         if bool(delivery): 
#             bagel_cost = bagel_cost + cost_of_delivery
        
#         else:
#             bagel_cost
    
#     return bagel_cost


#part b





def three_options(text, optionA, optionB, optionC):
    '''
Purpose: list choices for user to choose
Parameter(s): text needed, and the 3 options to choose from
Return Value: what the user chose as their answer
'''


    print(text)
    print('A.', optionA)
    print('B.', optionB)
    print('C.', optionC)
    
    var = input('Your Choice was: ')

    if var == 'A':
        return 'A'

    elif var == 'B':
        return 'B'

    elif var == 'C':
        return 'C'
    
    else:
        print ('Invalid option, defaulting to C')
        return 'C'


# #part c 
# def adventure():
#     '''
# Purpose: Going on an adventure
# Parameter(s): None
# Return Value: Choice given by user
# '''
#     choice = three_options('1st_part', 'Go right', 'Go left', 'Go forward')
#     if choice == 'A':
#         print('move on to the right')
        
        
#         second_choiceA = three_options('2nd_part', 'Fight the demon', 'Fight the dragon', 'Go forward')
#         if second_choiceA == 'A' or second_choiceA == 'B':
#             print('Sorry, you died')
#             return False
#         else:
#             print('Proceed')
            
            


#         third_choiceA = three_options('3rd_part', 'Keep going', 'Go digging', 'Fight the goblin')
#         if third_choiceA == 'B':
#             print('You found gold!!! Congrats!!!')
#             return True
#         elif third_choiceA == 'C':
#             print('You died!!')
#             return False
#         elif third_choiceA == 'A':
#             print('Final step incoming!!!')
            
        

#         fourth_choiceA = three_options('4th_part', 'Pull the sword out of the stone', 'Try to go back and escape', 'Fight the Giant')
#         if fourth_choiceA == 'A':
#             print('You have reached the end, you are the new king')
#             return True
#         elif fourth_choiceA == 'B' or fourth_choiceA == 'C':
#             print('Oof, so close but sadly, you died. ')
#             return False
    

#     elif choice == 'C':
#         print('You have decided to run away, smart person!!')
#         return True

#     elif choice == 'B':
#         print('move on to the left')

#         second_choiceB = three_options('2nd_part','Go down this creepy path', 'Try to fight your clone', 'Pray for mercy from the Giant')
#         if second_choiceB == 'A':
#             print('Well done, you took the shortcut and now you are emperor of the world!!')
#             return True
#         elif second_choiceB == 'B' or second_choiceB == 'C':
#             print('Whoops, try again.')
#             return False
        

# print(adventure())

        

my_list = [3.2, 5.0, 16.5, 12.25]

for i in range(len(my_list)):
    my_list[ i ] += 5

print(my_list)