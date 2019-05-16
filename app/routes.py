from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)