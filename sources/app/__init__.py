from flask import Flask, render_template, current_app
import  os
import configparser

app = Flask(__name__)

# Thiết lập cấu hình
app.config['UPLOAD_FOLDER'] = 'app/static/uploads'

# with app.app_context():
# Thực hiện các hoạt động yêu cầu ngữ cảnh ứng dụng ở đây
root_path_folder = app.root_path
# Lấy thư mục chứa file hiện tại
current_directory = root_path_folder + '/models/files'
config_init = configparser.ConfigParser()
ini_path = os.path.join(os.getcwd(),'config.ini')
print(ini_path)
config_init.read(ini_path)
print(config_init['MODEL']['ver'])
MODEL_PATH = os.path.join(current_directory, config_init['MODEL']['ver'])


# Import Blueprint và đăng ký Blueprint vào app
from app.routes import upload, index, version
# predict

app.register_blueprint(index.index_bp)
app.register_blueprint(upload.upload_bp)
app.register_blueprint(version.version_bp)

# app.register_blueprint(predict.predict_bp)
