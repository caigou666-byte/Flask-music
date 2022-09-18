from flask import request, render_template,Blueprint
from flask import  session, redirect, url_for, request
from .DataBase.SQLite import DB
myCollection = Blueprint('myCollection', __name__)
def getMusicInformation(SQL):
    music_data = DB.Excute(SQL)
    return music_data
@myCollection.route('/myCollection')
def myCollection_():
    if request.method == 'GET':
        if 'username' in session:
            username = session['username']
            user_ID = getMusicInformation(
                "SELECT user_ID FROM UserInformation WHERE username='%s';" % (username))[0][0]
            data = getMusicInformation(
                "SELECT music_ID FROM numberOfMusicLovers WHERE user_ID='%s';" % (user_ID))
            music_data = []
            for i in data:
                music_data.append(getMusicInformation(
                    "SELECT * FROM musicResources WHERE ID='%s';" % (str(i[0])))[0])
            return render_template("myCollection.html", music_data=music_data, username_=username)
        return redirect(url_for('login.login_'))