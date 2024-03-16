from flask import Flask, render_template
from server.request_proccessor import RequestProcessor

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("login.html")

if __name__ == '__main__':
    request_processor: RequestProcessor
    app.run(debug=True)