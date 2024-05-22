from main import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    website = db.Column(db.String(255), nullable=False)
    username_email = db.Column(db.String(255), nullable=False)
    encrypted_password = db.Column(db.String(255), nullable=False)

    user = db.relationship('User', backref=db.backref('passwords', lazy=True))
