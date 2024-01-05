from flask import Blueprint, render_template, request,jsonify, redirect, Response, send_file
import os, requests
from flask import current_app
from dotenv import load_dotenv
import configparser

version_bp = Blueprint('version', __name__)

@version_bp.route('/load-version', methods=['GET', 'POST'])
def load_version():
    if request.method == 'POST':
        print('vao ne')
        link = "https://drive.google.com/drive/folders/1lfL24Zc8kfBekuiyBhKOt_r7K4m6dC96?usp=sharing"
        res = download_all_files(link)   
        print(res)
    
    list_files = get_list_files()
    current_ver = get_current_version()
    return render_template('version.html', files=list_files, ver = current_ver)


def download_all_files(link):
    try:
        #link = request.args.get('link')  # Get the link from request query parameter
        if not link:
            return "Please provide a valid link."

        response = requests.get(link)

        # Check if the request was successful
        if response.status_code == 200:
            # Get the content disposition to identify filenames
            content_disposition = response.headers.get('content-disposition')
            print(content_disposition)
            if content_disposition:
                # Extract filenames from content disposition
                filenames = [filename.strip()[len('filename='):] for filename in content_disposition.split(';') if filename.strip().startswith('filename=')]
                for filename in filenames:
                    # Set up response headers to trigger file download
                    headers = {
                        'Content-Type': 'application/octet-stream',
                        'Content-Disposition': f'attachment; filename={filename}'
                    }
                    return send_file(response.content, as_attachment=True, attachment_filename=filename, headers=headers)
            else:
                return "No files found at the provided link."
        else:
            return f"Failed to fetch files from the link. Status code: {response.status_code}"
    except Exception as e:
        return f"An error occurred: {str(e)}"


def get_current_version():
    load_dotenv('.env')
    return os.getenv('VER')


def get_list_files():
    folder_name = '/models/files'
    root_path = current_app.root_path
    absolute_path = root_path + folder_name
    if os.path.exists(absolute_path) and os.path.isdir(absolute_path):
        files = os.listdir(absolute_path)
        return files
    else:
        return 'Folder not found or is not a directory'
