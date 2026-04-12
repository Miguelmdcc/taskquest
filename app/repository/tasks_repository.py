from app.models.tasks import Task
from app import db

class TaskRepository:
    @staticmethod
    def create_task(title='Titulo', description='Descrição padrão', xp_reward=10, gold_reward=5, user_id=1):
        task = Task(title=title, description=description, xp_reward=xp_reward, gold_reward=gold_reward, user_id=user_id)
        db.session.add(task)
        db.session.commit()
        return task