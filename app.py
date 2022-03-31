#pylint: disable=invalid-name
#pylint: disable=missing-final-newline
#pylint: disable=line-too-long
#pylint: disable=unpacking-non-sequence
#pylint: disable=superfluous-parens
#pylint: disable=trailing-whitespace
#pylint: disable=wrong-import-order
#pylint: disable=unused-import
import os
import flask
import requests
from flask import flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask import request

from dotenv import find_dotenv, load_dotenv



load_dotenv(find_dotenv())


app = flask.Flask(__name__)
secret_key=os.getenv("SECRET_KEY")
app.secret_key = secret_key

    
