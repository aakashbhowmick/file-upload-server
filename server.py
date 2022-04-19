from flask import Flask
from flask import request

app = Flask("test")
@app.route("/")
def hello_word():
    response = { 'name' : 'Aakash', 'age'  : 31 }
    return response

@app.route('/store', methods=['POST'])
def post_file():
    print('Received post data')