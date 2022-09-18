from flask import Blueprint,render_template
from flask import request
from .DataBase.SQLite import DB
register = Blueprint('register', __name__)
@register.route('/register',methods=['GET','POST'])
def register_():
    if request.method=='GET':
        return render_template("register.html")
    elif request.method=='POST':
        print(request.form.get("username"),request.form.get("password"),request.form.get("email"))
        if int(DB.Excute("SELECT COUNT(*) FROM UserInformation WHERE email='%s';"%(request.form.get("email")))[0][0])>0:
            return "MailboxAlreadyExists" 
        if int(DB.Excute("SELECT COUNT(*) FROM UserInformation WHERE username='%s';"%(request.form.get("username")))[0][0])>0:
            return "AccountNumberAlreadyExists" 
        else:
            DB.Submit_For_Execution("INSERT INTO UserInformation(username,sha256,email)VALUES('%s','%s','%s');"%(request.form.get("username"),request.form.get("password"),request.form.get("email")))       
        return "success"    
    
