from flask import Flask

def create_app():
    app = Flask(__name__)

    app.secret_key = '123456'

    with app.app_context():
        from batepapo import rotas

    return app