from flask import Flask, request

app = Flask(__name__)

@app.route('/api/data', methods = ['GET', 'POST'])
def manage_data():
    if request.method == 'GET':
        return {"message": "GET request received!"}
    
    elif request.method == 'POST':
        json_data = request.get_json()
        return {"message": "POST request received! Here's your data:", "data": json_data}

if __name__ == "__main__":
    app.run(port=5000)