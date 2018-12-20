# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:08:29 2018

@author: Skitt
"""

#------------ Withdrawing money from a bank Exercise ------------# 


#    """A customer of ABC Bank with a checking account. Customers have the following properties:
# Attributes:
#     name: A string representing the customer's name.
#     balance: A float tracking the current balance of the customer's account.
# """

class Customer (object):
    
    def __init__(self, fullName, balance=1000.0):
         #--> Customer objectis *name* and starting balance is *balance*."""
         self.fullName = fullName
         self.balance = balance
         
         
def withdraw(self, withdrawAmount):
        #--> Return the balance remaining after withdrawing *amount* dollars."""
        if withdrawAmount > self.balance:
            raise RuntimeError('Amount greater than available balance.') #--> This means that if the object(customer) was to put an amount greater than 1000, they would get an 'error' message saying they can't withdraw because they don't have enough money available.
            
        else: 
            self.balance = withdrawAmount
        
        return self.balance  
    
def deposit(self, amount):
        """Return the balance remaining after depositing *amount* dollars."""
        self.balance += amount
        return self.balance 
Amina = Customer('Amina Aweis', 1000.0)


withdrawAmount = float(input('How much would you like to take out today? ' ))
print()
Customer.withdraw( 60.0)
    
print(Amina.balance)
    
print(Amina.name)
    
print(Amina.withdraw(100.0))
    
print(Amina.balance)

#----------------- Inheritence: Animal Exercise -----------------# 

class Animal():
        def eat(self):
            print('yum')
    
class Dog(Animal):
        def bark(self):
            print('Woof!')

class Cat(Animal):
        def meow(self):
            print('Meow')
            
Snoopy = Dog()
Snoopy.bark()
Snoopy.eat()

class Robot():
    def move(self):
        print('...move move move...')
        
class Clean_Robot(Robot):
    def clean(self):
        print('I\'m here to annoy you')
        
class CookRobot(Robot):
    def cook(self):
        print('before I go to make some lunch')

#----------------- Class Associations -----------------# 
import sys

class Animal():   
    def __init__(self, name,age):
        self.name = name
        self.age = age 
    def eat(self):
         print('yum')
         
class Dog(Animal):
    def bark(self):
        print('Woof!')
        
class Robot():
    def move(self):
        print('...move move move...')
        
class CleanRobot(Robot):
    def clean(self):
        print('I vaccum dust')        

class SuperRobot():
    def __init__(self, name,age):
        #There are 3 objects in this particular class
        self.name = name
        self.age = age
        
        self.o1 = Robot()
        self.o2 = Dog(name,age)
        self.o3 = CleanRobot()
        
    def playGame(self):
        print('alphago game')
        
    def move(self):
        return self.o1.move() #using robot class method
    
    def bark(self):
        return self.o2.bark() #using dog class method
     
    def clean(self):
        return self.o3.clean() #using cleanrobot class method
    
name = sys.argv[1]
age = sys.argv[2]
print(name)
print(age)

machineDog = SuperRobot(name,age)
machineDog.move()
machineDog.bark()

