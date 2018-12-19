# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:59:39 2018

@author: Skitt
"""

#This is an empty function

#Step 1 - the user is enetering their password 
def DataBundlePurchase(truePasscode, balance):
    if passwordCheck(truePasscode):
        selection = options()
#This is a function calling the options once the password has been entered. It is followed by an if statement and the result of it as displayed, shows that when you choose option 2. it prints out your balance. 
        if selection == "1":
            return ('Your balance is: {}'.format(balance))
        elif selection == "2":
            checkPhoneNumber()
        else:
            print("go back to main menu")    
    else: 
        return 'Wrong password'
 
#In the case that the user enters the wrong password, they have to enter it again. If they continue to enter it incorrectly, then they will have to do the same again.        
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
    
#This is step 2 essentially - the user has finally entered their passowrd and is now being given the option to either check their balance or buy data. Whatever option they choose will be displayed in the return selection. 
def options():
    print('What would you like to do?')
    print ("1. Check your balance")
    print ("2. Buy Data")
    selection = input()
    return selection
            
#Step 3 - the user has chosen to buy more data but now has to enter their phone number and verify it before continuing. 
    
def buyData(balance):
    print('It\'s great that you want to buy data from us! Before you can continue please eneer the following: ')
    checkPhoneNumber()

#The function for this is CheckPhoneNumber():    
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

def purchaseData(balance):
       #ask the user how much they want 
       #check their balance 
       #compare the amount 
       #
       
        
    
