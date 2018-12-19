# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:31:07 2018

@author: Skitt
"""

#While loop in a function- Triangular numbers# 

#def triangular(n):
#        trinum = 10 
#        while n > 0:
#            trinum = trinum + n 
#            n = n - 1
#        return trinum 
 

    
#Exmaple of a while loop with an if/else statement - School test# 

#mark = 1 #-- you iniitalise this so the computer knows what mark is. Kind of like assigning a variable#


#while mark > 0:
#    mark = int(input('Enter mark: '))
#    mark =int(mark)
#    print("Mark is", mark, end='')
#    
#    if mark >= 70:
#        print("-first class!")
#    elif mark >= 40:
#        print("-that\'s a pass")
#    else:print("-that\'s a fail")
#       

#----Another exmaple----# 
#didYouPass = 'Yes'

#while didYouPass == 'Yes':
#
#   mark = int(input('What is your score? '))
#   
#   if mark >= 70 and mark <=90:
#       print('FIRST CLASS')
#
#   elif mark >= 40:
#       print('PASS')
#
#   elif mark < 40:
#       print('FAIL')
#
#   didYouPass = input('Did you pass? ') 

 
# Breaking a loop# 
#i = 55 
#while i > 10:
#        print(i)
#        i=i*0.8
#        if i ==35.2:
#            break

while True:
    name = input('What is your name?')
    if name == 'done':
        break
    print('Hello',name)  
    
    