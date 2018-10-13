from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': "Евгений"}
    posts = [{"author": {"nick": "Юлька"},
              "body": "Привет, какашка"}]
    return render_template('index.html', posts=posts)
