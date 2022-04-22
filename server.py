from flask import Flask
from flask import request
from flask_tus import tus_manager

app = Flask("test")
@app.route("/")
def hello_word():
    response = { 'name' : 'Aakash', 'age'  : 31 }
    return response

@app.route('/store', methods=['POST'])
def post_file():
    print('Received post data')

tm = tus_manager(app, upload_url='/upload', upload_folder='D:/dev/file_upload_app/uploaded')