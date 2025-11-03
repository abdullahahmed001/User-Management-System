from click import password_option
from flask import request, render_template, redirect, url_for, render_template_string

import username
from flask import render_template
from wtforms.validators import email
from . import db
from .forms import LoginForm
#from app import myapp_obj
from flask import current_app as myapp_obj
from flask import jsonify
from .models import User

@myapp_obj.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')
        else:
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')

        if not username or not email or not password:
            return jsonify({'error': 'Username, email, and password required'}), 400

        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': f'User {username} added successfully!'})

    # GET → show HTML form
    return render_template_string('''
        <h2>Add User</h2>
        <form method="POST">
            Username: <input type="text" name="username"><br>
            Email: <input type="email" name="email"><br>
            Password: <input type="password" name="password"><br>
            <button type="submit">Add User</button>
        </form>
    ''')


# Search for a user
@myapp_obj.route('/search_user/<email>', methods=['GET'])
def search_user(email):
    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({'id': user.id, 'username': user.username, 'email': user.email})
    else:
        return jsonify({'error': 'User not found'}), 404
# Delete a user
@myapp_obj.route('/delete_user/<email>', methods=['GET','POST'])
def delete_user(email):
    if request.method == 'POST':
        email = request.form.get('email') or (request.get_json() or {}).get('email')
        if not email:
            return jsonify({'error': 'Email required'}), 400

        user = User.query.filter_by(email=email).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({'message': f'User {user.username} deleted successfully!'})
        else:
            return jsonify({'message': 'User not found'}), 404

    # GET → show a simple form to delete users
    return render_template_string('''
        <h2>Delete User</h2>
        <form method="POST">
            Email: <input type="email" name="email"><br>
            <button type="submit">Delete User</button>
        </form>
    ''')
@myapp_obj.route('/')
# view functions
def hello():
    return '<h1>hello world</h1>'

# http://127.0.0.1:5000/members/Carlos/
@myapp_obj.route('/members/<string:naame>/')
def member(naame):
    return naame

@myapp_obj.route('/morn')
def morning():
    return 'Good Morning!'

@myapp_obj.route('/login')
def login():
    form = LoginForm()
    abc = {'name':'carlos'}
    return render_template('login.html', users=abc, form=form)

@myapp_obj.route('/calling_db')
def calling_db():
    users = User.query.all()
    users_list = [{"id": u.id, "name": u.name} for u in users]
    return jsonify(users_list)


