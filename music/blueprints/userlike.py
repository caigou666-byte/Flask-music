from flask import request, render_template,Blueprint
from flask import  session, redirect, url_for, request
from .DataBase.SQLite import DB
userlike = Blueprint('userlike', __name__)
def getMusicInformation(SQL):
    music_data = DB.Excute(SQL)
    return music_data
@userlike.route('/user/like', methods=['POST'])
def userlike_():
    if request.method == 'POST':
        if 'username' in session:
            username = request.form.get("username")
            music_ID = request.form.get("music_ID_")
            status = request.form.get("status")
            user_ID = getMusicInformation(
                "SELECT user_ID FROM UserInformation WHERE username='%s';" % (username))[0][0]
            if status == "unlike":
                DB.Submit_For_Execution(
                    "DELETE FROM numberOfMusicLovers WHERE user_ID='%s' AND music_ID='%s';" % (user_ID, music_ID))
                return "OK"
            elif status == "like":
                DB.Submit_For_Execution(
                    "INSERT INTO numberOfMusicLovers(user_ID,music_ID)VALUES('%s','%s');" % (user_ID, music_ID))
                return "OK"
            else:
                count = getMusicInformation(
                    "SELECT count(music_ID) FROM numberOfMusicLovers WHERE user_ID='%s' and music_ID='%s';" % (user_ID, music_ID))[0][0]
                if int(count) >= 1:
                    return "1"
                else:
                    return "0"
        else:
            return redirect(url_for('login.login_'))