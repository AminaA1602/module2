# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 11:42:55 2018

@author: Skitt
"""

from random import randint

#
#def guess():
#   end_range=20 
#   attempts=5
#   number = randint(0,end_range) 
#The lucky number is between 0- 20

def user_game(attempts,end_range): 
    number = randint(1,end_range) #---> Your lucky number is 20. This bit means that the lucky number is between 1 and 20.  
    print("Welcome! Can you guess my secret number? ")
    print("You only have 5 attempts so choose wisely!" ) #--> This section is the user input 
    
    while attempts > 0 :
       number = int(input("Enter your number here: "))
    
    LuckyNumber = 20 
    if user_game > LuckyNumber: #---> condition
        print(int('you entered {} which is too low. You have {} attempts left.format(user_guess, attempts'))
    elif user_game > number:
           print('you guessed {}. Here\'s a hint - it was too high! You have {} attempts left.format(user_guess, attempts') #--> This is why you used the while loop
      
    elif user_game == number:
           print(int('You entered {} which is the right number. YOU WIN!'))
           attempts-=1 #---> When the user types in the number, they'll have one less attempt so this updates that and will keep doing so until all 5 attempts have run out. 
    
user_game(1,20)  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#   while attempts> 0:
#       print('the secret number is', number)
#       user_guess=int(input("Enter your number: "))
#       if user_guess < number:
#           print('you guessed {}. Unfortunately - it was too low! You have {} attempts left.'.format(user_guess, attempts))
#       elif user_guess > number:
#           print('you guessed {}. Here\'s a hint - it was too high! You have {} attempts left.'.format(user_guess, attempts))
#       elif user_guess ==number:
#           print('That\'s the right number. You won!')
#           break
#           attempts-=1 
#   print("Thanks for playing!")
  




    





   

    
   
        