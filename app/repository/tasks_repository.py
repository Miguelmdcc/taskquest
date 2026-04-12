from app.models.tasks import Task
from app import db

class TaskRepository:
    @staticmethod
    def create_task(user_id, title='Titulo', description='Descrição', xp_reward=10, gold_reward=5):
        task = Task(title=title, description=description, xp_reward=xp_reward, gold_reward=gold_reward, user_id=user_id)
        db.session.add(task)
        db.session.commit()
        return task
    
    @staticmethod
    def get_by_user(user_id):
        return Task.query.filter_by(user_id=user_id).all()