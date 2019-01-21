# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 11:44:06 2018

@author: Skitt
"""

from shape import*

frame = Frame()
s1 = Shape('square',100)
s1.goto(200,100)

s2 = Shape('circle',100)
s2.goto(400,200)

s3 = Shape('diamond',100)
s3.goto(600,100)

x = 8 
y = 10

for i in range(100):
    s1.goto(x,y)
    x = x + 5
    y = y + 5 
    
#frame.close()
