# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 16:55:47 2018

@author: Skitt
"""

from shape import*
from pylab import random as r 

class MovingShape:
    def __init__(self,frame,shape,diameter):
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape,diameter)
        self.frame= frame
        self.x = self.startx()
        self.y = self.starty()
        self.dx = self.movingrandomx()
        self.dy = self.movingrandomy()
    def movingrandomx(self):    
        self.dx = 5 + 10 * r()
        if r() > 0.5:
            return self.dx 
        else:
            self.dx = 0-self.dx
            return self.dx
            
    def movingrandomy(self):    
        self.dy = 5 + 10 * r()
        if r() > 0.5:
            return self.dy 
        else:
            self.dy = 0-self.dy
            return self.dy
    
    def goto(self,x,y):
        self.figure.goto(x, y)
        
    def moveTick(self):
        self.x += self.dx
        self.y += self.dy
        self.goto(self.x, self.y)
        self.hitx()
        self.hity()
        
    def hitx(self):
        if self.x <= self.minimumx:
            self.dx = self.dx * - 1 
        elif self.x >= self.maximumx:
            self.dx = self.dx * - 1 
        return self.dx 
    
    def hity(self):    
        if self.y <= self.minimumy:
            self.dy = self.dy * - 1 
        elif self.y >= self.maximumy:
            self.dy = self.dy * -1 
        return self.dy 
        
    def minimumx(self):
        self.minimumx = self.diameter/2 
        return self.minimumx
    
    def minimumy(self):
        self.minimumy = self.diameter/2 
        return self.minimumy
    
    def maximumx(self):
        d2 = self.diameter / 2 
        self.maximumx = self.frame.width - d2
        return self.maximumx 
    
    def maximumy(self):
        d2 = self.diameter / 2 
        self.maximumy = self.frame.height - d2
        return self.maximumy
     
    def startx(self): 
        self.maximumx()
        self.minimumx()
        self.x = self.minimumx + r() * (self.maximumx - self.minimumx)
        return self.x 
        
    def starty(self): 
        self.maximumy()
        self.minimumy()
        self.y = self.minimumy + r() * (self.maximumy - self.minimumy)
        return self.y 
            
   
class Square(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'square',diameter)

class Diamond(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'diamond',diameter)

class Circle (MovingShape):
    def __init__(self,frame,diameter ):
        MovingShape.__init__(self,frame,'circle',diameter)


