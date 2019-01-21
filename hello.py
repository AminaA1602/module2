# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 09:59:34 2019

@author: Skitt
"""

# ---------------- Importing Flask -----------------#
 
#from flask import Flask
#app = Flask("MyApp")
#@app.route("/bio")
#def hello():
#    return "Hello World"
#app.run(debug=True)

# ---------- Using render_template function -----------#

from flask import Flask, render_template 
app = Flask("MyApp")
@app.route("/news")
def hello():
    return "Hello World"
app.run(debug=True)

# ---------- Serving html file with Flask -----------#

@app.route("/<name>")
def hello_someone(name):
    return render_template("hello.html", name=name.title())





