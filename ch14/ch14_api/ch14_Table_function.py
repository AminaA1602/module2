# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 09:43:02 2019

@author: Skitt
"""

# --------- Task 1: Create a table and insert data ------------ # 

import sqlite3 
conn = sqlite3.connect('task1.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToBuild(unix REAL, datestamp TEXT, keyword TEXT, value REAL)') #-- A table has been created but it's currently empty. So far, it's only got a data frame but no real/actual data --#
    
    
def data_entry():
    c.execute("INSERT INTO stuffToBuild VALUES(142233222, '2018-01-01','python', 5)")
conn.commit()
#c.close()
#conn.close()

create_table()
data_entry()

#------------------ Task 2: Add data to your table with varaibles ---------------- # 
import sqlite3 
import sqlite3
import time 
import datetime
import random 

def dynamic_data_entry():
     unix = time.time()
     date=str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d%H:%M:%S'))
     
     keyword = 'Python'
     value = random.randrange(0,10)
     c.execute('INSERT INTO stuffToBuild(unix, datestamp, keyword,value)VALUES(?, ?, ?, ?)', (unix, date, keyword,value))
     conn.commit()

for i in range(10):
    dynamic_data_entry()
    time.sleep(1)
c.close()
conn.close()

#------------ Task 3: Read and select data from database ---------- # 

def read_db_all():
    c.execute('SELECT * FROM stuffToBuild WHERE value=8 ')
for row in c.fetchall():
    print(row)

def read_from_db2():
    c.execute('SELECT * FROM stuffToBuild WHERE value =8 and unix > 154348733 and unix < 1534855741 ')

    for row in c.fetchall():
        print(row[0])



