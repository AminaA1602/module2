# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 13:36:24 2018

@author: Skitt
"""
from MovingShapes import*

frame = Frame()
numshapes = 3 
shapes = []

for i in range(numshapes):
    shapes.append(Square(frame,100))
for i in range(100):
    for shape in shapes: 
        shape.moveTick()

frame.close()

