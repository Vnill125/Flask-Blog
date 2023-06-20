from flask import render_template, flash, redirect, url_for
from flaskblog import app, db , bc
from flaskblog.models import User, Post
from flaskblog.forms import RegistrationForm, LoginForm
from flask_bcrypt import generate_password_hash

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(username = form.username.data, password = hashed_password, email = form.email.data)
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form.email.data)

@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "kris125132@gmail.com" and form.password.data == "rok321": 
            return redirect(url_for('home'))
        
    return render_template("login.html", title="Login",  form=form)
    
    
