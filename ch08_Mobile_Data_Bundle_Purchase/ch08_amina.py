# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:59:39 2018

@author: Skitt
"""


def DataBundlePurchase(truePasscode, balance):
    if passwordCheck(truePasscode):
        return 'Password OK'
    else: 
        return 'Wrong password'
        
    
def passwordCheck(truePasscode):
    attempt = input('Please enter your password ')
    if attempt == truePasscode: 
        return True
    else: 
        return False