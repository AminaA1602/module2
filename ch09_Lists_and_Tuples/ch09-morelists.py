# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 12:15:42 2018

@author: Skitt
"""

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