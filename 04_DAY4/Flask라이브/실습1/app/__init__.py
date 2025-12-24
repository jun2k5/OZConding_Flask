from flask import Flask
from .routes import todo_blp



def create_app():
    app=Flask(__name__)
    app.register_blueprint(todo_blp)

    return app











