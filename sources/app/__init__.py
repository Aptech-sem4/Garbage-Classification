from flask import Flask, render_template, current_app
import  os
from dotenv import load_dotenv

app = Flask(__name__)

# Thiết lập cấu hình
app.config['UPLOAD_FOLDER'] = 'app/static/uploads'

# with app.app_context():
# Thực hiện các hoạt động yêu cầu ngữ cảnh ứng dụng ở đây
# try:
root_path_folder = app.root_path
print(root_path_folder)
# Lấy thư mục chứa file hiện tại
current_directory = root_path_folder + '/models/files'

load_dotenv('.env')
app.config['VER'] = os.getenv('VER')
ver_app = app.config['VER']

# print(app.config['VER'])
MODEL_PATH = os.path.join(current_directory, ver_app)
# except Exception as e:
#     print(f"An error occurred: {e}")


# Import Blueprint và đăng ký Blueprint vào app
from app.routes import upload, index, version
# predict

app.register_blueprint(index.index_bp)
app.register_blueprint(upload.upload_bp)
app.register_blueprint(version.version_bp)

# app.register_blueprint(predict.predict_bp)
