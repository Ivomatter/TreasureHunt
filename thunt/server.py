import base64

from flask import Flask, render_template, redirect, request, jsonify
from werkzeug.exceptions import RequestEntityTooLarge
from werkzeug.datastructures import FileStorage
from game_state import *

import os
import tempfile

requestProcessor = RequestProcessor()
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16MB
app.config['ALLOWED_EXTENSIONS'] = set(['.jpg', '.jpeg', '.png', '.gif'])
app.config['uploaded_files'] = {}  # Dictionary to store uploaded files in memory

@app.route('/')
def index():
    images = list(app.config['uploaded_files'].keys())
    return render_template('newGame.html', images=images)

@app.route('/game')
def game():
    images = list(app.config['uploaded_files'].keys())
    return render_template('game.html', images=images)

@app.route('/leaderboard')
def leaderboard():
    images = list(app.config['uploaded_files'].keys())
    return render_template('leaderboard.html', images=images)

@app.route('/join_game')
def join_game():
    images = list(app.config['uploaded_files'].keys())
    return render_template('joinGame.html', images=images)

@app.route('/start_game')
def start_game():
    images = list(app.config['uploaded_files'].keys())
    return render_template('createGame.html', images=images)

@app.route('/upload', methods=['POST'])
def upload():
    try:
        file = request.files['file']
        if file:
            app.config['uploaded_files'][file.filename] = base64.b64encode(file.read())
        return redirect('/')
        
  
    except RequestEntityTooLarge:
        return 'File is larger than the 16MB limit.'

@app.route('/backend/create_game', methods=['POST'])
def create_game():
    return requestProcessor.get_response(request.json)


@app.route('/backend/skip_riddle', methods=['POST'])
def skip_riddle():
    print(request.json)
    res = requestProcessor.get_response(request.json)
    return res

@app.route('/backend/guess', methods=['POST'])
def backend_guess():
    user = request.form.get('user')
    room = request.form.get('room')

    file = request.files['file']
    _, file_extension = os.path.splitext(file.filename)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=file_extension)
    file.save(temp_file.name)

    body = {
        'request': 'guess',
        'user': user,
        'room': room,
        'image': temp_file.name  # Send the image file
    }

    return requestProcessor.get_response(body)

@app.route('/backend/leaderboard', methods=['POST'])
def backend_leaderboard():
    user = request.form.get('user')
    room = request.form.get('room')

    body = {
        'request': 'leaderboard',
        'user': user,
        'room': room,
    }

    return requestProcessor.get_response(body)

@app.route('/backend/start_game', methods=['POST'])
def backend_start_game():
    request_data = request.form.get('request')
    user = request.form.get('user')
    room = request.form.get('room')
    duration = request.form.get('duration')
    treasure_count = request.form.get('treasure_count')

    images = []

    for i in range(20): 
        if 'file' + str(i) in request.files:
            file = request.files['file' + str(i)]
            _, file_extension = os.path.splitext(file.filename)
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=file_extension)
            file.save(temp_file.name)
            images.append(temp_file.name)

    body = {
        'request': 'start_game',
        'user': user,
        'room': room,
        'duration': duration,
        'treasure_count': treasure_count,
        'images': images
    }
    
    return requestProcessor.get_response(body)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/send-user-data', methods=['POST'])
def submit_data():
    data = request.json  # Extract JSON data from the request
    user = data.get('user')
    room = data.get('room')
    current_riddle = data.get('current_riddle')
    riddle_count = data.get('riddle_count')

    # Do something with the data, such as storing it in a database
    print("User:", user)
    print("Room:", room)
    print("Current Riddle:", current_riddle)
    print("Riddle Count:", riddle_count)

    # Respond to the client
    response_data = {"message": "Data received successfully"}
    return jsonify(response_data)
    
@app.route('/serve-image/<filename>', methods=['GET'])
def serve_image(filename):
    if filename in app.config['uploaded_files']:
        file_contents = app.config['uploaded_files'][filename]
        encoded_image = base64.b64decode(file_contents)
        return f'<img src="data:image/jpeg;base64,{encoded_image}" alt="{filename}">'
    else:
        return 'File not found.'
    

app.run(debug=True)
