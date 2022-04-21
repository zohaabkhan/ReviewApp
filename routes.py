#pylint: disable=invalid-name
#pylint: disable=missing-final-newline
#pylint: disable=line-too-long
#pylint: disable=unpacking-non-sequence
#pylint: disable=superfluous-parens
#pylint: disable=trailing-whitespace
#pylint: disable=wrong-import-order
#pylint: disable=unused-import
#pylint: disable=invalid-envvar-default



from requests import session
from app import app, db
import random
import os

import flask
from flask_login import login_user, current_user, LoginManager, logout_user
from flask_login.utils import login_required
from models import User
from quizzes import QUIZ1,QUIZ2,QUIZ3



login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    """
    function to handle user login 
    """    
    return User.query.get(int(id))

@app.route("/")
def main():
    """
    function to bring users to the Landing page
    before the login page

    """
    return flask.render_template("Landing.html")

@app.route("/signup")
def signup():
    """
    function to handle user sign up
    """
    return flask.render_template("signup.html")


@app.route("/signup", methods=["POST"])
def signup_post():
    """
    doc string: user sign up routing
    """
    username = flask.request.form.get("username")
    email = flask.request.form.get("email")
    password = flask.request.form.get("password")
    fullname = flask.request.form.get("password")
    
    user = User.query.filter_by(username=username).first()
    if user:
        pass
    else:
        user = User(username=username, email=email, fullname=fullname)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

    return flask.redirect(flask.url_for("login"))


@app.route("/login")
def login():
    """
    doc string: user login
    """
    return flask.render_template("login.html")


@app.route("/login", methods=["POST"])
def login_post():
    """
    doc string: login navigation
    """
    username = flask.request.form.get("username")
    password = flask.request.form['password']
    user = User.query.filter_by(username=username).first()
    
    if user:
        login_user(user)
        return flask.redirect(flask.url_for("index"))

    else:
        return flask.jsonify({"status": 401, "reason": "Username or Password Error"})


@app.route("/landing")
def landing():
    """
    doc string: landing page navigation
    """
    if current_user.is_authenticated:
        return flask.redirect("index")
    return flask.redirect("login")


@app.route("/logout")
def logout():
    """
    doc string: user logout naviagtion
    """
    logout_user()
    return flask.redirect("/")


@app.route("/index")
@login_required
def index():
    """
    doc string: render menu page
    """
    return flask.render_template(
        "index.html",
    )

@app.route("/summary")
def summary():
    """
    doc string: summary
    """
    return flask.render_template("summary.html")    

@app.route("/videos")
def videos():
    """
    doc string: Videos
    """
    return flask.render_template("videos.html")  

@app.route("/eir")
def eir():
    """
    function to handle user EIR
    """
    return flask.render_template("eir.html")



@app.route("/quiz", methods=["GET","POST"]) #this page is the root endpoint
def quiz3():
    """
    this function controls Quiz#3
    """
    quiz3 = { 
        # list containing quiz questions and their answers
        "lecture": " 3: Python, Debugging",
        "question_1": "1. True or False: When you search for a video on Youtube, you are sending a request from the client to the server. The client is asking the Youtube server to get all the videos about a search topic. The server, then runs some processes on the search topic and returns all the data it found to the client.",
        "answer_1": "True",
        "question_2": "2. True or False: The frontend and the server tend to run together & the backend and the client tend to run together.",
        "answer_2": "False",
        "question_3": "3. True or False: The front end is NOT: JavaScript, HTML, CSS.",
        "answer_3": "False",
        "question_4": "4. True or False: Python controls all of its flow through indentation.",
        "answer_4": "True"}
      
    
    temp=quiz3
    lect = temp.get("lecture")
    q1 = temp.get("question_1")
    q2 = temp.get("question_2")
    q3 = temp.get("question_3")
    q4 = temp.get("question_4")

    a = temp.get("answer_1")
    b = temp.get("answer_2")
    c = temp.get("answer_3")
    d = temp.get("answer_4")

    return flask.render_template("quiz.html",lect=lect,q1=q1,q2=q2,q3=q3,q4=q4,a=a,b=b,c=c,d=d)    

   


@app.route("/results", methods=["GET","POST"]) #this page is the root endpoint
def results():
    """
    this function calculates quiz score and renders a quiz feedback message
    """

    if flask.request.method =="POST":
        data1 = flask.request.form.get("num1") #tells what to do with the form data
        data2 = flask.request.form.get("num2") #retrieves the user's answer for question#2
        data3 = flask.request.form.get("num3") #retrieves the user's answer for question#3
        data4 = flask.request.form.get("num4") #retrieves the user's answer for question#4


        feedback1=data1 #assign the retrieved form data to a variable
        feedback2=data2
        feedback3=data3
        feedback4=data4
    
        miss2=0
        miss3=0
        miss4=0

        if(feedback1=="a"): #checks if the user entered the correct answer for question#1
            point1=25       #if the answer is correct; the user earns 25 points for question#1
            miss1=0         #the user did not miss this question
        else:
            point1=0         #the answer was incorrect; the user does not earn points for question#1
            miss1=1          #the user has missed one question
        if(feedback2=="b"): #checks if the user entered the correct answer for question#2
            point2=25       #if the answer is correct; the user earns 25 points for question#2
            miss2=0         
        else:
            point2=0         #the answer was incorrect; the user does not earn points for question#2
            miss2=1
        if(feedback3=="c"): #checks if the user entered the correct answer for question#3
            point3=25       #the answer is correct; the user earns 25 points for question#3
            miss3=0         #the user did not miss this question
        else:
            point3=0         #the answer was incorrect; the user does not earn points for question#3
            miss3=1
        if(feedback4=="d"): #checks if the user entered the correct answer for question#4
            point4=25       #if the answer is correct; the user earns 25 points for question#4
            miss4=0         #the user did not miss this question
        else:
            point4=0        #the answer was incorrect; the user does not earn points for question4
            miss4=1         #the user missed this question

        score = point1+point2+point3+point4     #the sum of the points earned is the score
        missed = miss1+miss2+miss3+miss4        #the sum of the number ofmissed questions

        if(score==100):                         #logic to display a perfect score quiz feedback
            return flask.render_template("feedback_greatjob.html")
        else:                                   #logic to display quiz feedback results that are less than 100% score 
            return flask.render_template("feedback_improve.html",score=score,missed=missed)      

 
    return flask.render_template("feedback_improve.html",feedback1=feedback1,feedback2=feedback2,feedback3=feedback3)   
    



if __name__ == "__main__":
    app.run(
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 8080)),
        debug=True,
    )
