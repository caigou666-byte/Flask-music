from flask import Flask,render_template
from .blueprints import init_blueprints
app = Flask(__name__)
@app.errorhandler(404)
def error_date(error):
    return render_template("404.html")
def create_app():
    app.secret_key = 'fkdjsafjdkfdlkjfadskjfadskljdsfklj'
    init_blueprints(app)
    return app
