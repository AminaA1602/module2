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

#------------- Adding and removing items in a list  -------------# 
x = [1, 2, 3, 4, 5, 6, 7]
y = ['a', x]

print(y[1][2])

x[3] = ''
y.remove(x)
print(y)

print(x)
x.remove(x[0])
print(x)

#adding to a list. append always happens at the end 
x.append('hello')
print(x)

a = ['the', 'cat', 'sat']
b = ['on', 'the', 'mat']
c = a + b
print(c)

#set allows you to add lists and filter duplicates. Once this happens, the list becomes a dictionary. 
d =set(a+b)
print(d)


print(c[2:4])
print(c[-3:])

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

# ----------------- Lambda Function ----------------- # 

a = [0,1,2,3,77,4,5,6,7,8,9]
b = (0,1,2,3,4,5,6,7,8,9)
c = [2,2,3,3,33,4,5,6,7,8,9]
myFavF = ["apple", "orange", "banana"]
x = ["hw", "fy", "lf", "aa", "ed", "sb"]
z = ["ww", "uj", "cf", "uj", "fg", "sx"]

y = sorted(x)
x2 = [(a,3,'a',z ), (c, 1,'c', y), (b,5,'b', x)]
print(sorted(x2, key=lambda s:s[1]))
print(sorted(x2, key=lambda s:s[0][4]))
y[0] ='zz'
y[-2] ='ed'
#print(sorted(x2, key=lambda s:s[1]))


#x2 is the whole list in the table
#lambda s represnts each element in x2 in this ase it happens to be a tupole.
#:s[] represents the items inside the tupole. If there are more than one [] then it means the first item is the list and the rest is referring to the items in that first list. is the argument you're giving to tell the compound what to sort out. 


x = [1,2,3,4]
y = [3,4,10,3,]
z = [20,10,30,40] 






