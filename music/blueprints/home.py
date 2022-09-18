from flask import  render_template,Blueprint
from flask import   request
search_input = Blueprint('search_input', __name__)
home = Blueprint('home', __name__)
@home.route('/')
def home_():
    return render_template("home.html")