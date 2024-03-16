# from flask import Flask, render_template, redirect, request, send_from_directory
# from werkzeug.exceptions import RequestEntityTooLarge
# from werkzeug.utils import secure_filename
# import os

# app = Flask(__name__)
# app.config['UPLOAD_DIRECTORY'] = 'uploads/'
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16MB
# app.config['ALLOWED_EXTENSIONS'] = ['.jpg', '.jpeg', '.png', '.gif']

# @app.route('/')
# def index():
#   files = os.listdir(app.config['UPLOAD_DIRECTORY'])
#   images = []

#   for file in files:
#     if os.path.splitext(file)[1].lower() in app.config['ALLOWED_EXTENSIONS']:
#       images.append(file)
  
#   return render_template('index.html', images=images)

# @app.route('/upload', methods=['POST'])
# def upload():
#   try:
#     file = request.files['file']

#     if file:
#       extension = os.path.splitext(file.filename)[1].lower()

#       if extension not in app.config['ALLOWED_EXTENSIONS']:
#         return 'File is not an image.'
        
#       file.save(os.path.join(
#         app.config['UPLOAD_DIRECTORY'],
#         secure_filename(file.filename)
#       ))
  
#   except RequestEntityTooLarge:
#     return 'File is larger than the 16MB limit.'
  
#   return redirect('/')

# @app.route('/serve-image/<filename>', methods=['GET'])
# def serve_image(filename):
#   return send_from_directory(app.config['UPLOAD_DIRECTORY'], filename)

# app.run(debug=True)

import base64


from flask import Flask, render_template, redirect, request
from werkzeug.exceptions import RequestEntityTooLarge
from werkzeug.datastructures import FileStorage

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16MB
app.config['ALLOWED_EXTENSIONS'] = set(['.jpg', '.jpeg', '.png', '.gif'])
app.config['uploaded_files'] = {}  # Dictionary to store uploaded files in memory

@app.route('/')
def index():
    images = list(app.config['uploaded_files'].keys())
    return render_template('index.html', images=images)

@app.route('/upload', methods=['POST'])
def upload():
    try:
        file = request.files['file']

        
        app.config['uploaded_files'][file.filename] = base64.b64encode(file.read())
        # app.config CONTAINS THE ENCODED IMAGES
        print(app.config['uploaded_files'][file.filename])
        return redirect('/')
        
  
    except RequestEntityTooLarge:
        return 'File is larger than the 16MB limit.'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/serve-image/<filename>', methods=['GET'])
def serve_image(filename):
    if filename in app.config['uploaded_files']:
        file_contents = app.config['uploaded_files'][filename]
        encoded_image = base64.b64encode(file_contents).decode('utf-8')
        return f'<img src="data:image/jpeg;base64,{encoded_image}" alt="{filename}">'
    else:
        return 'File not found.'
    
    

app.run(debug=True)