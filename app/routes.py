from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/recrutamento', methods=['GET', 'POST']) 
def create_hero():
    if request.method == 'POST':
        real_name = request.form.get('real_name')
        hero_name = request.form.get('hero_name')

        return redirect(url_for('main.dashboard', name=real_name, hero=hero_name))
    
    return render_template('create_hero.html')

@main.route('/dashboard')
def dashboard():
    name = request.args.get('name')
    hero = request.args.get('hero')

    return render_template('dashboard.html', hero_name=hero)