# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 2018

@author: Amina 
"""
# ----------------- Simple Operations ----------------- # 
 
5 - 6
8 * 9
6 / 2
5 / 2
5.0 / 2
5 % 2
2 * (10 + 3)
2 ** 4

# % is called modulo - it shows the remainder of an expression e.g 5%2 is 1 because 1 is the remainder. 

# ----------------- How to use variables ----------------- # 

x = 12.5
y = 3 * x + 2 
print(y)

age = 5 #---> this is an integer 
age = "almost three" #--- > this is a string
a_longer_name = "hello, CFG!"

print(age)
print(a_longer_name)

# ----------------- Basic string manipulation ----------------- # 

print ("Bob " * 3)
print ("Bob " + 3)
print("hello".upper()) #-----> this is called a method
print("GOODBYE".lower()) 
print("the lord of the rings".title()) 
#there will be an error for print ("Bob" + 3) because you cannot have a string with an integer. 

# -------------------- String formatting ------------------- #

#What is string formatting? - It is a way of taking one or more variable and putting them inside a string b having placeholders for the values. 

age =5 
like = "painting"

age_description ="my age is {} and I like {}.".format(age,like)
print(age_description)

# ---------------- String formatting: User input -------------- #

age = " "
y=input(age)   
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

    
print ("So, you\'re" +str(age)+ "old," "{} tall  ","and weigh {} pounds/kg"
           .format(age, height, weight)) 
# %s{} = string , %d = decimal , %r = repr (another way of returning a string and detailed information of an object's content)


#--------------------HomeWork----------------------#
  
A = 2+3
B = 2.9+3.2
C = (3.2/2.0) + 7   
D = 2**3
E = 4**(1/2)
F = str(6) + 'a'
print (A)   
print (B)
    
""" For the Christmas holdidays, redo the homework and keep practicing them so you don't forget """