from flask import Flask
# from flask import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Password_manager.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# Import routes after initializing app and db
from route import *

if __name__ == '__main__':
    app.run(debug=True)