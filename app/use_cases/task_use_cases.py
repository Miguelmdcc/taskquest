from flask import render_template, redirect, url_for, flash
from app.repository.tasks_repository import TaskRepository
from app.repository.user_repository import UserRepository

def createTaskUseCase(request):
    user_id = request.args.get('user_id') or request.form.get('user_id')

    if not user_id:
        flash("Erro: Usuário não identificado para criar tarefa.", "error")
        return redirect(url_for('main.index'))
    
    user = UserRepository().get_user_by_id(user_id)

    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        xp = request.form.get('xp')
        gold = request.form.get('gold')

        if not title or not description or not xp or not gold:
            flash("Todos os campos são obrigatórios para criar uma tarefa.", "error")
            return render_template('create_task.html', user_id=user_id, hero_name=user.hero_name)

        task = TaskRepository()
        task.create_task(user_id=user_id, title=title, description=description, xp_reward=xp, gold_reward=gold)
        return redirect(url_for('main.dashboard', user_id=user_id))

    return render_template('create_task.html', user_id=user_id, hero_name=user.hero_name)

def deleteTaskUseCase(task_id, request):
    user_id = request.args.get('user_id') or request.form.get('user_id')
    if TaskRepository.delete_task_by_id(task_id):
        flash('Missão deletada com sucesso!', 'success')
    else:
        flash('Erro ao deletar a missão.', 'error')
    return redirect(url_for('main.dashboard', user_id=user_id))

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
    read_only = request.args.get('read_only', 'false').lower()
    task = TaskRepository().get_task_by_id(task_id)

    if not task:
        flash("Tarefa não encontrada.", "error")
        return render_template('dashboard.html', user_id=user_id)

    return render_template('task_details.html', task=task, user_id=user_id, read_only=read_only)

def acceptTaskUseCase(task_id, request):
    user_id = request.args.get('user_id') or request.form.get('user_id')
    task = TaskRepository().update_task(task_id=task_id, status='in_progress')
    if task:
        flash("Missão aceita! Boa sorte, herói!", "success")
    else:
        flash("Erro ao aceitar a missão.", "error")
    return redirect(url_for('main.dashboard', user_id=user_id))

def doneTaskUseCase(task_id, request):
    user_id = request.args.get('user_id') or request.form.get('user_id')
    task = TaskRepository().update_task(task_id=task_id, status='completed')
    if task:
        flash("Missão concluída! Parabéns, herói!", "success")
    else:
        flash("Erro ao concluir a missão.", "error")
    return redirect(url_for('main.dashboard', user_id=user_id))