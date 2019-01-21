# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:04:11 2019

@author: Skitt
"""

import requests 

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox2c7ac8253379410383b2c87119e3e858.mailgun.org/messages", # -- domain name --# 
        auth=("api", "8015ce218130fce084f2471c26ef357f-060550c6-dc22e098"), 
        # -- Key -- #
        data={"from": "Myself Amina <aminaaweis1150@gmail.com>",
              "to": ["skittlesforlife12@gmail.com"],
              "subject": "Hello Amina",
              "text": "Congratulations Amina, you just sent an email with Mailgun!  You are truly awesome!"})

send_simple_message()