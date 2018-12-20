# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 10:18:06 2018

@author: Skitt
"""
salary = {}
salary['al'] = 20000
salary['bo'] = 50000
#name of the dictionary is salary
#there are two lists in this dictionary


#Here we are creating and assigning values to a dictionary which you can see in the last part with te curly brackets. NOTE: You can't start numbers with zero because it won't count. 
salary[7] = ('Joke', 'Chen', 'Bond')
salary 
{'bo': 5000, 'al': 2000, 7:('Joke', 'Chen', 'Bond')}

#This is how you would use a key to get values in a dictionary
#salary['bo']
#50000

#This is an exmaple of how you can overwrite dictionary values or do operations with values. When you run this, you will notice that the dictionary value salary['bo'] changes which means that it's mutable. 
salary['bo'] = 55000
salary['al'] += 2000
salary 
{'bo':5500, 'al': 22000}

#----------------- Creating your own dicitonary -----------------# 


tel = { 'alf':111, 'bobby':222, 'calvin':333 } 
tel 
{'alf':111, 'calvin': 333, 'bobby': 222}

tel['bobby']
222

tel['bobby'] = 555
tel
{'alf':111, 'bobby':555, 'calvin':333}

#---------- Deleting an item in a dictionary dicitonary ---------# 

del tel ['bobby']
tel
{'alf':111, 'calvin': 333}

#getting keys and values from a dictionary##
tel.keys()
dict_keys(['alf', 'calvin'])
tel.values()
dict_values([111, 333])

#-------------------- get keys and values ---------------------# 

tel_keys = list(tel.keys())
print(tel_keys)
#print(tel.values())
tel.keys()[0]

type(tel.values())
#dict_values
list(tel.keys())[0]
'alf'

#----------------- How to avoid key errors ------------------# 

k= 'eric'
if k in tel:
    print(k, ':', tel[k])
    
else: 
    print(k,'not found')

#----------------- Sorting dictionary by value ------------------# 
    
counts = {'a':3,'c': 1,'b':5}
labels = list(counts.keys())
labels.sort(key=lambda k:counts[k])
print()

students = {}
students = {'Amina': (2, 4), 'Leanne': (9, 26), 'Pam': (5, 7), 'Kate': (3, 14)}
pupil = list(students.keys())

#----------------- Sorting keys and values ------------------# 

metals = {}
metals = {'zinc':[7.13, 24, 2.6], 
          'iron':[7.8,64,3.8], 
          'gold':[19.3,54,5.2], 
          'lead':[11.4,74,8.5]}

sortedMetals=list(metals.keys())
sortedMetals.sort(reverse=True,key=lambda m:metals[m][1])
print(sortedMetals)

Shareprice=list(metals.keys())
Shareprice.sort(key=lambda m:metals[m][1])
print(Shareprice)

Density=list(metals.keys())
Density.sort(key=lambda m:metals[m][0])
print(Density)



