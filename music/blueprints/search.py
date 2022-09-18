from flask import request, render_template,Blueprint
from flask import  session, redirect, url_for, request
from .DataBase.SQLite import DB
search = Blueprint('search', __name__)

def getMusicInformation(SQL):
    music_data = DB.Excute(SQL)
    return music_data
@search.route('/search', methods=['POST'])
def search_():
    if request.method == 'POST':
        if 'username' in session:
            username = request.form.get("username")
            KeyWord_ = request.form.get("KeyWord_")
            SQL = "SELECT * FROM musicResources WHERE music_name LIKE'%%%s%%' OR author LIKE'%%%s%%' or album LIKE'%%%s%%' limit 50;" % (
                KeyWord_, KeyWord_, KeyWord_)
            data = getMusicInformation(SQL)
            return render_template("search_result.html", music_data=data, username_=username)
        else:
            return redirect(url_for('login.login_'))