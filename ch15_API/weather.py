# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 09:28:31 2019

@author: Skitt
"""

import requests 

endpoint = "http://api.openweathermap.org/data/2.5/weather"
payload = {"q": "London, UK", "units":"metric", "appid": "api.openweathermap.org/data/2.5/weather?id=2172797"}

response = requests.get(endpoint, params=payload)
data = response.json()

print (response.url)
print (response.status_code)
print (response.headers["content-type"])
print (data["main"])

temperature = data["main"]["temp"]
name = data["name"]
weather = data ["weather"][0]["main"]
print = (u"It\'s {}C in {}, and the sky is {}".format(temperature,name, weather))


