# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 16:16:14 2018

@author: Skitt
"""

from MovingShapes import *
frame = Frame()
shape1= Square(frame,100)
for i in range(100):
        shape1.moveTick()
