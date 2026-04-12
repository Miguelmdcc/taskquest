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
    def get_user_by_real_name_and_hero_name(real_name, hero_name):
        user =  User.query.filter_by(real_name=real_name, hero_name=hero_name).first()
        if not user:
            return user
        return user
    
    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)
    
    @staticmethod
    def user_rewards(user_id, xp, gold):
        user = User.query.get(user_id)
        if user:
            user.xp += xp
            while user.xp >= 100:
                user.level += 1
                user.xp = user.xp - 100
            user.gold += gold
            db.session.commit()
            return user
        return None
    
    @staticmethod
    def reset_user_progress(user_id):
        user = User.query.get(user_id)
        if user:
            user.level = 1
            user.xp = 0
            user.gold = 0
            db.session.commit()
            return user
        return None