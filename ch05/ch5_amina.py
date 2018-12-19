# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:08:29 2018

@author: Skitt
"""

###################### JASON BANK EXERCISE ###########################

#class Customer(object):
#    """A customer of ABC Bank with a checking account. Customers have the following properties:
# Attributes:
#     name: A string representing the customer's name.
#     balance: A float tracking the current balance of the customer's account.
# """
#    def __init__(self, fullName, age, balance=1000.0):
#         """Return a Customer object whose name is *name* and starting balance is *balance*."""
#         self.fullName = fullName
#         self.balance = balance
#         self.age = 20
#         
#         
#    def withdraw(self, withdrawAmount):
#        """Return the balance remaining after withdrawing *amount* dollars."""
#        if withdrawAmount > self.balance:
#            raise RuntimeError('Amount greater than available balance.')
#            
#        else: 
#            self.balance = withdrawAmount
#        
#        return self.balance  
#    
#    def deposit(self, amount):
#        """Return the balance remaining after depositing *amount* dollars."""
#        self.balance += amount
#        return self.balance 
#    
#Customer1 = Customer('Jason Taylor', 1000.0)
#withdrawAmount = float(input('How much would you like to take out today? ' ))
#print()
#Customer1.withdraw( 60.0)
    
#print(jason.balance)
#    
#print(jason.name)
#    
#print(jason.withdraw(100.0))
#    
#print(jason.balance)

###################### ANIMAL EXERCISES/EXAMPLES #####################

#class Animal():
#        def eat(self):
#            print('yum')
#    
#class Dog(Animal):
#        def bark(self):
#            print('Woof!')
#
#class Cat(Animal):
#        def meow(self):
#            print('Meow')
#            
#Snoopy = Dog()
#Snoopy.bark()
#Snoopy.eat()

#class Robot():
#    def move(self):
#        print('...move move move...')
#        
#class CleanRobot(Robot):
#    def clean(self):
#        print('I vaccum dust')
#        
#class CookRobot(Robot):
#    def cook(self):
#        print('I\'m going to make some lunch')


######################### MY PERSONAL EXAMPLE ########################


class Robot():
    def __init__(self, name, planet, location, evilBoss, scream):
        self.name = name
        
         
class Alien(Robot):
    def __init__(self, name, planet, location, evilBoss, scream):
        self.scream = scream
        
    def scream(self):
        print('MWAHAHAHA'*self.scream)
        
        
class AlienAgent(Robot):
    def detect(self,screamNumber):
        if screamNumber>= 10:
            print('It\'s an alien invasion!!!')
        
name = input('State your name and why you are on this planet!' )
print()
print('I think he\'s a bit lost boss, he looks scared')
evilBoss = input('This is my planet so it\'s my rules, I can ask what I want')
print('yes boss, but I think he atually might be los-')
evilBoss = input('BE QUIET OR I\'LL ZAP YOU TO THE FORBIDDEN PLANET!' )
print()
location = input( 'right, you don\'t look familiar, how did you end up here then?:') 
print('uhhh boss, what\'s that noise?') 
evilBoss = input('if you interupt me again, I will actually zap you')
print()      
planet= input('so young creature, where\s your planet?: ')
print()
scream = input('I don\'t have a planet, I came here to take yours MWAHAHAHA')

Robot007 = AlienAgent(name, planet, location, evilBoss, scream) #always inheritant ancester's
Robot007.detect(12)

#Collapse 
#Message Input
#I need to finish this script 

################### CLASS ASSOCIATIONS #######################
#import sys
#
#class Animal():   
#    def __init__(self, name,age):
#        self.name = name
#        self.age = age 
#    def eat(self):
#         print('yum')
#         
#class Dog(Animal):
#    def bark(self):
#        print('Woof!')
#        
#class Robot():
#    def move(self):
#        print('...move move move...')
#        
#class CleanRobot(Robot):
#    def clean(self):
#        print('I vaccum dust')        
#
#class SuperRobot():
#    def __init__(self, name,age):
#        #There are 3 objects in this particular class
#        self.name = name
#        self.age = age
#        
#        self.o1 = Robot()
#        self.o2 = Dog(name,age)
#        self.o3 = CleanRobot()
#        
#    def playGame(self):
#        print('alphago game')
#        
#    def move(self):
#        return self.o1.move() #using robot class method
#    
#    def bark(self):
#        return self.o2.bark() #using dog class method
#     
#    def clean(self):
#        return self.o3.clean() #using cleanrobot class method
#    
#name = sys.argv[1]
#age = sys.argv[2]
#print(name)
#print(age)

#machineDog = SuperRobot(name,age)
#machineDog.move()
#machineDog.bark()

#####################################################################