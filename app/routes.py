from flask import render_template, flash, redirect
from app import app
from app.forms import RegisterForm, LoginForm, HomeSearchGames

@app.route('/', methods=['GET', 'POST'])
def index():
    form = HomeSearchGames()
    games = {
        'coming_soon': ['Flower Picking Sim', 'Frog Stomp'],
        'out_now': ['Tank Busters', 'Kitty with a Kite']
    }
    if form.validate_on_submit():
        flash(f'Your search for {form.game_title} successful')
        flash(f'Your search for {form.genre} successful')
        flash(f'Your search for {form.rating} successful')
        return redirect('/')
    return render_template('home.jinja', games=games, form=form, title='Home')

@app.route('/about')
def about():
    return render_template('about.jinja')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'Request to register {form.first_name} successful')
        flash(f'Request to register {form.last_name} successful')
        flash(f'Request to register {form.username} successful')
        flash(f'Request to register {form.email} successful')
        return redirect('/')
    return render_template('/register.jinja', form=form)

@app.route('/login', methods=['GET', 'POST'])
def sign_in():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'{form.email} Sign in was successful')
        return redirect('/')
    return render_template('/login.jinja', form=form)

@app.route('/blog')
def blog():
    return render_template('/blog.jinja')