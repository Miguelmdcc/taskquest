from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.repository.user_repository import UserRepository

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/recrutamento', methods=['GET', 'POST']) 
def create_hero():
    if request.method == 'POST':
        real_name = request.form.get('real_name')
        hero_name = request.form.get('hero_name')

        user_repository = UserRepository()
        user = user_repository.create_user_if_not_exists(real_name, hero_name)

        if not user:
            flash('O herói já existe. Por favor, escolha outro nome.', 'error')
            return render_template('create_hero.html')

        return redirect(url_for('main.dashboard', name=real_name, hero=hero_name))
    
    return render_template('create_hero.html')

@main.route('/login', methods=['GET', 'POST']) 
def use_hero():
    if request.method == 'POST':
        real_name = request.form.get('real_name')
        hero_name = request.form.get('hero_name')

        user_repository = UserRepository()
        user = user_repository.get_user(real_name, hero_name)
        
        if not user:
            flash('O herói não existe. Por favor, crie um novo herói.', 'error')
            return render_template('use_hero.html')

        return redirect(url_for('main.dashboard', name=real_name, hero=hero_name))
    
    return render_template('use_hero.html')

@main.route('/dashboard')
def dashboard():
    name = request.args.get('name')
    hero = request.args.get('hero')

    return render_template('dashboard.html', hero_name=hero)

@main.route('/create-task')
def create_task():
    flash('Task criada com sucesso!', 'success')
    return render_template('dashboard.html')