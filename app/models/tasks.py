from flask_sqlalchemy import SQLAlchemy
from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    xp_reward = db.Column(db.Integer, default=10)
    gold_reward = db.Column(db.Integer, default=5)
    status = db.Column(db.Enum('pending', 'in_progress', 'completed'), default='pending', nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"<Task {self.name}>"
