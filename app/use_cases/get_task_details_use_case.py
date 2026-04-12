from app.repository.tasks_repository import TaskRepository
from flask import render_template, flash, redirect, url_for

def getTaskDetailsUseCase(request):
    if request.method == 'POST':
        task_id = request.form.get('task_id')
        user_id = request.form.get('user_id')
        print("task_id:", task_id)
        print("user_id:", user_id)
        task_title = request.form.get('title')
        task_description = request.form.get('description')
        task_xp = request.form.get('xp')
        task_gold = request.form.get('gold')

        task = TaskRepository().update_task(task_id=task_id, title=task_title, description=task_description, xp_reward=task_xp, gold_reward=task_gold)

        if task:
            flash("Missão atualizada com sucesso!", "success")
            return redirect(url_for('main.dashboard', user_id=user_id))
        else:
            flash("Erro ao atualizar a missão.", "error")
            return render_template('task_details.html', task=task, user_id=user_id)
        
    task_id = request.args.get('task_id')
    user_id = request.args.get('user_id')
    task = TaskRepository().get_task_by_id(task_id)

    if not task:
        flash("Tarefa não encontrada.", "error")
        return render_template('dashboard.html', user_id=user_id)

    return render_template('task_details.html', task=task, user_id=user_id)