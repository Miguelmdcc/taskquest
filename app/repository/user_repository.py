from app.models.user import User
from app import db

class UserRepository:
    @staticmethod
    def create_user_if_not_exists(real_name, hero_name):
        user = User.query.filter_by(real_name=real_name, hero_name=hero_name).first()
        if not user:
            user = User(real_name=real_name, hero_name=hero_name)
            db.session.add(user)
            db.session.commit()
            return user

        return None

    @staticmethod
    def get_user(real_name, hero_name):
        user =  User.query.filter_by(real_name=real_name, hero_name=hero_name).first()
        if not user:
            return user
        return user