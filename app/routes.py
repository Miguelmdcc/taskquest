from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.repository.user_repository import UserRepository
from app.repository.boss_repository import BossRepository
from app.repository.tasks_repository import TaskRepository
from app.use_cases.create_user import createUserUseCase
from app.use_cases.login_user import loginUserUseCase
from app.use_cases.create_task import createTaskUseCase
from app.use_cases.delete_task import deleteTaskUseCase
from app.use_cases.show_dashboard import showDashboardUseCase
from app.use_cases.get_task_details_use_case import getTaskDetailsUseCase

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
    return showDashboardUseCase(request)

@main.route('/dashboard/create-task', methods=['GET', 'POST'])
def create_task():
    return createTaskUseCase(request)

@main.route('/dashboard/delete-task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    return deleteTaskUseCase(task_id, request)

@main.route('/dashboard/task/', methods=['GET', 'POST'])
def get_task_details():
    return getTaskDetailsUseCase(request)