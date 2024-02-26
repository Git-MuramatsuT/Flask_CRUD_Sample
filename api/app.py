from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def hello():
    message = "Hello World"
    return message

@app.route('/test', methods=['GET'])
def test():
    message = "test"
    return message

if __name__ == '__main__':
    app.run(debug=True)