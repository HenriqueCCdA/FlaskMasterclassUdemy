from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(85), nullable=True)
    email = db.Column(db.String(85), nullable=True, unique=True, index=True)
    password = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return self.name
