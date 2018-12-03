# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 09:48:24 2018

@author: Skitt
"""

print(range(10))
print(range(1,10))
print(range(1,10,2))

def hello_world_2args(a, b):
    print ("{} {}".format(a, b))
    
a1 = 'hello'
b1 = 'world'
a2 = 'love'
b2 = 'coding'
#    
#hello_world_2args(a1, b1)
#hello_world_2args(a2, b2)

def add_two_numbers(number1, number2):
    answer = number1 + number2
    print ("{} plus {} is{}".format(number1, number2, answer))

number1 = 1
number2 = 2 
add_two_numbers(number1, number2)
    
def convert_distance(miles):
    kilometers = (miles * 8.0) / 5.0
    print ("Converting distance in miles to kilometers:")
    print ("Distance in miles:", miles)
    print ("Distance in kilometers:", kilometers    
    
    
