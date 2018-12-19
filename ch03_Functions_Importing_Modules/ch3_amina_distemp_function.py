# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 16:08:30 2018

@author: Skitt
"""

#----------------- Task 3  -----------------# 

def add_two_numbers_from_args(a, b):
    a = 1 
    b = 2 
    answer = a + b
    print(answer)
    return ("{} plus {} is {}".format(a, b, answer))
    add_two_numbers_from_args(a, b)


def converting_distance(miles): 
    kilometers = (miles * 8.0) / 5.0
    convertdist = "{} miles to km is {}".format(miles,kilometers)
    print(convertdist)
    return convertdist


#----------------- Task 4  -----------------# 

def temperature_conversion(centigrade):
    fahrenheit = centigrade * 9.0 / 5.0 + 32
    kelvin = centigrade + 273.15
    convert_temp= "temperture from centigrade to fahrenheit is {}, and {} in kevin".format(fahrenheit,kelvin)
    print(convert_temp)
    return convert_temp


