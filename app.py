from flask import Flask
app =Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome "

from controller import user_controller