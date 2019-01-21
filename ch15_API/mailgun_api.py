# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:04:11 2019

@author: Skitt
"""

# ------- Task 1 : using mailgun API to send an email ------ # 

import config
import requests 

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox2c7ac8253379410383b2c87119e3e858.mailgun.org/messages", # -- domain name --# 
        auth=("api", config.api_key), 
        # -- Key -- #
        data={"from": "Myself Amina <aminaaweis1150@gmail.com>",
              "to": ["skittlesforlife12@gmail.com"],
              "subject": "Hello Amina",
              "text": "Congratulations Amina, you just sent an email with Mailgun!  You are truly awesome!"})

send_simple_message()