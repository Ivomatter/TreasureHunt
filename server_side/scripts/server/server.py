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