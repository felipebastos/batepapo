from flask import Flask
import click

from flask.cli import with_appcontext
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

loginmanager = LoginManager()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///batepapo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    app.secret_key = '123456'

    # configurações de plugins
    loginmanager.init_app(app)
    db.init_app(app)

    app.cli.add_command(init_db)

    with app.app_context():
        from batepapo import rotas

    return app

@click.command('init-db')
@with_appcontext
def init_db():
    from . import entidades
    db.create_all()
    print('Criado com sucesso')