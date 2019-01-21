# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:34:54 2019

@author: Skitt
"""

# ------- Task 2 : Getting current weather information ------ # 

import requests 

endpoint = "http://api.openweathermap.org/data/2.5/weather"

payload = {"q": "London,UK", "units":"metric", "appid":"dffcf8833571226ae5c8f08c498f4060"}

response = requests.get(endpoint,params=payload)

data = response.json()

print(data)  
print('this is what data looks like \n')
print(response.url)
print(response.status_code)
print (response.headers["content-type"])

temperature = data["main"]["temp"]
name = data["name"]
weather = data["weather"][0]["main"]
print (u"It\'s {}, and the sky is {}".format(temperature,name, weather))