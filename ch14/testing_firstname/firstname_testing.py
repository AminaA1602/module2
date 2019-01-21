# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 14:45:50 2019

@author: Skitt
"""
import json
import sqlite3 
conn = sqlite3.connect('firstnametest.db')
c = conn.cursor()

def create_table():
 c.execute('CREATE TABLE IF NOT EXISTS people(firstname TEXT)') 
 
data_people = open('data_people.json').read()
 
data = json.loads(data_people)
print(data)

for row in data:
     firstname = row["first_name"]
     print(firstname)

