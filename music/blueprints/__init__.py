#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .login import login
from .register import register
from .logout import logout
from .home import home
from .music import music
from .musicHall import musicHall
from .myCollection import myCollection
from .pearsonData import pearsonData
from .search import search
from .userlike import userlike
from .search_input import search_input

def init_blueprints(app):
    app.register_blueprint(blueprint=login)
    app.register_blueprint(blueprint=register)
    app.register_blueprint(blueprint=logout)
    app.register_blueprint(blueprint=home)
    app.register_blueprint(blueprint=music)
    app.register_blueprint(blueprint=musicHall)
    app.register_blueprint(blueprint=myCollection)
    app.register_blueprint(blueprint=pearsonData)
    app.register_blueprint(blueprint=search)
    app.register_blueprint(blueprint=userlike)
    app.register_blueprint(blueprint=search_input)