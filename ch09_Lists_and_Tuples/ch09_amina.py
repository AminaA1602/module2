# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 11:18:17 2018

@author: Skitt
"""

#----------------- Basic list -----------------# 
#x = ['hello', 'this','is','my','first','list']
#
#print(x[0]) 

#----------------- Index list -----------------# 
my_favourite_fruits = ['apple', 'orange' , 'banana']
print (my_favourite_fruits[0])

#----------------- Sorting a list -----------------# 
##generic sort function () has two variables and inputs as well as two memory space 

x = [7,11,3,9,2]
y = sorted(x)

y [2,3,7,9]
x [7,11,3,9,2]
x.sort()
x [2,3,7,9,11]

#----------------- Reverse sort -----------------# 
x = [7,11,3,9,2]
sorted(x)
[2,3,7,9,11]
sorted(x,reverse=True)
[11,9,7,3,2]
print()

#print('------generic sorted() function-------')
x = ['ab','cs','yw','zs','hd']
y=sorted(x,reverse=True)
print('now x is:', x)
print('now y is:', y)
print()

##print('--------object.method .sort()----------')
x.sort(reverse=True)
print('now x is:', x)
print('now y is:', y)
print()

# ----------------- List vs Tuples ----------------- # 

#---> The following is a list exmaple

a = [0,1,2,3,4,5,6,7,8,9]
a[0] = 50 
a.append('z')
print()

#--->The following is a Tuple list exmaple 
#
b = (0,1,2,3,4,5,6,7,8,9)
b[0] = 50 
b.append('z')
#--->There is an error here because Tuple is immutable which means they are more memory efficient.This is good for security reasons and useful for when running tests. That's why when you try and assign different types of listing, it always comes up with an error. 

#--->Tuple and list can covert with each other. e.g if I wnated to keep my bank detais safe I would use a tuple. However say I wanted to update my details, I can convert a tuple into a list and do so. 




