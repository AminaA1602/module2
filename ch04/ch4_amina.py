# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 09:23:10 2018

@author: Skitt
"""
import random 
import datetime
import time 

def luckyNumberRandom():
    name = input('please type your name here: ')
    print ("hello " + name.upper() )
    number = int(input('please give a number '))

    print ('your lucky number is: '+ str(random.randint(50,number)))
 
startTime = time.time()

print('date and time', datetime.datetime.now())
print()
print('current time' , datetime.datetime.now().time())

#luckyNumberRandom()

processTime = time.time()-startTime

print()
print('program running time:', round(processTime,2),'second')