from app.repository.user_repository import UserRepository
from app.repository.boss_repository import BossRepository
from app.repository.tasks_repository import TaskRepository
from flask import render_template

def showDashboardUseCase(request):
    user_id = request.args.get('user_id')
    user = UserRepository().get_user_by_id(user_id=user_id)
    boss = BossRepository().create_boss_if_not_exists(user_id=user_id)
    task = TaskRepository().get_by_user(user_id=user_id)

    return render_template('dashboard.html', user=user, boss=boss, tasks=task)