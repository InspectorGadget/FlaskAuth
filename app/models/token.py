from app import db
import secrets

class Token(db.Model):
    __tablename__ = "tokens"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(80), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User')

    def __init__(self, url, user_id):
        self.url = url
        self.token = secrets.token_urlsafe(16)
        self.user_id = user_id

    def json(self):
        return {'url': url}

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def delete_all_tokens(cls, user_id: int):
        for token in cls.query.filter_by(user_id=user_id).all():
            db.session.delete(token)
            db.session.commit()

    def __repr__(self):
        return '<UserToken {}>'.format(self.user_id)