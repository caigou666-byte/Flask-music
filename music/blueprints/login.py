
from flask import Blueprint, request, render_template
from flask import Blueprint
from .DataBase.SQLite import DB
from flask import Flask, session,request
import validators
login = Blueprint('login', __name__)

@login.route('/login',methods=['GET','POST'])
def login_():
    if request.method=='GET':
        return render_template("login.html")
    elif request.method=='POST':
        print(request.form.get("username"))
        print(request.form.get("password"))
        if validators.email(request.form.get("username")):
            if int(DB.Excute("SELECT COUNT(*) FROM UserInformation WHERE email='%s';"%(request.form.get("username")))[0][0])<=0:
                return "UserDoesNotExist"
            elif DB.Excute("SELECT sha256 FROM UserInformation WHERE email='%s';"%(request.form.get("username")))[0][0]==request.form.get("password"):
                session['username'] = DB.Excute("SELECT username FROM UserInformation WHERE email='%s';"%(request.form.get("username")))[0][0]
                return "LoginSucceeded"
            else:
                return "PasswordError"            
        elif int(DB.Excute("SELECT COUNT(*) FROM UserInformation WHERE username='%s';"%(request.form.get("username")))[0][0])<=0:
            return "UserDoesNotExist"
        elif DB.Excute("SELECT sha256 FROM UserInformation WHERE username='%s';"%(request.form.get("username")))[0][0]==request.form.get("password"):
            session['username'] = request.form['username']
            return "LoginSucceeded"
        else:
            return "PasswordError"    