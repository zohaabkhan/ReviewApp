#page navigation logic HERE


#pylint: disable=unused-import


import os
from app import app

import flask





@app.route("/")
def index():
    """
    method 
    """
    return flask.render_template("index.html")



@app.route("/signUp")
def signUp():
    """
    method
    """
    return flask.render_template("signUp.html")


@app.route("/login")
def login():
    """
    method 
    """
    return flask.render_template("login.html")


@app.route("/main_menu")
def main_menu():
    """
    method 
    """
    return flask.render_template("main_menu.html")




if __name__ == "__main__":
    app.run(
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 8080)),
        debug=True,
    )