from flaskr import db
from flask_login import UserMixin

class User(db.Model,UserMixin):
    __tabelname__ = 'b_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username
