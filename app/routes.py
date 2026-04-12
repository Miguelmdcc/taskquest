from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.repository.user_repository import UserRepository
from app.repository.boss_repository import BossRepository
from app.repository.tasks_repository import TaskRepository
from app.use_cases.user_use_cases import createUserUseCase, loginUserUseCase
from app.use_cases.task_use_cases import createTaskUseCase, deleteTaskUseCase, getTaskDetailsUseCase, acceptTaskUseCase
from app.use_cases.dashboard_use_cases import showDashboardUseCase


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

@main.route('/dashboard/accept_task/<int:task_id>', methods=['POST'])
def accept_task(task_id):
    return acceptTaskUseCase(task_id, request)