def three_options(text, optionA, optionB, optionC):
   print(text)
   print('A.',optionA)
   print('B.',optionB)
   print('C.',optionC)
 
 
   player = input('choose: ')
 
   if player== 'A':
       return 'A'
     
 
   elif player == 'B':
       return 'B'
 
 
   elif player == 'C':
       return 'C'
 
   else:
       print('Invalid option, defaulting to C')
       return 'C'
 
 
 
 
'''
Purpose: give player options to choose from
parameter(s): the Options to choose from
Return Value: the option they have selected
'''
 
 
 
# Part C of the Homework
 
def adventure():
 
   print('You are in a cave with a big bear and you are trying to escape, but you see that there is a pile of treasure near the bear.')
   option = three_options('Its adventure time', 'LOL', 'YOLO', 'SOLO')
   if option == 'A':
       print('You have reached the next room')
      
 
       second_optionA = three_options('second part', 'GOGO', 'NOW', 'DONT')
       if second_optionA == 'A' or second_optionA == 'B':
           print('you have been caught stealing')
           return False
      
       else:
           print('On to the next room')
 
 
       third_optionA =  three_options('third part', 'Fob', 'next', 'Up')
       if third_optionA == 'B':
           print('You have made it out safe and sound')
           return True
       elif third_optionA == 'C':
           print('you have been devoured')
           return False
       elif third_optionA == 'A':
           print('you have reached the next path')
 
 
      
       fourth_optionA = three_options('chose one', 'die', 'live', 'lose')
       if fourth_optionA == 'A':
           print('winner')
           return True
       elif fourth_optionA == 'B' or fourth_optionA == 'C':
           print('loser')
           return False
 
   elif option == 'C':
       print('survivor')
       return True
  
  
   elif option == 'B':
       print('next')
       second_optionB = three_options('finally', 'winner winner chicken dinner', 'lose', 'welp')
       if second_optionB =='A':
           print('yessir')
           return True
       elif second_optionB == 'B' or second_optionB == 'C':
           print('sucks')
           return False
 
if __name__== "__main__":
 
   print(adventure())
