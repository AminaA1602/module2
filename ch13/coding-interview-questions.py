# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 13:52:21 2019

@author: Skitt
"""
import string 
string.ascii_lowercase

#--- Step 1: Write the letters 'A' to 'Z' (in upper case) to the console, placing each letter on a new line ----#

#---- What not to do-- # alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 
  
list(string.ascii_uppercase)
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

alphabet = list(string.ascii_lowercase)

for i in alphabet :
    print(i)

#--- Step 2: For every third letter, write it to the console in lowercase instead. ---#
        
import string 
alphabetstring = list(string.ascii_uppercase)
alphabet = list(string.ascii_uppercase)

alphabet[2: :3] = [x.upper() for x in alphabet[2::3]]#
alphabetstring = ' '.join(alphabet)

#for i in alphabet: 
#    if i in alphabet [0:26:2]:
#        print(i.lower())  
        
        
    