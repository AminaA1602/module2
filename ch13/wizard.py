# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 12:07:39 2019

@author: Skitt
"""

# ------- TASK 1: Initialising the person class ------- # 

class Person:
     def __init__(self,name,age,gender):
         self.name = name
         self.age = age
         if gender == 'm':
             self.isMale = True
         elif gender == 'f':
             self.isMale = False
         else:
             print('Gender not recognised!')
     def greetingInformal(self):
         print('Hi', self.name)
     def greetingFormal(self):
         if self.isMale:
             print('Welcome, Mr ', self.name)
         else:
             print('Welcome, Ms ', self.name)          
     def greetingAgeBased(self):
         
         if self.age < 18:
             print('Welcome, young ', self.name)
         elif self.age > 60:
             print('Welcome, venerable ', self.name)
         else:
             self.greetingFormal()
             
# --- TASK 2: Functionalities for the person class --- #

personOne = Person('Amina', 88, 'f')
personTwo = Person('Marie', 56, 'l')
personThree = Person('Milly', 39, 'k')

personOne.greetingInformal()#--- prints out the a customised formal message

personOne.greetingAgeBased()#---Typing this in the console prints out the a customised message based on age

# --- TASK 4: Create a subclass for the person class ---#
             
class Wizard(Person):
    def __init__(self,name,age,gender):
         self.name = name
         self.age = age
         if gender == 'm':
             self.isMale = True
         elif gender == 'f':
             self.isMale = False
         else:
             print('Gender not recognised!')
    def greetingFormal(self):
         print('Welcome, Mr ', self.name, end=' ')
         print('- you\’re a fine wizard!')
    def spell(self):#----TASK 6---------
        print('Expelliarmus!')



# ------------TASK 5: Redefine init --------------- #
         
#class Wizard(Person):
#    def __init__(self,name,age,gender):
#        Person.__init__(self,name,age,'f')
#        self.name = name
#        self.age = age
#        if gender == 'm':
#             self.isMale = True
#        elif gender == 'f':
#             self.isMale = False
#        else:
#             print('Gender not recognised!') 
             
# ---- TASK 6: Add new methods to subclass ------ #
 
#class Wizard(Person):
#     def spell(self):
#         print('Expelliarmus')
            
             