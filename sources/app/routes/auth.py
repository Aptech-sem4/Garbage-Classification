from flask import Blueprint, render_template, request, url_for, redirect
# from flask_login import LoginManager
from app.repositories.auth import User
from flask import current_app
from app import login_manager
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


auth_bp = Blueprint('auth', __name__)

# login_manager = LoginManager(current_app)
users = {
    'admin': User('admin', 'team1'),
}                                                                                    


@login_manager.user_loader
def load_user(username):
    return users.get(username)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = users.get(username)
        # print(user)
        # print(password)
        # print(user.check_password(password))
        if user and user.check_password(password):
            login_user(user)
            # flash('Login successful', 'success')
            return redirect(url_for('index.index'))
        else:
            return redirect(request.url)
            # return('Invalid username or password', 'danger')

    return render_template('login.html')



@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

