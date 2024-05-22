from flask import render_template, request, redirect, url_for, session, flash
from main import app, db, cipher_suite
from models import User, Password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:  # Replace with hashed password check
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))

        flash('Invalid username or password', 'error')

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        user_id = session['user_id']
        user = User.query.get(user_id)
        passwords = Password.query.filter_by(user_id=user_id).all()
        return render_template('dashboard.html', user=user, passwords=passwords)

    return redirect(url_for('login'))

@app.route('/add_password', methods=['POST'])
def add_password():
    if 'user_id' in session:
        user_id = session['user_id']
        website = request.form['website']
        username_email = request.form['username_email']
        password = request.form['password']

        encrypted_password = cipher_suite.encrypt(password.encode()).decode()

        new_password = Password(user_id=user_id, website=website, username_email=username_email, encrypted_password=encrypted_password)
        db.session.add(new_password)
        db.session.commit()

        flash('Password added successfully', 'success')

    return redirect(url_for('dashboard'))

@app.route('/decrypt_password/<int:password_id>')
def decrypt_password(password_id):
    if 'user_id' in session:
        password = Password.query.get(password_id)
        if password:
            decrypted_password = cipher_suite.decrypt(password.encrypted_password.encode()).decode()
            return decrypted_password

    return 'Error: Password not found or unauthorized access'

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))
