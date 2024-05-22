from flask import Flask
from cryptography.fernet import Fernet
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///passwords.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'THISISSECURITYKEY'

db = SQLAlchemy(app)

key = Fernet.generate_key()
cipher_suite = Fernet(key)
app.config['ENCRYPTION_KEY'] = key

from routes import *

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)