# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 09:45:44 2019

@author: Skitt
"""

def DataBundlePurchase(truePasscode, balance):
    if passwordCheck(truePasscode):
        option=transaction()
        if option == "1":
            displayBalance(balance)
            return "display balance"
        elif option == "db":
            print("Before you can buy data we need to check your phone number.")
            if validateNumbers():
                purchaseDatabundle(balance)
            return 'databundle purchase'
        elif option == "tb":
            topUp(balance)
            return 'topUp'
        else:
            return "Sorry I didn't get that, please start again"
    else:
        return "Wrong password"
    
#------------- Checking user password -------------#
        
def passwordCheck(truePasscode):
    attempt = input("Please enter your password ")
    if attempt == truePasscode:
        return True
    else: 
        return False
    
            ##--Checking balance--## 
        
def checkBalance(balance):
    if balance > 0:
        return True
    else:
        return False
    
# ------- Type of transaction ------ # 
        
def transaction():
    option_type =int(input('1. check balance, 2. Purchase bundle, 3. Top up your account'))
    option = input("").lower()
    return option
    return option_type
 
#--------Display balance to user their balance-------#
     
def displayBalance(balance):
    if checkBalance(balance):
        print("Your balance is {}".format(balance))
    
    else:
        print("Your balance is not sufficient: {}".format(balance))
        
# ---- Purchasing data function if balance insufficient you can topUp ----- #
        
def purchaseDatabundle(balance):
    purchaseCompleted=False
    while not purchaseCompleted:
        print("Your current balance is {}".format(balance))
        dataPurchase = input("How much money would you like to spend on purchasing data? ")
        
        dataPurchase=int(dataPurchase)
        if dataPurchase >= balance:
            topbalance=input("Your balance is insufficient for this purchase. Would you like to top up? (please type yes or no ")
            if topbalance [0]== "y":
                balance=topUp(balance)
        elif dataPurchase > 100:
            print("You cannot purchase more that £100 worth of data.")
        elif dataPurchase%5!=0:
            print("You have to top up by a multiple of 5.")
        else:
            newBalance=round(balance-dataPurchase, 2)
            purchaseCompleted=True
            print("Your new balance is {}".format(newBalance))
            
    if dataPurchase <= balance and dataPurchase <= 100 and dataPurchase%5==0:
        newBalance=round(balance-dataPurchase, 2)
        print("Your new balance is {}".format(newBalance))
    elif dataPurchase <= balance and dataPurchase > 100:
        print("You cannot purchase more that £100 worth of data.")
        
    elif dataPurchase >= balance:
        print("Your balance is insufficient for this purchase. Please top up.")
            
            
            
#--Validate user number twice function using loop--#
            
def validateNumbers():  
    numbers=checkDataTypeOfNumbers()      
    if numbers[0]==numbers[1]:
        return True
    else:
        print("You need to enter the correct phone number twice in order to proceed. Please try again ")
        numbers=checkDataTypeOfNumbers()
        validateNumbers()
        
def checkDataTypeOfNumbers():
    while True:
        try:
            phoneOne=int(input("Please enter your phone number. "))
            
        except ValueError:
            print("Please type a number! ")
            
        else:
            break
    while True:
        try:
            phoneTwo=int(input("Please enter your phone number. "))
            
        except ValueError:
            print("Please type a number! ")
        else:
            break
    return phoneOne, phoneTwo           

    
##--Topping up account function--##
    
def topUp(balance):
    print("Your balance is {}".format(balance))
    topUpbalance=input("How much would you like to to top up your balance by? ")
    flotopUpbalance=float(topUpbalance)
    newtopUpbalance = round(balance + flotopUpbalance, 2)
    print("Your new balance is {}".format(newtopUpbalance))
    return newtopUpbalance