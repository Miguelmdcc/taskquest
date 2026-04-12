from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from app import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    real_name = db.Column(db.String(100), nullable=False)
    hero_name = db.Column(db.String(100), nullable=False)
    level = db.Column(db.Integer, default=1)
    xp = db.Column(db.Integer, default=0)
    gold = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<User {self.real_name} ({self.hero_name})>"
