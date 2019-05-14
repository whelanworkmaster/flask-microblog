from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Bill'}
    test_user1 = {'username': 'Jane'}
    test_user2 = {'username': 'Maria'}
    posts = [
        {
            'author': test_user1,
            'body': 'Having a great day today!'
        },
        {
            'author': test_user2,
            'body': 'I really hate Jane'
        },
        {
            'author': test_user2,
            'body': 'This is a different Maria!'
        }
    ]
    return render_template('index.html', title='Welcome to the Fun Zone', user=user, posts=posts)