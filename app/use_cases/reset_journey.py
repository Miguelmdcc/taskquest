from app.repository.user_repository import UserRepository
from app.repository.boss_repository import BossRepository
from app.repository.tasks_repository import TaskRepository
from flask import redirect, url_for, flash

def resetJourneyUseCase(user_id):
    print("Reset Journey Use Case called")
    user = UserRepository().reset_user_progress(user_id)
    if not user:
        flash("Erro: Usuário não encontrado para resetar a jornada.", "error")
    boss_deleted = BossRepository().delete_boss_by_user_id(user_id)
    if not boss_deleted:
        flash("Erro: Não foi possível deletar o chefe associado ao usuário.", "error")
    tasks_deleted = TaskRepository().delete_tasks_by_user_id(user_id)
    if not tasks_deleted:
        flash("Erro: Não foi possível deletar as tarefas associadas ao usuário.", "error")
    
    return redirect(url_for('main.dashboard', user_id=user_id))
