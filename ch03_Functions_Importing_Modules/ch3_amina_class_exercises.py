# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 09:48:24 2018

@author: Skitt
"""

########### Chapter 3 - Funtions & Importing Modules #############

#----------------- Input from a user -----------------# 

print("What is your name?")
name = input()
print("Hello{}!".format(name))

##----------------- My first Function -----------------# 
def first_name():
    print("Amina") #---> At this stage, the funtion is running but not actually doing anything. You have to call the funtion by whatever name you defined it by. 
first_name()

print(int(2+2))

#----------------- Defining functions -----------------# 

def hello_world():
    print ("Hello World!")
    
def name_surname():
    print ("Whats your name?")
    name = input()
    
    print ("My name is {}".format(name))
    addition()
          
def ask_age():
    print ("How old are you?")
    age = int(input())
    
    print ("My age is {}".format(age))
    print () 
    year=2018-age 
    print("so you were born in..{}" .format(year))
    
def addition():
    add2_2 = 2+2 
    print (add2_2)
    
#name_surname()
ask_age()


##----------------- Functions and Methods -----------------# 

def hello_worldd():
    print("Hello World") #---> At this stage, the funtion is running but not actually doing anything. You have to call the funtion by whatever name you defined it by. 
    hello_worldd()
    
#----------------- Using range() with arguments -----------------# 

print(range (10)) #---> one argument
print(range (1,10)) #---> two argument
print(range (1,10,2)) #---> three argument

def hello_world_2args(a, b):
    print ("{} {}".format(a, b))
    
a1 = 'hello'
b1 = 'world'
a2 = 'love'
b2 = 'coding'
    
hello_world_2args(a1, b1)
hello_world_2args(a2, b2)

# ---------- Adding two numbers together with funtions --------- # 
 

def add_two_numbers():
    number1 = 1
    number2 = 2 
    answer = number1 + number2
    print ("{} plus {} is{}".format(number1, number2, answer))
    add_two_numbers()

def add_two_numbers_from_args(number1,number2):
    answer =number1 + number2
    print("{} plus {} is {}".format(number1, number2, answer))
add_two_numbers_from_args(5,10)

