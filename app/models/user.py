from app import db
from app.models.token import Token

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {'username': self.username, 'email': self.email}
    
    @classmethod
    def get_all(cls):
        return {'users': [user.json() for user in cls.query.all()]}

    @classmethod
    def find_by_username_password(cls, username: str, password: str):
        return cls.query.filter_by(username=username, password=password).first()

    @classmethod
    def find_by_email(cls, email: str):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_username(cls, username: str):
        return cls.query.filter_by(username=username).first()

    def __repr__(self):
        return '<User {}>'.format(self.username)