# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:59:39 2018

@author: Skitt
"""

#This is an empty function

def DataBundlePurchase(truePasscode, balance):
    if passwordCheck(truePasscode):
        selection = options()
        if selection == "1":
            return ('Your balance is: {}'.format(balance))
        elif selection == "2":
            buyData(balance)
        else:
            print("go back to main menu")
    

        
    else: 
        return 'Wrong password'
        
def passwordCheck(truePasscode):
    attempt = input('Please enter your password ')
    if attempt == truePasscode: 
        return True
    else: 
        return False
    
def checkBalance(balance):
    if balance > 0:          
        return True
    else:
        return False
    

def options():
    print('What would you like to do?')
    print ("1. Check your balance")
    print ("2. Buy Data")
    selection = input()
    return selection
        

#Buydata = input 

def buyData(balance):
    print('It\'s great that you want to buy data from us! Before you can continue please eneer the following: ')
    checkPhoneNumber()

    
def checkPhoneNumber():
    print('Please enter you phone: ')
    phoneNumberOne = input()
    print('Please enter you phone number again: ')
    phoneNumberTwo = input()
    
    if phoneNumberOne == phoneNumberTwo:
        return True
    else:
        print('Didn\'t match')
        checkPhoneNumber()
#recursion-calling the function within itself e.g. here we are calling the function checkPhoneNumber(): again if the user eneters the password incorrectly so it can go back to the question again. 
        
        
        
    
