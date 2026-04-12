from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.repository.user_repository import UserRepository
from app.repository.boss_repository import BossRepository
from app.use_cases.create_user import createUserUseCase
from app.use_cases.login_user import loginUserUseCase
from app.use_cases.create_task import createTaskUseCase

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
    hero_name = request.args.get('hero_name')
    real_name = request.args.get('real_name')
    user = UserRepository().get_user(real_name=real_name, hero_name=hero_name)
    boss = BossRepository().create_boss(user_id=user.id)

    return render_template('dashboard.html', user=user, boss=boss)

@main.route('/create-task')
def create_task():
    return createTaskUseCase(request)