from flask import Flask,render_template
from flask_bootstrap import Bootstrap
def login(user,password):
    return render_template('login.html')