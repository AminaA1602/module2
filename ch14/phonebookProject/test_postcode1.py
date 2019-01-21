# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 13:28:32 2019

@author: Skitt
"""

import sqlite3 
import json

conn = sqlite3.connect('phonebook_function.db')
c = conn.cursor()

 # --- created a table with just the postcode ---#
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS test_postcode(postcode VARCHAR(15)')
  
    
with open('json/mock_data_people.js') as people:
       people_data = json.load(people)
       
with open('json/mock_data_business.js') as business:
       business_data = json.load(business)


def getUniquePostcode():  
    pc = []
    for item in people_data:
        print(item['postcode'])
        pc.append((item['postcode']))  
    for item in business_data:
        print(item['postcode'])
        pc.append((item['postcode']))   
        
    unique_pc = set(pc) # --- > This is currently a set 
    unique_list = list(unique_pc) # --- > This is now a list
    return unique_list 
print(getUniquePostcode())
    
# To do: Get longitude and latitude    
    
    
    