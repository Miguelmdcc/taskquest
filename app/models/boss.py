from app import db

class Boss(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    hp = db.Column(db.Integer, default=10)
    xp_reward = db.Column(db.Integer, default=50)
    gold_reward = db.Column(db.Integer, default=25)
    status = db.Column(db.Enum('alive', 'defeated'), default='alive', nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    def __repr__(self):
        return f"<Boss {self.name}>"