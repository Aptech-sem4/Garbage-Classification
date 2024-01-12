from flask import Flask, render_template, current_app
import  os
from dotenv import load_dotenv

app = Flask(__name__)

# Thiết lập cấu hình
app.config['UPLOAD_FOLDER'] = 'app/static/uploads'

root_path_folder = app.root_path
# Lấy thư mục chứa file hiện tại
current_directory = root_path_folder + '/models/files'
path_env = os.path.join(root_path_folder, '.env')

load_dotenv(path_env)
app.config['VER'] = os.getenv('VER')
ver_app = app.config['VER']

MODEL_PATH = os.path.join(current_directory, ver_app)

# Import Blueprint và đăng ký Blueprint vào app
from app.routes import upload, index, version, auth
# predict

app.register_blueprint(index.index_bp)
app.register_blueprint(upload.upload_bp)
app.register_blueprint(version.version_bp)
app.register_blueprint(auth.auth_bp)

# app.register_blueprint(predict.predict_bp)
