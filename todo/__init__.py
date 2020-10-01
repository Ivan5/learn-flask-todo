import os

from flask import Flask

def create_app():
  app = Flask(__name__)
  app.config.from_mapping(
    SECRET_KEY='mikey',
    DATABASE_HOST='localhost',
    DATABASE_PASSWORD='',
    DATABASE_USER='root',
    DATABASE='todo_flask'
  )

  from . import db

  db.init_app(app)

  from . import auth
  from . import todo

  app.register_blueprint(auth.bp)
  app.register_blueprint(todo.bp)

  @app.route('/hola')
  def hola():
    return 'Chanchito Feliz'

  return app