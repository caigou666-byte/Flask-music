from flask import request, render_template,Blueprint
from flask import  session, redirect, url_for, request
search_input = Blueprint('search_input', __name__)

@search_input.route('/search_input', methods=['GET', 'POST'])
def search_input_():
    if request.method == 'GET':
        if 'username' in session:
            return render_template("search.html")
        else:
            return redirect(url_for('login.login_'))