from app.models.boss import Boss
from app import db

class BossRepository():
    @staticmethod
    def create_boss_if_not_exists(name='Procastinator', hp=100, xp_reward=50, gold_reward=25, user_id=1):
        boss = Boss.query.filter_by(user_id=user_id).first()
        if not boss:
            boss = Boss(name=name, hp=hp, xp_reward=xp_reward, gold_reward=gold_reward, user_id=user_id)
            db.session.add(boss)
        db.session.commit()
        return boss
    
    @staticmethod
    def hurt_boss(user_id, damage):
        boss = Boss.query.filter_by(user_id=user_id).first()
        if boss:
            boss_hp = boss.hp
            boss.hp = boss_hp - damage
            if boss.hp <= 0:
                boss.status = 'defeated'
            db.session.commit()
            return boss
        return None