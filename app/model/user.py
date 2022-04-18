from database import db

class User(db.Model):
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False, server_default='')

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):

        db.session.add(self)
        db.session.commit()

    def remove_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def find_user_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()