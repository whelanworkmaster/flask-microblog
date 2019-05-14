from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Bill'}
    return render_template('index.html', title='Welcome to the Fun Zone', user=user)