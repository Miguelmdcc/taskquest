from flask import render_template, redirect, url_for, request, flash
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