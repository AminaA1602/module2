# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 10:12:54 2018

@author: Skitt
"""
phonebook = {}
phoneBook = {'Amina':[599, 4,'E17','London',20] 
             'Leanne':[721, 26,'NW12','Edinburgh',35]
             'Pam':[322,37,'SE17','Cardiff',30]
             'Katie':[321,19,'E15','Bristol',]}
users = 0
while users < 4:
       print("-" * 50 )
#        queens_age = 92
       print('Welcome and Thank you classmate\n for taking part in our survey ')
       name = input("What's your name? ")
       print('\nA warm welcome {}' .format(name))
       LastthreeDigits = input("What is the last 3 digits of your phone number? ")
       luckyNumber = input("What is your luckiest of ever number? \n You know you have one..... ")
       age = int(input("What be your age? "))
       print('Don\'t worry we\'re not using these numbers for our lottery tickets!')
       city = input("Whereabouts are you living these days,\njust the name of the place will do.  ")
       postcode = input('\nLast but not least......\n What is the first letter of your postcode?')
       users = users + 1
       if users == 4:
           print("Thank you for entering these details.")
       return phoneBook

phoneBook[name.title()] = LastthreeDigits, luckyNumber, postcode, city, age


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
    phoneBook = name(phoneBook)
    
    sortbyName(phoneBook)
    sortbyluckyNumber(phoneBook)
    sortbyCity(phoneBook)


#This is a dictionary called phoneBook
#phoneBook = {}

#Everything in the square bracket is a list. 'Amina' is the item and everything after : is the value.#

phoneBook_run(phoneBook)







