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
    
    @staticmethod
    def delete_task_by_id(task_id):
        task = Task.query.get(task_id)
        if task:
            db.session.delete(task)
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def get_task_by_id(task_id):
        return Task.query.get(task_id)
    
    @staticmethod
    def update_task(task_id=None, title=None, description=None, xp_reward=None, gold_reward=None, status=None):
        if not task_id:
            return None
        task = Task.query.get(task_id)
        if not task:
            return None
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        if xp_reward is not None:
            task.xp_reward = xp_reward
        if gold_reward is not None:
            task.gold_reward = gold_reward
        if status is not None:
            task.status = status
        db.session.commit()
        return task