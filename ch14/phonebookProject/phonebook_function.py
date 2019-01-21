# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 15:30:25 2019

@author: Skitt
"""
import sqlite3 
import json 
conn = sqlite3.connect('db/phonebook_function.db')
c = conn.cursor()

# ---------------- Creating a table -----------------#

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS business(business_name TEXT, address_line_1 TEXT, address_line_2 TEXT, address_line_3 TEXT, postcode TEXT, country TEXT, telephone_number TEXT, business_category TEXT)')

    c.execute('CREATE TABLE IF NOT EXISTS people(first_name TEXT, last_name TEXT, address_line_1 TEXT, address_line_2 TEXT, address_line_3 TEXT, postcode TEXT,country TEXT, telephone_number TEXT)'),
      
    c.execute('CREATE TABLE IF NOT EXISTS postcode(postcode TEXT, latitude TEXT, longitude TEXT)')  
create_table()
  
 # ------------- Populating the table ------------- #

def business_entry(): 
    for item in business_data:
       values_list=list(item.values())
       c.execute("INSERT INTO business(business_name,  address_line_1, address_line_2, address_line_3, postcode, country,telephone_number, business_category ) VALUES(?,?,?,?,?,?,?,?)", (values_list))
       conn.commit()
         
def people_entry(): 
   for item in people_data:
      values_list=list(item.values())
      c.execute("INSERT INTO people(first_name, last_name, address_line_1, address_line_2, address_line_3, postcode, country, telephone_number) VALUES(?,?,?,?,?,?,?,?)", (values_list))
      conn.commit()    

 # ---------- Storing the data in the table --------- #
    
def store_data_in_variable():
    global business_data
    global people_data
    with open('json/mock_data_business.js') as business:
        business_data=json.load(business) # -- Loding json file and assigning it a variable which you can feed into the table later on -- # 
    with open('json/mock_data_people.js') as people:
        people_data=json.load(people)
    return people_data, business_data 
        
#c.close()
#conn.close()