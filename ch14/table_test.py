# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 11:44:46 2019

@author: Skitt
"""

import sqlite3 
conn = sqlite3.connect('task1.db')
c = conn.cursor()
conn.commit()

c.close()
conn.close()
#print(row)
