# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 11:18:17 2018

@author: Skitt
"""

userInput = input('Please give a number ')
#result = userInput - 2 --- you get an error here because you need to refer to the right type. 2 is an integer but this is not displayed in the code. 

userInput = input('Please give a number ')
result = (type(userInput))
# --- The data type str and not an int because it has not been told that the value 5 is an inetger yet. To change this, you need to change the result to an int data type. 

userInput = input('Please give a number ')
result = (int(userInput)) #--- the resut has now been changed into an int data type. 

#---------------- Using Breakpoints for debugging ----------------# 

# Data type errors are quite common. When you're not using the print function to check and see if your function is working, you can use breakpoints to check your code and see if it's 'flowing' correctly 

userInput = input('Please give a number ')
def simpleOperation(userInput):
    intInput = int(userInput)
    result = intInput - 2
    return result 

def nestedOperation(result):
    result = simpleOperation(userInput)
    result2 = result * 2 
    return result2
result = simpleOperation(userInput)
result2 = nestedOperation(result)
print(result2)

