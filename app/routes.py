from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.repository.user_repository import UserRepository
from app.use_cases.create_user import createUserUseCase
from app.use_cases.login_user import loginUserUseCase

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/recrutamento', methods=['GET', 'POST']) 
def create_hero():
    return createUserUseCase(request)

@main.route('/login', methods=['GET', 'POST']) 
def use_hero():
    return loginUserUseCase(request)

@main.route('/dashboard')
def dashboard():
    name = request.args.get('name')
    hero = request.args.get('hero')

    return render_template('dashboard.html', hero_name=hero)

@main.route('/create-task')
def create_task():
    flash('Task criada com sucesso!', 'success')
    return render_template('dashboard.html')