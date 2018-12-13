# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 13:54:24 2018

@author: Skitt
"""

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


#x = [1,2,3,4]
#y = [3,4,10,3,]
#z = [20,10,30,40] 