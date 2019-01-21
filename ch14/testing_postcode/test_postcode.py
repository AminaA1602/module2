# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 12:29:06 2019

@author: Skitt
"""

import sqlite3 
conn = sqlite3.connect('phonebook_function.db')
c = conn.cursor()

 # --- created a table with just the postcode ---#
#def create_table():
#    c.execute('CREATE TABLE IF NOT EXISTS test_postcode(postcode VARCHAR(15)')
#create_table()
 

# --- Reading and selecting from existing table ---- #

def get_postcode(): 
    c.execute("SELECT * FROM business")
    for row in c.fetchall():
        print(row)

#       current_postcode = row[0]
##      print(type(postcode))
#       print("current_postcode is: ", current_postcode)
#       check_postcode_exists(current_postcode)

get_postcode()
 
#def check_postcode_exists(current_postcode):
#    c.execute("SELECT postcode FROM practice WHERE postcode = ?", (current_postcode,))
#    results=c.fetchall()
#    print("result is: ",results)     
#    if len(results)<1: 
#        print("fetch API")
#        c.execute("INSERT INTO practice(postcode)VALUES(?)", (current_postcode,))
#        conn.commit()
#    else:
#        print("Got It")   
#          

