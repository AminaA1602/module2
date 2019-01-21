# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 11:08:56 2019

@author: Skitt
"""

import sqlite3 
import json 
conn = sqlite3.connect('db/phonebook_function.db')
c = conn.cursor() 