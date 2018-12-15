# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 09:23:10 2018

@author: Skitt
"""
#import random 
#import datetime
#import time 
#
#def luckyNumberRandom():
#    name = input('please type your name here: ')
#    print ("hello " + name.upper() )
#    number = int(input('please give a number '))

#    print ('your lucky number is: '+ str(random.randint(50,number)))
 
#startTime = time.time()
#
#print('date and time', datetime.datetime.now())
#print()
#print('current time' , datetime.datetime.now().time())
#
#luckyNumberRandom()
#
#processTime = time.time()-startTime
#
#print(round(processTime,2))
#print('program running time:', round(processTime,2),'second') 


#
#def checkTeen(age):
#    return age >=13 and age <=19
#
#age = 22 
#isaTeen = age >= 13 and age <= 19 
#
#print(isaTeen)

#age_list = [14, 20, 68]
#for age in age_list:
#    if age < 13:
#        print("Child")
#    elif age <= 19:
#        print("Teen")
#    elif age <= 65:
#        print("Adult")
#    else:
#        print("Pensioner")

#number = input("Enter a nmber between 1 and 10: ")
##number = int(number) #converts input from string
#
#
#if number > 10:
#    print ("Too high!")
#    
#if number <= 0:
#        print ("Too low!")
#
#else:
#    print("dont't know!")    


age = " "
y=input(age)   
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

    
print ("So, you\'re" +str(age)+ "old," "{} tall  ","and weigh {} pounds/kg"
           .format(age, height, weight))
   