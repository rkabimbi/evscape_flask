

# LANCER AVEC flask run

from my_app import app
from flask import Flask, redirect
from flask import request
from flask import render_template
from jinja2 import Template
from jinja2 import Environment, PackageLoader
from jinja2 import environment
from random import randint
import math

from my_app import db #import de la db

#from my_app.models.riddle import Enigmes, EnigmesJsn #import de la table (de la classe contenant la table)
#from my_app.forms.RiddleForm import EnigmeForm, ReponseForm

from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from flask import url_for
from flask import flash
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, date

from flask import json, jsonify



from datetime import date
#from dateutil.relativedelta import *#pour calculer age

#from my_app.models.riddleJSN import EnigmesJsn







#gere la page d'acceuil
@app.route("/", methods=['GET','POST'])
#login_required #pour obliger que l'utilisateur soit# log
def fonction_login():
    return render_template("game.html",currentUser=None)

