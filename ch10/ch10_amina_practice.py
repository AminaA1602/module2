# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 10:12:54 2018

@author: Skitt
"""


def addClassmate(phoneBook):
    name = input('what\'s your name? ')
    luckyNumber = int(input('what\'s your lucky number? '))
    LastthreeDigits = input('What is the last three digits of your phone number? ')
    postcode = input('what\'s your postcode? ')
    city = input('What city do you live in? ')
    age = int(input('How old are you? '))    
    
    phoneBook[name.title()] = LastthreeDigits, luckyNumber, postcode, city, age
    return phoneBook

def sortbyName(phoneBook):
    sortedbyname = sorted(phoneBook.items(), key=lambda kv:kv[0])
    print('\n', sortedbyname)

#the key= is referring to how the variable is going to be sorted. In this case, key is referring to how sortedbyname is going to be sorted. 
#kv:kv is the index within the item that it will be looking at/referencing/targeting. 

def sortbyluckyNumber(phoneBook):
    sortedbyluckyNumber = sorted(phoneBook.items(), key=lambda kv:kv[1][1])
    print('\n', sortedbyluckyNumber)


def sortbyCity(phoneBook):
    sortedbycity = sorted(phoneBook.items(), key=lambda kv:kv[1][3])
    print('\n', sortedbycity)



def phoneBook_run(phoneBook):
    phoneBook = addClassmate(phoneBook)
    
    sortbyName(phoneBook)
    sortbyluckyNumber(phoneBook)
    sortbyCity(phoneBook)


#This is a dictionary called phoneBook
phoneBook = {}
#phoneBook = {'Amina':[599, 4,'E17','London',20] 
#             'Leanne':[721, 26,'NW12','Edinburgh',35]
#             'Pam':[322,37,'SE17','Cardiff',30]
#             'Katie':[321,19,'E15','Bristol',]}
#Everything in the square bracket is a list. 'Amina' is the item and everything after : is the value.#

phoneBook_run(phoneBook)







