# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:28:48 2018

@author: Skitt
"""

# ------------ Shopping cart: For loop ------------- #

#my_shopping_cart = ["cake", "plates" , "plastic forks", "juice", "cups"] #--On the console it says there are 5 items because this is a compound data type which means that the item 'cake' starts with 0
#
#for item in my_shopping_cart:
#    print (item)
#    
##for char in 'I like codey codey'.split(): #--> This splits the word in each line. 
##    print(char) 
#
##for char in 'I like codey codey'.split('O'): #--> This splits the word in each line. 
##    print(char) 
#
## ------------ Loop through a list ------------- #
#
#values = [875,23,451]
#
#for val in values:
#    print('-->'+str(val))    
#    
## ------------ Loop through strings ------------- #
#
#for char in "Yes":
#    print(char)
#
## ------------ Task 3 - Creating a list  ------------- #
#    
#values = ['this', 55, 'that']   
#for item in values:
#         print('***', item)
#         
## ------------ Task 5 - Loop through a Tuple ------------- #
#    
## ------------ Task 7 - Create a salary dictionary ------------- #
         
#al = 20000
#bo = 50000
#ced = 1500
# Do this after the example below 

# -- Step 1: You need to create a dicitonary. 

#metals = {}
#metals = {'zinc':7.13,'iron':7.8,'gold':19.3,'lead':11.4}
#
#densities=list(metals.keys())
#densities.sort(key=lambda m:metals[m])
#
#densities.sort(reverse=True,key=lambda m:metals[m])
#KeyValue = sorted(metals.items(),key=lambda kv:kv[1], reverse=True)
#print(densities)

#for metal, metalValue in KeyValue:
#print('{0:>8} = {1:5.1f}'.format(metal,densities[metal]))

# ------------ Task - Combining if and else in for loops  ------------- #

#for metal in metals:
#   if densities[metals][0]> 9: 
#       print (metal)

# ------------ Task 9 - Design a sum function  ------------- #

#values = [7.13, 7.8, 19.3, 11.4]
#total = 0 
#for val in values: 
#    total+=val #---> this is the same as total = total + val
#print('TOTAL:'+str(total))
#
#def sumValues(l):
#    sumV = 0 
#    for val in l:
#        return sumV
#print (sumValues(values))

# ------------ Mid class challenge: Christmas list  ------------- #

Christmas_list = {}
Christmas_list = {'brain': 4, 'chocolates': 10, 'house': 3, 'laptop': 2, 'fluffysocks': 12 }

Wishlist=list(Christmas_list.items())

for gift in Christmas_list.items: