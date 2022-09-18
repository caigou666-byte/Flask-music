from flask import request, render_template,Blueprint
from flask import  session, redirect, url_for, request
pearsonData = Blueprint('pearsonData', __name__)
@pearsonData.route('/pearsonData')
def pearsonData_():
    if request.method == 'GET':
        if 'username' in session:
            username = session['username']
            return render_template("pearsonData.html", username_=username)
        return redirect(url_for('login.login_'))