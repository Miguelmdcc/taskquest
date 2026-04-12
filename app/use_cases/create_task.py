from flask import flash, render_template
from app.repository.tasks_repository import TaskRepository

def createTaskUseCase(request):
    task = TaskRepository.create_task()
    flash('Task criada com sucesso!', 'success')
    return render_template('dashboard.html')