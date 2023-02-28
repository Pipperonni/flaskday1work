from flask import render_template
from app import app
from app.forms import RegisterForm

@app.route('/')
def index():
    games = {
        'coming_soon': ['Flower Picking Sim', 'Frog Stomp'],
        'out_now': ['Tank Busters', 'Kitty with a Kite']
    }
    return render_template('home.jinja', games=games, title='Home')

@app.route('/about')
def about():
    return render_template('about.jinja')

@app.route('/register')
def register():
    form = RegisterForm()

    return render_template('/register.jinja', form=form)

@app.route('/login')
def sign_in():
    return render_template('/login.jinja')

@app.route('/blog')
def blog():
    return render_template('/blog.jinja')