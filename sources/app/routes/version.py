from flask import Blueprint, render_template, request, redirect, url_for
import os
from flask import current_app
from dotenv import set_key, dotenv_values
from repository.auth import User
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


version_bp = Blueprint('version', __name__)

@version_bp.route('/load-version', methods=['GET', 'POST'])
def load_version():
    list_files = get_list_files()
    current_ver = get_current_version()
    if request.method == "POST":
        if 'file' not in request.files:
            return 'No file part'

        file = request.files['file']

        if file.filename == '':
            return redirect(request.url) 

        if file:
            folder_name = '/models/files'
            root_path = current_app.root_path
            absolute_path = root_path + folder_name
            file.save(os.path.join(absolute_path, file.filename))
            return redirect(request.url) 
        
    return render_template('version.html', files=list_files, ver = current_ver)


@version_bp.route('/pick-version', methods=[ 'POST'])
def pick_version():
    if request.method == 'POST':
        if 'version_model' in request.form and request.form['version_model'] is not None:
            model_name = request.form['version_model']     
            set_key('.env', 'VER', model_name)

    return redirect(url_for('version.load_version')) 


def get_current_version():
    env_vars = dotenv_values('.env')
    return env_vars.get('VER')


def get_list_files():
    folder_name = '/models/files'
    root_path = current_app.root_path
    absolute_path = root_path + folder_name
    if os.path.exists(absolute_path) and os.path.isdir(absolute_path):
        files = os.listdir(absolute_path)
        return files
    else:
        return 'Folder not found or is not a directory'
