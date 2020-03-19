from flask import Flask

def create_app():
    """
    Creates application
    :return: app
    """
    app = Flask(__name__)
    with app.app_context():
        from . import routes
        return app