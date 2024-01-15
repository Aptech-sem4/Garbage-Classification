from flask import Flask, render_template, current_app, redirect, url_for
import  os
from dotenv import load_dotenv
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

# Thiết lập cấu hình
app.config['UPLOAD_FOLDER'] = 'app/static/uploads'

root_path_folder = app.root_path
# Lấy thư mục chứa file hiện tại
current_directory = root_path_folder + '/models/files'
path_env = os.path.join(root_path_folder, '.env')

load_dotenv(path_env)
app.config['VER'] = os.getenv('VER')
app.config['SECRET_KEY'] = 'xxxxxxxxxxx'
ver_app = app.config['VER']

MODEL_PATH = os.path.join(current_directory, ver_app)

# Import Blueprint và đăng ký Blueprint vào app
from app.routes import upload, index, version, auth
# predict


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect(url_for('auth.login'))


app.register_blueprint(index.index_bp)
app.register_blueprint(upload.upload_bp)
app.register_blueprint(version.version_bp)
app.register_blueprint(auth.auth_bp)

# app.register_blueprint(predict.predict_bp)
