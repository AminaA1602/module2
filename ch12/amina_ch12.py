# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:28:48 2018

@author: Skitt
"""

# ------------ Shopping cart: For loop ------------- #

# my_shopping_cart = ["cake", "plates" , "plastic forks", "juice", "cups"] #--On the console it says there are 5 items because this is a compound data type which means that the item 'cake' starts with 0
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

#dessert = ("cheesecake", "brownie", "chocolate")
#for item in dessert:
#    print(item)
#prints:
#cheesecake
#brownie
#chocolate    

## ------------ Task 7 - Create a salary dictionary ------------- #
 
#Task 6&7-looping through a sorted dictionary
  
#densities = {'iron':7.8, 'gold':19.3, 'zinc':7.13, 'lead':11.4}
#metals = list(densities.keys())
#print(metals)
#prints:
# ['iron', 'gold', 'zinc', 'lead']    
        
#al = 20000
#bo = 50000
#ced = 1500
# Do this after the example below 

#########################################################################

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

# ---> To return/print outside the for loop, print the return outside the loop  # ---> To return/print within the loop if say, you're looking for immediate results within each loop, you 

# --- Task 10 - using a loop with index values --- #
#values = [12,3,22]
#for i in range(len(values)):
#    values[i] = values[i] * 2
#    print(values)     
#prints:
#[24, 3, 22]
#[24, 6, 22]
#[24, 6, 44]

# ------------ Task 8: Counter dictionary ----------- #
    
#colours = ['red', 'green', 'red', 'green', 'blue', 'green', 'green']
#d ={}
#for item in colours:
#    
#    if item not in d: 
#        d[item] = 0 
#        print(d, 'first time')
#    else:
#        d[item] =  d[item] +1
#        print(d)

#--- task 11: using a loop with the range function --- #

#values = [3,12,9]
    
#for v in values:    
#    print(values) 
#prints: 
#[3, 12, 9] 
#[3, 12, 9] 
#[3, 12, 9] 
#as there are three values
    
# -------- Task 12: Using break in for loops --------- #

#values = ['milly', 'sariks', 'fabi', 'amina', 'joke', 'chen', 'loren']
#
#for index in range (0,len(values)):
#    if values [index]=='fabi':
#        print('find her!', values[index])
#        break 

#nums = [1,5,30,200,101,100,22]
#for index in range(len(nums)):
#    print('loop index', index, 'with value', nums[index])
#    if nums [index] > 100:
#        print('break :', nums[index], 'with index', index)
#        break

# ------------ Task 13: Nested Loops ------------- #

#outer_vals = [1,2, 3]
#inner_vals = ['A','B','C']
#d = {}
#for oval in outer_vals: #--> this is [1,2,3]
#    print(oval)
#    for ival in inner_vals: #--> this is ['A','B','C']
#        d[oval] = ival
#        print(d)

# --- Task 14: Multiplication --- multiplication table with a for loop --- #


#for i in range(1,7):
#   for j in range(1,11):
#      print('{0:>3}'.format(i * j), end='')
#   print('\n')
#prints:
   
#1  2  3  4  5  6  7  8  9 10
#
#2  4  6  8 10 12 14 16 18 20
#
#3  6  9 12 15 18 21 24 27 30
#
#4  8 12 16 20 24 28 32 36 40
#
#5 10 15 20 25 30 35 40 45 50

#6 12 18 24 30 36 42 48 54 60

#Loop takes the first loop i (from 1 to 7) takes the first number (1) 
#Then goes to the second loop (from 1 to 11) takes the first number (again 1) so does 1*1
#Then 1 * 2, 1 * 3 until 1*10. 
#Then will go to 2 and ill do: 2*1, 2*2 until 2*10. 
#Then 3*1 etc until all are finished up until the final one 6*10 which is 60
   
#for i in range(1,11):
#   for j in range(1,11):
#      print('{0:>3}'.format(i * j), end='')
#   print('\n')   
#until 10*10
    
    
    
    
    
    
# -------- Mid class challenge: Christmas list ------- #

#Christmas_list = {}
#Christmas_list = {'brain': 4, 'chocolates': 10, 'house': 3, 'laptop': 2, 'fluffysocks': 12 }
#
#Wishlist=list(Christmas_list.items())

#for gift in Christmas_list.items:  