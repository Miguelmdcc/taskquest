from app.repository.tasks_repository import TaskRepository
from flask import redirect, url_for, flash

def deleteTaskUseCase(task_id, request):
    user_id = request.args.get('user_id') or request.form.get('user_id')
    if TaskRepository.delete_task_by_id(task_id):
        flash('Missão deletada com sucesso!', 'success')
    else:
        flash('Erro ao deletar a missão.', 'error')
    return redirect(url_for('main.dashboard', user_id=user_id))