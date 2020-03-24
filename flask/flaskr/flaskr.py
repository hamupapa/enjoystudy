# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash

# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application :)
app = Flask(__name__)
# 与えられたオブジェクト内で大文字の変数をすべて取得する
app.config.from_object(__name__)

def connect_db():
  return sqlite3.connect(app.config['DATABASE'])

# データベースを作成する
def init_db():
  with closing(connect_db()) as db:
    with app.open_resource('schema.sql') as f:
      db.cursor().executescript(f.read())
    db.commit()

@app.before_request
def before_request():
  g.db = connect_db()

@app.after_request
def after_request(response):
  g.db.close()
  return response

@app.route('/')
def show_entries():
  cur = g.db.execute('select title, text from entries order by id desc')
  entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
  return render_template('show_entries.html', entries=entries)


if __name__ == '__main__':
  app.run()

