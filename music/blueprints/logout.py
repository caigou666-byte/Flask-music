from flask import Blueprint
from flask import  session, redirect, url_for, request
logout = Blueprint('logout', __name__)
@logout.route('/logout')
def logout_():
    session.pop('username', None)
    return redirect(url_for('first.login'))