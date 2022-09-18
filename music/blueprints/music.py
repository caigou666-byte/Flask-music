from flask import request, render_template,Blueprint
from flask import  session, redirect, url_for, request
from .DataBase.SQLite import DB
music = Blueprint('music', __name__)
def getMusicInformation(SQL):
    music_data = DB.Excute(SQL)
    return music_data

@music.route('/music', methods=['GET', 'POST'])
def music_():
    if request.method == 'GET':
        if 'username' in session:
            music_data = getMusicInformation(
                "SELECT *FROM musicResources limit 50;")
            return render_template("card.html", music_data=music_data)
        return redirect(url_for('login.login_'))