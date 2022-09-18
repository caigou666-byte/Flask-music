from flask import request, render_template,Blueprint
from flask import  session, redirect, url_for, request
from .DataBase.SQLite import DB
musicHall = Blueprint('musicHall', __name__)
def getMusicInformation(SQL):
    music_data = DB.Excute(SQL)
    return music_data
@musicHall.route('/musicHall')
def musicHall_():
    if request.method == 'GET':
        if 'username' in session:
            username = session['username']
            music_data = getMusicInformation(
                "SELECT * FROM `musicResources` ORDER BY RANDOM() limit 35;")
            user_ID = getMusicInformation(
                "SELECT user_ID FROM UserInformation WHERE username='%s';" % (username))[0][0]
            like = []
            for i in music_data:
                count = getMusicInformation(
                    "SELECT count(music_ID) FROM numberOfMusicLovers WHERE user_ID='%s' and music_ID='%s';" % (user_ID, i[0]))[0][0]
                if int(count) >= 1:
                    like.append("1")
                else:
                    like.append("0")
            return render_template("musicHall.html", music_data=music_data, username_=username, music_like=like)
        return redirect(url_for('login.login_'))